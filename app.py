import streamlit as st

st.set_page_config(page_title="Code Reference", page_icon="📖", layout="centered")

# ─────────────────────────────────────────
# HIDE STREAMLIT BRANDING
# ─────────────────────────────────────────

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden !important;}
    [data-testid="stToolbar"] {visibility: hidden !important;}
    [data-testid="stBottomBlockContainer"] {visibility: hidden !important;}
    </style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# DATA
# ─────────────────────────────────────────

COMMANDS = {
    "Python": {
        "categories": ["All", "Strings", "Lists", "Dicts", "Files", "Functions", "Control flow", "Dates"],
        "commands": [
            {
                "name": "print()",
                "category": "Functions",
                "what": "Outputs text or values to the console. You can pass multiple arguments — they'll be joined with a space.",
                "code": 'print("Hello world")\nprint("Name:", name)\nprint(f"You have {n} items")',
                "gotcha": None,
                "tip": "f-strings (f\"...\") let you embed variables directly inside quotes — much cleaner than joining with commas.",
            },
            {
                "name": "len()",
                "category": "Functions",
                "what": "Returns the number of items in a string, list, dict, or any collection.",
                "code": 'name = "Ozzie"\nprint(len(name))      # 5 (characters)\n\nworkouts = ["Run", "Swim"]\nprint(len(workouts))  # 2 (items)',
                "gotcha": None,
                "tip": None,
            },
            {
                "name": "None",
                "category": "Functions",
                "what": "None means 'no value'. It's not zero, not an empty string — it's the absence of anything. Use it as a default when something might not exist.",
                "code": '# Use None as a default\nweight = None\n\n# Check if something has a value\nif weight is None:\n    print("No weight entered")\n\nif weight is not None:\n    print(f"Weight: {weight}kg")\n\n# Functions return None by default if no return statement\ndef greet(name):\n    print("Hi", name)\n    # no return = returns None\n\nresult = greet("Dad")  # result is None',
                "gotcha": "Use 'is None' and 'is not None' to check for None — don't use == None.",
                "tip": "In the workout tracker, weight_kg=None means the user didn't enter a weight. You check 'if w.get(\"weight_kg\") is not None' before showing it.",
            },
            {
                "name": "def (functions)",
                "category": "Functions",
                "what": "Defines a reusable block of code. Call it later by name. Use return to send a value back.",
                "code": '# Basic function\ndef greet(name):\n    return f"Hello, {name}!"\n\nmessage = greet("Dad")\nprint(message)  # Hello, Dad!\n\n# Default argument\ndef greet(name="friend"):\n    return f"Hello, {name}!"\n\n# Function with no return (just does stuff)\ndef show_welcome():\n    st.title("Welcome")\n    st.write("Please log in")\n\n# Call it\nshow_welcome()',
                "gotcha": None,
                "tip": "Functions that don't return anything are great for Streamlit pages — define all the page content inside the def, then call the function from your router at the bottom.",
            },
            {
                "name": "if / elif / else",
                "category": "Control flow",
                "what": "Runs code only when a condition is True. elif and else are optional branches.",
                "code": 'age = 20\n\nif age < 18:\n    print("Minor")\nelif age < 65:\n    print("Adult")\nelse:\n    print("Senior")\n\n# One-line check\nif username == "Dad":\n    st.write("Welcome back Dad")',
                "gotcha": "Python uses indentation (4 spaces) instead of brackets. Wrong indentation = error.",
                "tip": None,
            },
            {
                "name": "for loop",
                "category": "Control flow",
                "what": "Loops over every item in a list, string, or other iterable.",
                "code": 'workouts = ["Run", "Swim", "Lift"]\n\nfor w in workouts:\n    print(w)\n\n# Loop with index using enumerate()\nfor i, w in enumerate(workouts):\n    print(i, w)  # 0 Run, 1 Swim, 2 Lift\n\n# Loop in reverse using reversed()\nfor w in reversed(workouts):\n    print(w)  # Lift, Swim, Run\n\n# Both — reversed with index\nfor i, w in reversed(list(enumerate(workouts))):\n    print(i, w)  # 2 Lift, 1 Swim, 0 Run',
                "gotcha": None,
                "tip": "enumerate() gives you the index AND the item — used in the workout tracker to loop sessions with their real index for deleting.",
            },
            {
                "name": "reversed()",
                "category": "Control flow",
                "what": "Loops through a list backwards without changing the original list. Wrap in list() if you need the index too.",
                "code": 'sessions = ["Mon", "Wed", "Fri"]\n\n# Show newest first\nfor s in reversed(sessions):\n    print(s)  # Fri, Wed, Mon\n\n# With index (needed for delete buttons)\nfor real_index, s in reversed(list(enumerate(sessions))):\n    print(real_index, s)\n    # 2 Fri, 1 Wed, 0 Mon',
                "gotcha": "reversed() on its own doesn't give you the index. Wrap in list(enumerate(...)) first, then reversed() around the outside.",
                "tip": "The workout tracker uses this in the history page so newest sessions show at the top, and the delete button still uses the correct original index.",
            },
            {
                "name": "while loop",
                "category": "Control flow",
                "what": "Keeps running a block of code as long as a condition stays True.",
                "code": 'count = 0\n\nwhile count < 5:\n    print(count)\n    count += 1  # MUST change something or loops forever',
                "gotcha": "Always make sure the condition will eventually become False, or your program hangs.",
                "tip": None,
            },
            {
                "name": "try / except",
                "category": "Control flow",
                "what": "Catches errors so your program doesn't crash. Put risky code in try, handle the error in except.",
                "code": 'try:\n    number = int("abc")  # this will fail\nexcept ValueError:\n    print("That wasn\'t a number")\n\n# Catch any error and see what it was\ntry:\n    result = risky_function()\nexcept Exception as e:\n    print("Something went wrong:", e)\n\n# Used in workout tracker for date parsing\ntry:\n    d = datetime.strptime(raw, "%Y-%m-%d").date()\nexcept ValueError:\n    pass  # skip bad dates silently',
                "gotcha": "Don't use bare except: — it catches everything. Use except Exception as e: or a specific error type like ValueError.",
                "tip": None,
            },
            {
                "name": "list [ ]",
                "category": "Lists",
                "what": "An ordered, changeable collection. Items are indexed from 0.",
                "code": 'fruits = ["apple", "banana", "cherry"]\n\nprint(fruits[0])   # apple (first)\nprint(fruits[-1])  # cherry (last)\n\nfruits.append("mango")   # add to end\nfruits.pop()             # remove last\nfruits.pop(0)            # remove by index\n\n# Check if item exists\nif "apple" in fruits:\n    print("Found it")',
                "gotcha": "Index starts at 0, not 1. fruits[1] is the SECOND item.",
                "tip": "fruits[-1] is a shortcut for the last item — works on any list.",
            },
            {
                "name": "list slicing",
                "category": "Lists",
                "what": "Grab a chunk of a list using [start:end]. End index is NOT included.",
                "code": 'nums = [0, 1, 2, 3, 4, 5]\n\nprint(nums[1:4])   # [1, 2, 3]\nprint(nums[:3])    # [0, 1, 2] — from start\nprint(nums[3:])    # [3, 4, 5] — to end\nprint(nums[::-1])  # [5,4,3,2,1,0] — reversed',
                "gotcha": None,
                "tip": "[::-1] is a neat trick to reverse any list or string.",
            },
            {
                "name": "list comprehension",
                "category": "Lists",
                "what": "A compact way to build a new list by transforming or filtering another list.",
                "code": 'nums = [1, 2, 3, 4, 5]\n\n# Square every number\nsquares = [n * n for n in nums]\n# [1, 4, 9, 16, 25]\n\n# Filter — only even numbers\nevens = [n for n in nums if n % 2 == 0]\n# [2, 4]\n\n# Real example from workout tracker:\n# Get all unique dates from sessions\ndates = sorted(set(s["date"] for s in user_sessions if "date" in s))',
                "gotcha": None,
                "tip": "Readable for simple cases. If the logic gets complex, use a regular for loop instead.",
            },
            {
                "name": "dict { }",
                "category": "Dicts",
                "what": "A key-value store. Look up values by key instead of by position.",
                "code": 'person = {\n    "name": "Dad",\n    "age": 40,\n    "active": True\n}\n\nprint(person["name"])       # Dad\nperson["age"] = 41          # update\nperson["city"] = "London"   # add new key\n\n# Check key exists before accessing\nif "city" in person:\n    print(person["city"])',
                "gotcha": "Accessing a key that doesn't exist crashes with KeyError. Use .get() to avoid this.",
                "tip": 'person.get("city", "unknown") returns "unknown" instead of crashing if the key is missing.',
            },
            {
                "name": "dict methods",
                "category": "Dicts",
                "what": "Useful built-in methods for working with dictionaries.",
                "code": 'd = {"a": 1, "b": 2, "c": 3}\n\nd.keys()    # dict_keys(["a", "b", "c"])\nd.values()  # dict_values([1, 2, 3])\nd.items()   # pairs — good for loops\n\nfor key, value in d.items():\n    print(key, "->", value)\n\n# .get() — safe access with fallback\nd.get("a")       # 1\nd.get("z")       # None (no crash)\nd.get("z", 0)    # 0 (custom fallback)',
                "gotcha": None,
                "tip": None,
            },
            {
                "name": "str methods",
                "category": "Strings",
                "what": "Strings have built-in methods for formatting, searching, and splitting.",
                "code": 's = "  Hello World  "\n\ns.strip()           # "Hello World" — trim spaces\ns.lower()           # "  hello world  "\ns.upper()           # "  HELLO WORLD  "\ns.replace("o", "0") # "  Hell0 W0rld  "\ns.split(" ")        # split into list\n\n"world" in s.lower()  # True — contains check',
                "gotcha": "String methods return a NEW string — they don't change the original. You must assign the result.",
                "tip": None,
            },
            {
                "name": "f-strings",
                "category": "Strings",
                "what": "The modern way to embed variables inside strings. Prefix the string with f and put variables in {}.",
                "code": 'name = "Ozzie"\nage = 15\n\nprint(f"Name: {name}, Age: {age}")\n\n# Expressions work too\nprint(f"In 10 years: {age + 10}")\n\n# Format numbers\npi = 3.14159\nprint(f"Pi is {pi:.2f}")  # Pi is 3.14\n\n# Used everywhere in workout tracker\nst.write(f"You have **{len(sessions)}** sessions")',
                "gotcha": None,
                "tip": ":.2f inside the braces rounds to 2 decimal places. :, adds thousand separators.",
            },
            {
                "name": "open() / read / write files",
                "category": "Files",
                "what": "Read from or write to a file on disk. Always use with open() so the file closes automatically.",
                "code": '# Write to a file\nwith open("data.txt", "w") as f:\n    f.write("Hello\\n")\n\n# Read entire file\nwith open("data.txt", "r") as f:\n    content = f.read()\n\n# Append without overwriting\nwith open("data.txt", "a") as f:\n    f.write("New line\\n")',
                "gotcha": '"w" overwrites the file completely. Use "a" to append without deleting existing content.',
                "tip": None,
            },
            {
                "name": "import json",
                "category": "Files",
                "what": "Converts between Python dicts/lists and JSON text. The standard way to save and load data in Streamlit apps.",
                "code": 'import json\nimport os\n\nFILE = "sessions.json"\n\n# Load from file (safe — handles missing file)\ndef load_sessions():\n    if not os.path.exists(FILE):\n        return {}  # first run, nothing saved yet\n    with open(FILE, "r") as f:\n        return json.load(f)\n\n# Save to file\ndef save_sessions(all_sessions):\n    with open(FILE, "w") as f:\n        json.dump(all_sessions, f, indent=2)\n\n# Add a new entry for a user and save\ndef save_for_user(username, entry):\n    data = load_sessions()\n    if username not in data:\n        data[username] = []\n    data[username].append(entry)\n    save_sessions(data)\n\n# Delete an entry by index and save\ndef delete_session(username, index):\n    data = load_sessions()\n    data[username].pop(index)\n    save_sessions(data)',
                "gotcha": "json.dump() writes to a file. json.dumps() returns a string. json.load() reads a file. json.loads() parses a string. Easy to mix up.",
                "tip": "indent=2 makes the saved JSON file human-readable. This is the exact pattern used in the workout tracker.",
            },
            {
                "name": "datetime — date.today() and timedelta",
                "category": "Dates",
                "what": "Get today's date, do maths with dates (add/subtract days), and navigate calendars.",
                "code": 'from datetime import date, timedelta\n\ntoday = date.today()           # e.g. date(2026, 3, 24)\nprint(today)                   # 2026-03-24\n\n# Add or subtract days\nyesterday = today - timedelta(days=1)\nnext_week = today + timedelta(days=7)\n\n# Used in workout tracker for calendar navigation\ndisplayed = today + timedelta(days=st.session_state.day_offset)\n\n# Get the Monday of the current week\nmonday = today - timedelta(days=today.weekday())',
                "gotcha": None,
                "tip": "today.weekday() returns 0 for Monday, 6 for Sunday — useful for finding the start of the week.",
            },
            {
                "name": "datetime — strftime and strptime",
                "category": "Dates",
                "what": "strftime converts a date TO a string. strptime converts a string BACK to a date. These two are used constantly in the workout tracker.",
                "code": 'from datetime import datetime, date\n\n# date → string (strftime = "format time")\ntoday = date.today()\ndate_str = today.strftime("%Y-%m-%d")      # "2026-03-24"\nfriendly = today.strftime("%A %d %B %Y")  # "Tuesday 24 March 2026"\n\n# string → date (strptime = "parse time")\nraw = "2026-03-24"\nd = datetime.strptime(raw, "%Y-%m-%d").date()\n\n# Common format codes:\n# %Y = 4-digit year    %m = month number\n# %d = day number      %A = full weekday name\n# %B = full month name %H:%M = time e.g. 07:30',
                "gotcha": "strftime and strptime are easy to mix up. Think: strfTIME = TO string. strpTIME = parse FROM string.",
                "tip": "The format string must exactly match the date string you're parsing or you get a ValueError.",
            },
            {
                "name": "datetime — now() and combine()",
                "category": "Dates",
                "what": "Get the current date and time, or combine a date with a time into a single datetime for doing time maths.",
                "code": 'from datetime import datetime, date, time\n\n# Current date and time\nnow = datetime.now()\nprint(now.date())              # 2026-03-24\nprint(now.strftime("%H:%M"))  # "07:30"\n\n# Combine date + time to calculate duration\nbase = date(2000, 1, 1)  # dummy date, just needs to be the same\nstart = datetime.combine(base, time(7, 30))\nend   = datetime.combine(base, time(8, 15))\ndelta = end - start\nminutes = int(delta.total_seconds() // 60)  # 45',
                "gotcha": None,
                "tip": "The workout tracker uses a dummy base date (2000-01-01) when combining times — it just needs any consistent date to do the subtraction.",
            },
        ],
    },
    "Streamlit": {
        "categories": ["All", "Display", "Input", "Layout", "State", "Data & files"],
        "commands": [
            {
                "name": "st.set_page_config()",
                "category": "Display",
                "what": "Must be the very first Streamlit call in your file. Sets the browser tab title and page layout.",
                "code": 'st.set_page_config(\n    page_title="My App",   # browser tab text\n    page_icon="🏋️",        # emoji or path to .ico\n    layout="centered"      # or "wide"\n)',
                "gotcha": "If this isn't the FIRST st.* call, you get a StreamlitAPIException. Only imports and plain Python can come before it.",
                "tip": None,
            },
            {
                "name": "st.title() / st.header() / st.subheader()",
                "category": "Display",
                "what": "Three heading sizes. title is biggest (H1), header is medium (H2), subheader is smaller (H3).",
                "code": 'st.title("Family Workout Tracker")  # biggest\nst.header("This Week")              # medium\nst.subheader("Add a workout")       # smaller',
                "gotcha": None,
                "tip": None,
            },
            {
                "name": "st.write()",
                "category": "Display",
                "what": "The Swiss-army knife. Pass a string, number, dict, dataframe — it figures out how to show it.",
                "code": 'st.write("Hello world")\nst.write("Logging for:", username)      # joins with space\nst.write(f"You have **{n}** sessions")  # markdown works\nst.write("---")                         # draws a divider line',
                "gotcha": None,
                "tip": 'st.write("---") is the quickest way to draw a section divider.',
            },
            {
                "name": "st.markdown()",
                "category": "Display",
                "what": "Renders Markdown. Add unsafe_allow_html=True only when you need actual HTML tags.",
                "code": '# Basic markdown\nst.markdown("This week: **3 sessions**")\n\n# Centred text with custom colour\nst.markdown(\n    "<p style=\'text-align:center; color:#888;\'>Today</p>",\n    unsafe_allow_html=True\n)\n\n# Indented bullet points\nst.markdown("&nbsp;&nbsp;• Bench press — 80kg", unsafe_allow_html=True)',
                "gotcha": "Only use unsafe_allow_html=True with your own hardcoded HTML, never with user-typed text.",
                "tip": None,
            },
            {
                "name": "st.info() / st.success() / st.warning() / st.error()",
                "category": "Display",
                "what": "Coloured alert banners. Blue = info, green = success, orange = warning, red = error.",
                "code": 'st.info("Session duration: **45 mins**")\nst.success("Session saved!")\nst.warning("Start time doesn\'t look right")\nst.error("Could not load file")',
                "gotcha": None,
                "tip": None,
            },
            {
                "name": "st.caption()",
                "category": "Display",
                "what": "Small grey helper text, like a footnote. Good for hints below buttons or inputs.",
                "code": 'st.caption("Add at least one workout before saving.")',
                "gotcha": None,
                "tip": None,
            },
            {
                "name": "st.button()",
                "category": "Input",
                "what": "Renders a button. Returns True on the frame the user clicks it — always use inside an if statement.",
                "code": '# Basic button\nif st.button("New Session"):\n    do_something()\n\n# Full-width (good for mobile)\nif st.button("Save", use_container_width=True):\n    save()\n\n# Disabled button (greyed out, unclickable)\nif st.button("Save Session", disabled=not can_save):\n    save()\n\n# Unique key — REQUIRED in loops\nfor i, item in enumerate(items):\n    if st.button("Delete", key=f"del_{i}"):\n        items.pop(i)\n        st.rerun()',
                "gotcha": "You MUST wrap it in 'if'. Without that, clicking the button does nothing.",
                "tip": "Always give buttons a unique key= when you have more than one, especially inside loops. Without it Streamlit gets confused about which one was clicked.",
            },
            {
                "name": "key= parameter",
                "category": "Input",
                "what": "A unique ID you give to any input widget. Required when the same widget appears more than once — like buttons inside a loop.",
                "code": '# Without key — CRASHES if two buttons have same label\nfor session in sessions:\n    st.button("Delete")  # ERROR: duplicate widget\n\n# With key — each button is unique\nfor i, session in enumerate(sessions):\n    st.button("Delete", key=f"delete_{i}")\n\n# Also needed for inputs that appear on multiple pages\nst.text_input("Start time:", key="start_time_input")\nst.text_input("End time:",   key="end_time_input")',
                "gotcha": "If you get a DuplicateWidgetID error, you're missing a key= somewhere. Add a unique string or f-string with an index.",
                "tip": "Use f-strings to make keys unique in loops: key=f\"button_{i}\" where i is the loop index.",
            },
            {
                "name": "st.text_input()",
                "category": "Input",
                "what": "A single-line text box. Returns whatever string the user typed. value= sets the default.",
                "code": 'start = st.text_input(\n    "Start time (HH:MM):",  # label\n    value="07:30",          # default text\n    key="start_input"       # unique ID\n)\n\nif len(start) != 5:\n    st.warning("Use HH:MM format")',
                "gotcha": "Always returns a string — even if the user types a number. Use int() or float() to convert.",
                "tip": None,
            },
            {
                "name": "st.number_input()",
                "category": "Input",
                "what": "A numeric stepper with + / − buttons. Returns an int or float depending on your step= value.",
                "code": '# Integer\nreps = st.number_input(\n    "Number of reps:",\n    min_value=0,\n    step=1,\n    key="reps"\n)\n\n# Float (decimal steps)\nweight = st.number_input(\n    "Weight (kg):",\n    min_value=0.0,\n    step=2.5,\n    key="weight"\n)',
                "gotcha": None,
                "tip": "Use step=1 for whole numbers, step=0.5 or step=2.5 for decimals. The type of step= sets the return type.",
            },
            {
                "name": "st.selectbox()",
                "category": "Input",
                "what": "A dropdown. options must be a list. Returns whichever item is currently selected.",
                "code": 'workout_types = ["Running", "Cycling", "Weights"]\n\nchosen = st.selectbox(\n    "Select workout type:",  # label\n    workout_types,           # the list — required!\n    key="workout_select"\n)\n\nif chosen == "Running":\n    st.write("How far did you run?")',
                "gotcha": 'st.selectbox("hi") crashes — it needs the options list as the second argument.',
                "tip": "The returned value is one of the items from your list, so you can compare it with == directly.",
            },
            {
                "name": "st.radio()",
                "category": "Input",
                "what": "Radio buttons — user picks exactly one option from a visible list. Good for 2–4 choices.",
                "code": 'choice = st.radio(\n    "Did you use added weight?",\n    ["No weight", "With weight"],\n    key="weight_choice"\n)\n\nif choice == "With weight":\n    kg = st.number_input(\n        "How many kg?",\n        min_value=0.0,\n        step=2.5,\n        key="kg"\n    )',
                "gotcha": None,
                "tip": "For 5+ options, use selectbox instead — radio buttons get visually cluttered.",
            },
            {
                "name": "st.date_input()",
                "category": "Input",
                "what": "A date picker calendar. Returns a datetime.date object — not a string.",
                "code": 'from datetime import datetime\n\nchosen_date = st.date_input(\n    "Session date:",\n    value=datetime.now().date()  # pre-select today\n)\n\n# Convert to string for saving to JSON\ndate_str = chosen_date.strftime("%Y-%m-%d")',
                "gotcha": "Returns a date object, NOT a string. Use .strftime() to convert it to text.",
                "tip": None,
            },
            {
                "name": "st.columns()",
                "category": "Layout",
                "what": "Splits the page into side-by-side columns. Pass a count or a list of width ratios.",
                "code": '# Equal columns\ncol1, col2, col3 = st.columns(3)\nwith col1:\n    st.write("Left")\nwith col2:\n    st.write("Middle")\n\n# Unequal widths — [1,4,1] = narrow/wide/narrow\ncol_l, col_m, col_r = st.columns([1, 4, 1])\nwith col_l:\n    if st.button("◀", key="prev"):\n        st.session_state.day_offset -= 1\n        st.rerun()\nwith col_m:\n    st.markdown(\n        f"<p style=\'text-align:center\'>{today}</p>",\n        unsafe_allow_html=True\n    )\nwith col_r:\n    if st.button("▶", key="next"):\n        st.session_state.day_offset += 1\n        st.rerun()',
                "gotcha": None,
                "tip": "The numbers in the list are ratios, not pixels. [1, 4, 1] means narrow-wide-narrow.",
            },
            {
                "name": "st.container()",
                "category": "Layout",
                "what": "A grouping box. With border=True it draws a visible rounded rectangle around its contents.",
                "code": '# Invisible container — just groups things\nwith st.container():\n    st.write("Grouped content")\n\n# Visible bordered card\nwith st.container(border=True):\n    st.markdown("**Session 1** — 07:30 to 08:15")\n    st.write("• Bench press — 80kg — 3 sets")',
                "gotcha": None,
                "tip": "border=True is great for making session cards or any record-style display.",
            },
            {
                "name": "st.session_state",
                "category": "State",
                "what": "A dictionary that remembers values between reruns. Streamlit reruns your whole script on every interaction — this is how you keep data alive.",
                "code": '# Set defaults at the TOP of your file\nif "page" not in st.session_state:\n    st.session_state["page"] = "login"\n\nif "workouts" not in st.session_state:\n    st.session_state.workouts = []\n\n# Read anywhere\npage = st.session_state.page\n\n# Write anywhere — change triggers rerun\nif st.button("Go home"):\n    st.session_state.page = "home"\n    st.rerun()',
                "gotcha": "Always check 'if key not in st.session_state' before setting a default, or you reset it on every rerun.",
                "tip": "Dot notation (st.session_state.page) and dict notation (st.session_state['page']) do the same thing — pick one style and stick to it.",
            },
            {
                "name": "st.rerun()",
                "category": "State",
                "what": "Forces Streamlit to immediately rerun your script from the top. Use after changing session_state to make the UI update.",
                "code": 'if st.button("Log out"):\n    st.session_state.user = None\n    st.session_state.page = "login"\n    st.rerun()  # without this the page won\'t change\n\n# Also use after modifying a list\nif st.button("Delete", key=f"del_{i}"):\n    items.pop(i)\n    st.rerun()  # refresh so deleted item disappears',
                "gotcha": "st.rerun() stops execution immediately — any code after it does NOT run in that cycle.",
                "tip": None,
            },
            {
                "name": "Multi-page app with def",
                "category": "State",
                "what": "The standard pattern for building an app with multiple pages. Each page is a function. A router at the bottom decides which to call.",
                "code": '# 1. Define each page as a function\ndef show_login_page():\n    st.title("My App")\n    if st.button("Log in as Dad"):\n        st.session_state.user = "Dad"\n        st.session_state.page = "home"\n        st.rerun()\n\ndef show_home_page():\n    user = st.session_state.user\n    st.title(f"Welcome, {user}")\n    if st.button("Log out"):\n        st.session_state.user = None\n        st.session_state.page = "login"\n        st.rerun()\n\n# 2. Set defaults at the top of the file\nif "page" not in st.session_state:\n    st.session_state.page = "login"\nif "user" not in st.session_state:\n    st.session_state.user = None\n\n# 3. Router at the BOTTOM — decides which page to show\nif st.session_state.page == "login":\n    show_login_page()\nelif st.session_state.page == "home":\n    show_home_page()',
                "gotcha": "The router must be at the bottom of the file, after all the def blocks. Python reads top to bottom — calling show_login_page() before defining it gives a NameError.",
                "tip": "This is the exact structure of the Family Workout Tracker — login, home, log_session, and history are all separate def functions called from the router at the bottom.",
            },
            {
                "name": "json + open() for storage",
                "category": "Data & files",
                "what": "There's no built-in Streamlit file storage — you use plain Python file I/O with JSON. This is the full pattern from the workout tracker.",
                "code": 'import json, os\n\nFILE = "sessions.json"\n\ndef load_sessions():\n    if not os.path.exists(FILE):\n        return {}  # no file yet\n    with open(FILE, "r") as f:\n        return json.load(f)\n\ndef save_sessions(data):\n    with open(FILE, "w") as f:\n        json.dump(data, f, indent=2)\n\ndef save_for_user(username, entry):\n    data = load_sessions()\n    if username not in data:\n        data[username] = []\n    data[username].append(entry)\n    save_sessions(data)\n\ndef delete_for_user(username, index):\n    data = load_sessions()\n    data[username].pop(index)\n    save_sessions(data)',
                "gotcha": "On Streamlit Community Cloud the filesystem resets when the app sleeps. For permanent storage, use a database like Supabase.",
                "tip": None,
            },
            {
                "name": "st.secrets",
                "category": "Data & files",
                "what": "How you safely store API keys and passwords — never hardcode them in your script.",
                "code": '# In your app code\napi_key = st.secrets["MY_API_KEY"]\n\n# In .streamlit/secrets.toml (local)\n# MY_API_KEY = "sk-abc123"\n\n# On Streamlit Cloud:\n# Settings → Secrets → paste key=value pairs',
                "gotcha": "Never commit secrets.toml to GitHub. Add it to .gitignore.",
                "tip": None,
            },
        ],
    },
    "Patterns": {
        "categories": ["All", "Pages", "Data", "UI"],
        "commands": [
            {
                "name": "Multi-page app structure",
                "category": "Pages",
                "what": "The full skeleton of any multi-page Streamlit app. Copy this as a starting point for any new app.",
                "code": 'import streamlit as st\n\nst.set_page_config(page_title="My App")\n\n# ── Session state defaults ──\nif "page" not in st.session_state:\n    st.session_state.page = "login"\nif "user" not in st.session_state:\n    st.session_state.user = None\n\n# ── Page functions ──\ndef show_login_page():\n    st.title("My App")\n    if st.button("Enter as Dad"):\n        st.session_state.user = "Dad"\n        st.session_state.page = "home"\n        st.rerun()\n\ndef show_home_page():\n    st.title(f"Hello {st.session_state.user}")\n    if st.button("Go to history"):\n        st.session_state.page = "history"\n        st.rerun()\n    if st.button("Log out"):\n        st.session_state.page = "login"\n        st.rerun()\n\ndef show_history_page():\n    st.title("History")\n    if st.button("Back"):\n        st.session_state.page = "home"\n        st.rerun()\n\n# ── Router — always at the bottom ──\nif st.session_state.page == "login":\n    show_login_page()\nelif st.session_state.page == "home":\n    show_home_page()\nelif st.session_state.page == "history":\n    show_history_page()',
                "gotcha": "Always put the router at the very bottom. Define all your page functions before the router.",
                "tip": "Add a new page in 3 steps: 1) write the def function, 2) add an elif to the router, 3) add a button somewhere that sets session_state.page to its name.",
            },
            {
                "name": "Login / user selection screen",
                "category": "Pages",
                "what": "A simple login page where users pick their name from a list of buttons — exactly how the workout tracker works.",
                "code": 'accounts = ["Dad", "Mum", "Ozzie"]\n\ndef show_login_page():\n    st.title("Family App")\n    st.write("---")\n    st.subheader("Who are you?")\n\n    for account in accounts:\n        if st.button(account, use_container_width=True,\n                     key=f"login_{account}"):\n            st.session_state.user = account\n            st.session_state.page = "home"\n            st.rerun()\n\ndef show_home_page():\n    username = st.session_state.user\n    st.title(username)\n\n    if st.button("Log out"):\n        st.session_state.user = None\n        st.session_state.page = "login"\n        st.rerun()',
                "gotcha": "Give each login button a unique key using the account name: key=f\"login_{account}\". Without it you get a duplicate widget error.",
                "tip": None,
            },
            {
                "name": "Save and load JSON data",
                "category": "Data",
                "what": "The complete pattern for persisting data between sessions using a JSON file — the backbone of the workout tracker.",
                "code": 'import json, os\n\nFILE = "data.json"\n\ndef load():\n    if not os.path.exists(FILE):\n        return {}  # no file yet — return empty\n    with open(FILE, "r") as f:\n        return json.load(f)\n\ndef save(data):\n    with open(FILE, "w") as f:\n        json.dump(data, f, indent=2)\n\n# ── Add something ──\ndata = load()\nif "Dad" not in data:\n    data["Dad"] = []\ndata["Dad"].append({"date": "2026-03-24", "workout": "Run"})\nsave(data)\n\n# ── Read something ──\ndata = load()\ndad_sessions = data.get("Dad", [])\nst.write(f"Dad has {len(dad_sessions)} sessions")',
                "gotcha": "json.load() reads a file. json.loads() parses a string. json.dump() writes to a file. json.dumps() makes a string.",
                "tip": "Always call load() fresh each time you need the data — don't store it in a variable at the top of the file or it'll go stale between reruns.",
            },
            {
                "name": "Delete with confirm step",
                "category": "UI",
                "what": "A two-step delete: first click shows a confirmation, second click actually deletes. Prevents accidental deletions.",
                "code": '# Set default\nif "confirm_delete" not in st.session_state:\n    st.session_state.confirm_delete = None\n\n# In your list loop\nfor i, item in enumerate(items):\n    with st.container(border=True):\n        st.write(item["name"])\n\n        if st.session_state.confirm_delete == i:\n            # Confirmation state\n            st.warning("Are you sure?")\n            col1, col2 = st.columns(2)\n            with col1:\n                if st.button("Yes, delete", key=f"confirm_{i}"):\n                    items.pop(i)\n                    st.session_state.confirm_delete = None\n                    st.rerun()\n            with col2:\n                if st.button("Cancel", key=f"cancel_{i}"):\n                    st.session_state.confirm_delete = None\n                    st.rerun()\n        else:\n            if st.button("Delete", key=f"delete_{i}"):\n                st.session_state.confirm_delete = i\n                st.rerun()',
                "gotcha": "Store the index of the item being confirmed, not just True/False — otherwise you can't tell which item to delete.",
                "tip": "This is exactly how the workout tracker's history page works. confirm_delete_index in session_state holds whichever session is awaiting confirmation.",
            },
            {
                "name": "Day-by-day calendar navigation",
                "category": "UI",
                "what": "Back/forward buttons to browse through dates one day at a time — used for the personal and family calendars in the workout tracker.",
                "code": 'from datetime import date, timedelta\n\n# Default\nif "day_offset" not in st.session_state:\n    st.session_state.day_offset = 0\n\n# Calculate displayed date\ntoday = date.today()\ndisplayed = today + timedelta(days=st.session_state.day_offset)\ndate_str = displayed.strftime("%Y-%m-%d")\nfriendly = displayed.strftime("%A %d %B %Y")\nis_today = displayed == today\n\n# Navigation row\ncol_l, col_m, col_r = st.columns([1, 4, 1])\nwith col_l:\n    if st.button("◀", key="prev_day"):\n        st.session_state.day_offset -= 1\n        st.rerun()\nwith col_m:\n    label = f"Today — {friendly}" if is_today else friendly\n    st.markdown(\n        f"<p style=\'text-align:center; color:#888;\'>{label}</p>",\n        unsafe_allow_html=True\n    )\nwith col_r:\n    if st.button("▶", key="next_day"):\n        st.session_state.day_offset += 1\n        st.rerun()\n\n# Use date_str to look up data for that day\nsessions_today = by_date.get(date_str, [])',
                "gotcha": None,
                "tip": "Reset day_offset to 0 when navigating to a new page — otherwise users land on whatever date they were last browsing.",
            },
            {
                "name": "Draft list — build before saving",
                "category": "UI",
                "what": "Let users add multiple items to a temporary list, review them, remove any they don't want, then save the whole thing at once.",
                "code": '# Default\nif "draft_items" not in st.session_state:\n    st.session_state.draft_items = []\n\n# Show what\'s in the draft so far\nif st.session_state.draft_items:\n    st.subheader("Added so far:")\n    for i, item in enumerate(st.session_state.draft_items):\n        col_item, col_del = st.columns([5, 1])\n        with col_item:\n            st.write(f"{i+1}. {item}")\n        with col_del:\n            if st.button("X", key=f"remove_{i}"):\n                st.session_state.draft_items.pop(i)\n                st.rerun()\n\n# Add to draft\nnew_item = st.text_input("Add item:", key="new_item")\nif st.button("Add"):\n    if new_item:\n        st.session_state.draft_items.append(new_item)\n        st.rerun()\n\n# Save all at once\ncan_save = len(st.session_state.draft_items) > 0\nif st.button("Save all", disabled=not can_save):\n    save_to_file(st.session_state.draft_items)\n    st.session_state.draft_items = []  # clear draft\n    st.rerun()',
                "gotcha": None,
                "tip": "This is how the workout tracker's log session page works — draft_workouts builds up during the session, then gets saved all at once when you hit Save Session.",
            },
        ],
    },
}

# ─────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────

if "selected_language" not in st.session_state:
    st.session_state.selected_language = "Streamlit"
if "selected_category" not in st.session_state:
    st.session_state.selected_category = "All"
if "search_query" not in st.session_state:
    st.session_state.search_query = ""

# ─────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────

def get_commands(language, category, query):
    cmds = COMMANDS[language]["commands"]
    if category != "All":
        cmds = [c for c in cmds if c["category"] == category]
    if query:
        q = query.lower()
        cmds = [c for c in cmds if q in c["name"].lower() or q in c["what"].lower() or q in c["code"].lower()]
    return cmds


def render_command_card(cmd):
    with st.container(border=True):
        col_name, col_cat = st.columns([3, 1])
        with col_name:
            st.markdown(f"**`{cmd['name']}`**")
        with col_cat:
            st.caption(cmd["category"])

        st.write(cmd["what"])
        st.code(cmd["code"], language="python")

        if cmd.get("gotcha"):
            st.warning(f"**Watch out:** {cmd['gotcha']}")
        if cmd.get("tip"):
            st.success(f"**Tip:** {cmd['tip']}")


# ─────────────────────────────────────────
# PAGE
# ─────────────────────────────────────────

st.title("📖 Code Reference")
st.write("---")

# ── Language / section selector ──
languages = list(COMMANDS.keys())
lang_cols = st.columns(len(languages))
for i, lang in enumerate(languages):
    with lang_cols[i]:
        is_active = st.session_state.selected_language == lang
        label = f"**{lang}**" if is_active else lang
        if st.button(label, use_container_width=True, key=f"lang_{lang}"):
            st.session_state.selected_language = lang
            st.session_state.selected_category = "All"
            st.rerun()

st.write("")

language = st.session_state.selected_language
categories = COMMANDS[language]["categories"]

# ── Search ──
search = st.text_input(
    "🔍 Search commands...",
    value=st.session_state.search_query,
    key="search_input",
    placeholder="e.g. button, loop, file, date"
)
st.session_state.search_query = search

# ── Category filter ──
if not search:
    st.write("**Filter by category:**")
    cat_cols = st.columns(len(categories))
    for i, cat in enumerate(categories):
        with cat_cols[i]:
            is_active = st.session_state.selected_category == cat
            label = f"**{cat}**" if is_active else cat
            if st.button(label, use_container_width=True, key=f"cat_{cat}"):
                st.session_state.selected_category = cat
                st.rerun()

st.write("---")

# ── Results ──
category = "All" if search else st.session_state.selected_category
commands = get_commands(language, category, search)

if search:
    st.caption(f"{len(commands)} result(s) for \"{search}\"")
else:
    st.caption(f"{len(commands)} command(s) — {language} / {category}")

st.write("")

if not commands:
    st.info("No commands found. Try a different search or category.")
else:
    for cmd in commands:
        render_command_card(cmd)
