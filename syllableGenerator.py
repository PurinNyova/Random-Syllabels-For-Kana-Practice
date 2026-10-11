import tkinter as tk
from tkinter import ttk
import random as rndm
import sylData

#Colors and fonts
BG = "#f4f5f7"
CARD = "#ffffff"
ACCENT = "#d94f4f"
ACCENT_HOVER = "#c03e3e"
TEXT = "#22252a"
MUTED = "#6b7280"
FONT = "Segoe UI"

root = tk.Tk()
root.geometry("620x430")
root.minsize(520, 420)
root.title("Syllabel Generator")
root.configure(bg=BG)

#Styles
style = ttk.Style(root)
style.theme_use("clam")
style.configure(".", background=BG, foreground=TEXT, font=(FONT, 10))
style.configure("Card.TFrame", background=CARD)
style.configure("Header.TLabel", font=(FONT, 20, "bold"))
style.configure("Sub.TLabel", foreground=MUTED, font=(FONT, 10))
style.configure("Section.TLabel", background=CARD, foreground=MUTED, font=(FONT, 9, "bold"))
style.configure("Result.TLabel", background=CARD, font=(FONT, 18))
style.configure("Card.TCheckbutton", background=CARD, font=(FONT, 11), padding=(4, 6))
style.map("Card.TCheckbutton", background=[("active", CARD)], indicatorcolor=[("selected", ACCENT), ("!selected", CARD)])
style.configure("Link.TButton", background=CARD, foreground=ACCENT, borderwidth=0, padding=(6, 2), font=(FONT, 9, "underline"))
style.map("Link.TButton", background=[("active", CARD)], foreground=[("active", ACCENT_HOVER)])
style.configure("Accent.TButton", background=ACCENT, foreground="white", borderwidth=0, padding=(18, 8), font=(FONT, 11, "bold"))
style.map("Accent.TButton", background=[("active", ACCENT_HOVER)])
style.configure("TSpinbox", padding=(6, 4), arrowsize=14)

main = ttk.Frame(root, padding=20)
main.pack(fill="both", expand=True)

#Header
ttk.Label(main, text="Syllabel Generator", style="Header.TLabel").pack(anchor="w")
ttk.Label(main, text="Pick the kana rows you want to practice, then generate random syllables.", style="Sub.TLabel").pack(anchor="w", pady=(0, 14))

#Display for showing the result
display = tk.StringVar()
resultCard = ttk.Frame(main, style="Card.TFrame", padding=(16, 12))
resultCard.pack(fill="x")
resultHeader = ttk.Frame(resultCard, style="Card.TFrame")
resultHeader.pack(fill="x")
ttk.Label(resultHeader, text="RESULT", style="Section.TLabel").pack(side="left")
def copyResult():
    root.clipboard_clear()
    root.clipboard_append(display.get().strip())
ttk.Button(resultHeader, text="Copy", style="Link.TButton", command=copyResult, cursor="hand2").pack(side="right")
resultLabel = ttk.Label(resultCard, textvariable=display, style="Result.TLabel", anchor="center", justify="center")
resultLabel.pack(fill="x", pady=(6, 4))
resultCard.bind("<Configure>", lambda e: resultLabel.configure(wraplength=e.width - 40))
display.set("—")

#Making checkbutton and corresponding data point
check_buttons = [tk.IntVar() for _ in range(15)]
syllable_data = [sylData.first, sylData.kaiueo, sylData.saiueo, sylData.taiueo, sylData.naiueo,
                 sylData.haiueo, sylData.maiueo, sylData.yaiueo, sylData.raiueo, sylData.gaiueo,
                 sylData.zaiueo, sylData.daiueo, sylData.baiueo, sylData.paiueo, sylData.special]

#Configure inputContainer
groupCard = ttk.Frame(main, style="Card.TFrame", padding=(16, 12))
groupCard.pack(fill="x", pady=14)
groupHeader = ttk.Frame(groupCard, style="Card.TFrame")
groupHeader.pack(fill="x")
ttk.Label(groupHeader, text="SYLLABLE GROUPS", style="Section.TLabel").pack(side="left")
def setAll(value):
    for variable in check_buttons:
        variable.set(value)
ttk.Button(groupHeader, text="Clear", style="Link.TButton", command=lambda: setAll(0), cursor="hand2").pack(side="right")
ttk.Button(groupHeader, text="Select all", style="Link.TButton", command=lambda: setAll(1), cursor="hand2").pack(side="right")

inputContainer = ttk.Frame(groupCard, style="Card.TFrame")
for i in range(5):
    inputContainer.columnconfigure(i, weight=1, uniform="group")
inputContainer.pack(fill="x", pady=(6, 0))

#Buttons
Buttons = [("AIUEO", check_buttons[0], 0, 0),("K", check_buttons[1], 0, 1),("S", check_buttons[2], 0, 2), ("T", check_buttons[3], 0, 3), ("N",check_buttons[4], 0, 4),
           ("H", check_buttons[5], 1, 0), ("M", check_buttons[6], 1, 1),("Y", check_buttons[7], 1, 2),("R", check_buttons[8], 1, 3), ("G", check_buttons[9], 1, 4),
           ("Z", check_buttons[10], 2, 0), ("D", check_buttons[11], 2, 1), ("B", check_buttons[12], 2, 2), ("P", check_buttons[13], 2, 3), ("Special", check_buttons[14], 2, 4)]
for title, variable, row, column in Buttons:
    ttk.Checkbutton(inputContainer, text = title, variable = variable, onvalue=1, offvalue=0, style="Card.TCheckbutton", cursor="hand2").grid(row=row, column=column, sticky=tk.W+tk.E)

#Define Generate
def generateText():
    store = []
    for i, data in enumerate(syllable_data):
        if check_buttons[i].get() == 1:
            store.extend(data)
    store2 = ""
    i = 0
    while i <= entryContent.get():
        store2 += " " + store[rndm.randint(0, len(store)-1)]
        i += 1

    display.set(store2)

#Make Generate Section
generateContainer = ttk.Frame(main)
generateContainer.pack(fill="x")
def validate_input(P):
    # Check if P is a digit or an empty string
    return P.isdigit() or P == ""
entryContent = tk.IntVar()
ttk.Label(generateContainer, text="Amount:", font=(FONT, 11)).pack(side="left")
entry = ttk.Spinbox(generateContainer, from_=0, to=999, width=6, font=(FONT, 11), textvariable=entryContent, validate="key", validatecommand=(root.register(validate_input), "%P"))
entry.pack(side="left", padx=(8, 0))
ttk.Button(generateContainer, text = "Generate", style="Accent.TButton", command= generateText, cursor="hand2").pack(side="right")
root.bind("<Return>", lambda e: generateText())

root.mainloop()
