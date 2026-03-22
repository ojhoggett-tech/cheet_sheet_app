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
        "categories": ["All", "Strings", "Lists", "Dicts", "Files", "Functions", "Control flow"],
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
                "name": "if / elif / else",
                "category": "Control flow",
                "what": "Runs code only when a condition is True. elif and else are optional branches.",
                "code": 'age = 20\n\nif age < 18:\n    print("Minor")\nelif age < 65:\n    print("Adult")\nelse:\n    print("Senior")',
                "gotcha": "Python uses indentation (4 spaces) instead of brackets. Wrong indentation = error.",
                "tip": None,
            },
            {
                "name": "for loop",
                "category": "Control flow",
                "what": "Loops over every item in a list, string, or other iterable.",
                "code": 'workouts = ["Run", "Swim", "Lift"]\n\nfor w in workouts:\n    print(w)\n\n# Loop with index\nfor i, w in enumerate(workouts):\n    print(i, w)  # 0 Run, 1 Swim...',
                "gotcha": None,
                "tip": "enumerate() gives you the index AND the item at the same time — no need for a counter variable.",
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
                "name": "def (functions)",
                "category": "Functions",
                "what": "Defines a reusable block of code. Call it later by name. Use return to send a value back.",
                "code": 'def greet(name):\n    return f"Hello, {name}!"\n\nmessage = greet("Dad")\nprint(message)  # Hello, Dad!\n\n# Default argument\ndef greet(name="friend"):\n    return f"Hello, {name}!"',
                "gotcha": None,
                "tip": None,
            },
            {
                "name": "list [ ]",
                "category": "Lists",
                "what": "An ordered, changeable collection. Items are indexed from 0.",
                "code": 'fruits = ["apple", "banana", "cherry"]\n\nprint(fruits[0])   # apple (first)\nprint(fruits[-1])  # cherry (last)\n\nfruits.append("mango")   # add to end\nfruits.pop()             # remove last\nfruits.pop(0)            # remove by index',
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
                "name": "dict { }",
                "category": "Dicts",
                "what": "A key-value store. Look up values by key instead of by position.",
                "code": 'person = {\n    "name": "Dad",\n    "age": 40,\n    "active": True\n}\n\nprint(person["name"])       # Dad\nperson["age"] = 41          # update\nperson["city"] = "London"   # add new key',
                "gotcha": "Accessing a key that doesn't exist crashes with KeyError. Use .get() to avoid this.",
                "tip": 'person.get("city", "unknown") returns "unknown" instead of crashing if the key is missing.',
            },
            {
                "name": "dict methods",
                "category": "Dicts",
                "what": "Useful built-in methods for working with dictionaries.",
                "code": 'd = {"a": 1, "b": 2, "c": 3}\n\nd.keys()    # dict_keys(["a", "b", "c"])\nd.values()  # dict_values([1, 2, 3])\nd.items()   # pairs — good for loops\n\nfor key, value in d.items():\n    print(key, "->", value)\n\n"a" in d    # True — check if key exists',
                "gotcha": None,
                "tip": None,
            },
            {
                "name": "str methods",
                "category": "Strings",
                "what": "Strings have built-in methods for formatting, searching, and splitting.",
                "code": 's = "  Hello World  "\n\ns.strip()          # "Hello World" — trim spaces\ns.lower()          # "  hello world  "\ns.upper()          # "  HELLO WORLD  "\ns.replace("o","0") # "  Hell0 W0rld  "\ns.split(" ")       # split into list\n\n"world" in s.lower()  # True — contains check',
                "gotcha": "String methods return a NEW string — they don't change the original. You must assign the result.",
                "tip": None,
            },
            {
                "name": "f-strings",
                "category": "Strings",
                "what": "The modern way to embed variables inside strings. Prefix the string with f and put variables in {}.",
                "code": 'name = "Ozzie"\nage = 15\n\nprint(f"Name: {name}, Age: {age}")\n\n# Expressions work too\nprint(f"In 10 years: {age + 10}")\n\n# Format numbers\npi = 3.14159\nprint(f"Pi is {pi:.2f}")  # Pi is 3.14',
                "gotcha": None,
                "tip": ":.2f inside the braces rounds to 2 decimal places. :,  adds thousand separators.",
            },
            {
                "name": "open() / read / write files",
                "category": "Files",
                "what": "Read from or write to a file on disk. Always use with open() so the file closes automatically.",
                "code": '# Write to a file\nwith open("data.txt", "w") as f:\n    f.write("Hello\\n")\n\n# Read entire file\nwith open("data.txt", "r") as f:\n    content = f.read()\n\n# Read line by line\nwith open("data.txt", "r") as f:\n    for line in f:\n        print(line.strip())',
                "gotcha": '"w" overwrites the file completely. Use "a" to append without deleting existing content.',
                "tip": None,
            },
            {
                "name": "import json",
                "category": "Files",
                "what": "Converts between Python dicts/lists and JSON text. Essential for saving structured data to files.",
                "code": 'import json\n\ndata = {"name": "Dad", "sessions": 12}\n\n# Python → JSON string\ntext = json.dumps(data, indent=2)\n\n# Save to file\nwith open("data.json", "w") as f:\n    json.dump(data, f, indent=2)\n\n# Load from file\nwith open("data.json", "r") as f:\n    loaded = json.load(f)',
                "gotcha": "json.dump() writes to a file. json.dumps() returns a string. Easy to mix up.",
                "tip": "indent=2 makes the saved file human-readable. Leave it out for smaller files.",
            },
            {
                "name": "try / except",
                "category": "Control flow",
                "what": "Catches errors so your program doesn't crash. Put risky code in try, handle the error in except.",
                "code": 'try:\n    number = int("abc")  # this will fail\nexcept ValueError:\n    print("That wasn\'t a number")\n\n# Catch any error\ntry:\n    result = risky_function()\nexcept Exception as e:\n    print("Something went wrong:", e)',
                "gotcha": "Don't use bare except: — it catches everything including keyboard interrupts. Use except Exception as e: instead.",
                "tip": None,
            },
            {
                "name": "list comprehension",
                "category": "Lists",
                "what": "A compact way to build a new list by transforming or filtering another list.",
                "code": 'nums = [1, 2, 3, 4, 5]\n\n# Square every number\nsquares = [n * n for n in nums]\n# [1, 4, 9, 16, 25]\n\n# Filter — only even numbers\nevens = [n for n in nums if n % 2 == 0]\n# [2, 4]\n\n# Both — square only evens\n[n*n for n in nums if n % 2 == 0]',
                "gotcha": None,
                "tip": "Readable for simple cases. If the logic gets complex, use a regular for loop instead.",
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
                "code": 'st.write("Hello world")\nst.write("Logging for:", username)  # joins with space\nst.write(f"You have **{n}** sessions")  # markdown works\nst.write("---")  # draws a divider line',
                "gotcha": None,
                "tip": 'st.write("---") is the quickest way to draw a section divider.',
            },
            {
                "name": "st.markdown()",
                "category": "Display",
                "what": "Renders Markdown. Add unsafe_allow_html=True only when you need actual HTML tags.",
                "code": '# Basic markdown\nst.markdown("This week: **3 sessions**")\n\n# Custom HTML — needs the flag\nst.markdown(\n    "<p style=\'text-align:center; color:#888;\'>Today</p>",\n    unsafe_allow_html=True\n)',
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
                "code": '# Basic button\nif st.button("New Session"):\n    do_something()\n\n# Full-width (good for mobile)\nif st.button("Save", use_container_width=True):\n    save()\n\n# Disabled button\nif st.button("Save Session", disabled=not can_save):\n    save()',
                "gotcha": "You MUST wrap it in 'if'. Without that, clicking the button does nothing.",
                "tip": "Give every button a unique key= if you have multiple buttons, especially inside loops: st.button('Delete', key=f'del_{i}')",
            },
            {
                "name": "st.text_input()",
                "category": "Input",
                "what": "A single-line text box. Returns whatever string the user typed. value= sets the default.",
                "code": 'start = st.text_input(\n    "Start time (HH:MM):",  # label\n    value="07:30",          # default\n    key="start_input"       # unique ID\n)\n\nif len(start) != 5:\n    st.warning("Use HH:MM format")',
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
                "code": 'workout_types = ["Running", "Cycling", "Weights"]\n\nchosen = st.selectbox(\n    "Select workout type:",  # label\n    workout_types,           # the list\n    key="workout_select"\n)\n\nif chosen == "Running":\n    st.write("How far did you run?")',
                "gotcha": 'st.selectbox("hi") by itself crashes — it needs the options list as the second argument.',
                "tip": "The returned value is one of the items from your list, so you can compare it with == directly.",
            },
            {
                "name": "st.radio()",
                "category": "Input",
                "what": "Radio buttons — user picks exactly one option from a visible list. Good for 2–4 choices.",
                "code": 'choice = st.radio(\n    "Did you use added weight?",\n    ["No weight", "With weight"],\n    key="weight_choice"\n)\n\nif choice == "With weight":\n    kg = st.number_input("How many kg?", min_value=0.0, step=2.5, key="kg")',
                "gotcha": None,
                "tip": "For 5+ options, use selectbox instead — radio buttons get visually cluttered.",
            },
            {
                "name": "st.date_input()",
                "category": "Input",
                "what": "A date picker calendar. Returns a datetime.date object — not a string.",
                "code": 'from datetime import datetime\n\nchosen_date = st.date_input(\n    "Session date:",\n    value=datetime.now().date()  # pre-select today\n)\n\n# Convert to string for saving\ndate_str = chosen_date.strftime("%Y-%m-%d")',
                "gotcha": "Returns a date object, NOT a string. Use .strftime() to convert it to text.",
                "tip": None,
            },
            {
                "name": "st.columns()",
                "category": "Layout",
                "what": "Splits the page into side-by-side columns. Pass a count or a list of width ratios.",
                "code": '# Equal columns\ncol1, col2, col3 = st.columns(3)\nwith col1:\n    st.write("Left")\nwith col2:\n    st.write("Middle")\n\n# Unequal widths (ratios)\ncol_l, col_m, col_r = st.columns([1, 4, 1])\nwith col_l:\n    st.button("◀")\nwith col_m:\n    st.markdown("<p style=\'text-align:center\'>Today</p>",\n        unsafe_allow_html=True)',
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
                "code": '# Set defaults at the top of your file\nif "page" not in st.session_state:\n    st.session_state["page"] = "login"\n\nif "workouts" not in st.session_state:\n    st.session_state.workouts = []\n\n# Read anywhere\npage = st.session_state.page\n\n# Write anywhere\nif st.button("Go home"):\n    st.session_state.page = "home"\n    st.rerun()',
                "gotcha": "Always check 'if key not in st.session_state' before setting a default, or you reset it on every rerun.",
                "tip": None,
            },
            {
                "name": "st.rerun()",
                "category": "State",
                "what": "Forces Streamlit to immediately rerun your script from the top. Use after changing session_state to make the UI update.",
                "code": 'if st.button("Log out"):\n    st.session_state.user = None\n    st.session_state.page = "login"\n    st.rerun()  # without this the page won\'t change',
                "gotcha": "st.rerun() stops execution immediately — any code after it does NOT run in that cycle.",
                "tip": None,
            },
            {
                "name": "json + open() for storage",
                "category": "Data & files",
                "what": "There's no built-in Streamlit file storage — you use plain Python file I/O with JSON.",
                "code": 'import json, os\n\nFILE = "sessions.json"\n\ndef load():\n    if not os.path.exists(FILE):\n        return {}  # file not created yet\n    with open(FILE, "r") as f:\n        return json.load(f)\n\ndef save(data):\n    with open(FILE, "w") as f:\n        json.dump(data, f, indent=2)',
                "gotcha": "On Streamlit Community Cloud the filesystem resets when the app sleeps. For permanent storage, use Supabase or another database.",
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

# ── Language selector ──
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
search = st.text_input("🔍 Search commands...", value=st.session_state.search_query, key="search_input", placeholder="e.g. button, loop, file")
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

