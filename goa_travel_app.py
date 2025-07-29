import customtkinter as ctk
from tkinter import messagebox, filedialog
from tkcalendar import DateEntry
from datetime import datetime, timedelta
from fpdf import FPDF

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class GoaTravelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Goa Trip Planner")
        self.root.geometry("1400x900")
        self.root.resizable(True, True)

        self.trip_data = {}
        self.entries = {}
        self.language = "en"

        self.translations = {
            "en": {
            "title":           "Goa Trip Planner",
            "plan_trip":       "✈️ Plan Your Trip",
"contact":         "📞 Contact Information",
"disclaimer":      "⚠️ Disclaimer",
"language":        "🌐 Select Language",
"footer":          "Made with ❤️ for Travel Lovers",
"start_point":     "Starting Point",
"start_date":      "Start Date",
"days":            "Days to Stay",
"persons":         "Number of Persons",
"rooms":           "Number of Rooms",
"next":            "Next",
"back":            "⬅ Back",
"home":            "🏠 Home",
"contact_info": (
    "Call us    : +91 8309051581\n"
    "Mail us    : syedeshan099@gmail.com\n"
    "We’re available:Everyday 9 AM – 9 PM\n"
    "Visit us     :\n"
    " Near sivalayam temple,\n"
     " achempet road, Sattenapalli\n"
    "24x7 Helpdesk: +91 83090 727623\n"
),
"select_language": "Select Language",
            "lang_english":    "English",
            "lang_telugu":     "తెలుగు (Telugu)",
            "disclaimer_text": (
                "Destination: Goa (fixed)\n"
                "Note: Liquor is not allowed in the Bus  during travel as per government regulations.\n"
            ),
            "missing":         "Please fill in all the details.",
            "invalid_input":   "Please enter valid numeric values.",
            "download_pdf":    "Download PDF",
            "saved":           "Trip summary saved to",
            "summary_title":   "✈️ Goa Trip Summary ✈️\n\n",
            "est_total":       "Estimated Total: ₹"
            },
            "te": {
            "title":           "గోవా ట్రిప్ ప్లానర్",
            "plan_trip":       "✈️ మీ ప్రయాణాన్ని ప్లాన్ చేయండి",
            "contact":         "📞 సంప్రదింపు సమాచారం",
            "disclaimer":      "⚠️ డిస్క్లెయిమర్",
            "language":        "🌐 భాషను ఎంచుకోండి",
            "footer":          "ప్రేమికుల కోసం తయారు చేసిన ❤️",
            "start_point":     "ప్రారంభ స్థలం",
            "start_date":      "ప్రారంభ తేదీ",
            "days":            "ఉండే రోజులు",
            "persons":         "వ్యక్తుల సంఖ్య",
            "rooms":           "గదుల సంఖ్య",
            "next":            "తదుపరి",
            "back":            "⬅ వెనుకకు",
            "home":            "🏠 హోమ్",
            "contact_info":    "మమ్మల్ని సంప్రదించండి: +91 00000 00000",
            "select_language": "భాషను ఎంచుకోండి",
            "lang_english":    "ఇంగ్లీష్",
            "lang_telugu":     "తెలుగు (Telugu)",
            "disclaimer_text": (
                "గమ్యం: గోవా (స్థిరమైనది)\n"
                "ప్రారంభ స్థలం మరియు తేదీ వినియోగదారుడి ఎంపిక.\n"
                "స్థిర ఫీచర్లు: 2 PM చెక్-ఇన్, డబుల్ ఆక్యుపెన్సీ గది, "
                "రెండు బ్రేక్‌ఫాస్ట్‌లు + రెండు లంచ్‌లు లేదా డిన్నర్లు.\n"
                "గోవా నుండి తిరుగు: చెక్-ఇన్ తర్వాత 2 రోజులు. చెక్‌అవుట్ సమయం: ఉదయం 11 గంటలు."
            ),
            "missing":         "దయచేసి అన్ని వివరాలను నమోదు చేయండి.",
            "invalid_input":   "సరైన న్యూమరిక్ విలువలు ఇవ్వండి.",
            "download_pdf":    "PDF డౌన్‌లోడ్ చేయండి",
            "saved":           "ట్రిప్ సారాంశం దాచబడింది",
            "summary_title":   "✈️ గోవా ట్రిప్ సారాంశం ✈️\n\n",
            "est_total":       "అంచనా మొత్తం: ₹"
            }
        }

        self.show_main_menu()

    def t(self, key):
        return self.translations[self.language][key]

    def clear_root(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_main_menu(self):
        self.clear_root()

        frame = ctk.CTkFrame(self.root, corner_radius=15)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        title = ctk.CTkLabel(frame, text=self.t("title"), font=("Arial", 36, "bold"))
        title.pack(pady=(40, 50))

        buttons = [
            (self.t("plan_trip"), self.show_trip_planner),
            (self.t("contact"), self.show_contact_info),
            (self.t("disclaimer"), self.show_disclaimer),
            (self.t("language"), self.show_language_selection),
        ]

        for text, command in buttons:
            btn = ctk.CTkButton(frame, text=text, font=("Arial", 22), height=60, width=400, command=command)
            btn.pack(pady=12)

        footer = ctk.CTkLabel(frame, text=self.t("footer"), font=("Arial", 18, "italic"))
        footer.pack(side="bottom", pady=20)

    def show_contact_info(self):
        self.clear_root()
        frame = ctk.CTkFrame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        label = ctk.CTkLabel(frame, text=self.t("contact_info"), font=("Arial", 26))
        label.pack(pady=40)

        self.add_nav_buttons(frame)

    def show_disclaimer(self):
        self.clear_root()
        frame = ctk.CTkFrame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        label = ctk.CTkLabel(frame, text=self.t("disclaimer_text"), font=("Arial", 20), justify="left")
        label.pack(pady=40, padx=20)

        self.add_nav_buttons(frame)

    def show_language_selection(self):
        self.clear_root()
        frame = ctk.CTkFrame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        label = ctk.CTkLabel(frame, text=self.t("select_language"), font=("Arial", 26))
        label.pack(pady=40)

        lang_buttons = [
            (self.t("lang_english"), lambda: self.set_language("en")),
            (self.t("lang_telugu"), lambda: self.set_language("te"))
        ]

        for text, command in lang_buttons:
            btn = ctk.CTkButton(frame, text=text, font=("Arial", 20), command=command)
            btn.pack(pady=10)

        self.add_nav_buttons(frame)

    def set_language(self, lang):
        self.language = lang
        self.show_main_menu()

    def show_trip_planner(self):
        self.clear_root()
        frame = ctk.CTkFrame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        self.entries = {}
        labels = [
            (self.t("start_point"), "start_point"),
            (self.t("start_date"), "start_date"),
            (self.t("days"), "days"),
            (self.t("persons"), "persons"),
            (self.t("rooms"), "rooms")
        ]

        for idx, (text, key) in enumerate(labels):
            label = ctk.CTkLabel(frame, text=text, font=("Arial", 20))
            label.grid(row=idx, column=0, padx=20, pady=20, sticky="w")

            if key == "start_date":
                entry = DateEntry(frame, date_pattern='dd-mm-yyyy', font=("Arial", 16))
            else:
                entry = ctk.CTkEntry(frame, font=("Arial", 18))
                entry.bind("<KeyRelease>", lambda e: self.live_update())

            entry.grid(row=idx, column=1, padx=20, pady=20)
            self.entries[key] = entry

        self.live_label = ctk.CTkLabel(frame, text="", font=("Arial", 18), text_color="green")
        self.live_label.grid(row=len(labels), column=0, columnspan=2, pady=10)

        next_btn = ctk.CTkButton(frame, text=self.t("next"), font=("Arial", 20),
                                 command=self.validate_and_proceed)
        next_btn.grid(row=len(labels)+1, column=1, pady=30, sticky="e")

        back_btn = ctk.CTkButton(frame, text=self.t("back"), command=self.show_main_menu)
        back_btn.grid(row=len(labels)+1, column=0, pady=30, sticky="w")

    def validate_and_proceed(self):
        if self.save_trip_data():
            self.show_summary_page()

    def live_update(self):
        try:
            persons = int(self.entries['persons'].get())
            total = persons * 13500
            self.live_label.configure(text=f"{self.t('est_total')}{total}")
        except:
            self.live_label.configure(text="")

    def save_trip_data(self):
        try:
            missing = []
            for key, entry in self.entries.items():
                value = entry.get() if key != 'start_date' else entry.get_date()
                if key != 'start_date' and not value.strip():
                    entry.configure(border_color="red")
                    missing.append(key)
                elif key != 'start_date':
                    entry.configure(border_color="#979DA2")

            if missing:
                messagebox.showerror("Missing Fields", self.t("missing"))
                return False

            self.trip_data = {
                'start_point': self.entries['start_point'].get(),
                'start_date': self.entries['start_date'].get_date(),
                'days': int(self.entries['days'].get()),
                'persons': int(self.entries['persons'].get()),
                'rooms': int(self.entries['rooms'].get())
            }
            self.trip_data['return_date'] = self.trip_data['start_date'] + timedelta(days=self.trip_data['days'])
            self.trip_data['total_cost'] = self.trip_data['persons'] * 13500
            return True
        except:
            messagebox.showerror("Invalid Input", self.t("invalid_input"))
            return False

    def show_summary_page(self):
        self.clear_root()
        frame = ctk.CTkFrame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        summary = (
            f"{self.t('summary_title')}"
            f"{self.t('start_point')}: {self.trip_data['start_point']}\n"
            f"{self.t('start_date')}: {self.trip_data['start_date'].strftime('%d-%m-%Y')}\n"
            f"{self.t('days')}: {self.trip_data['days']}\n"
            f"{self.t('persons')}: {self.trip_data['persons']}\n"
            f"{self.t('rooms')}: {self.trip_data['rooms']}\n"
            f"💰 Price per Head: ₹13,500\n"
            f"💸 Total Price: ₹{self.trip_data['total_cost']}\n\n"
            f"🏨 Check-in: 2 PM | Double Room | 2 Breakfasts + 2 Meals\n"
            f"🚗 Return: {self.trip_data['return_date'].strftime('%d-%m-%Y')} | Checkout: 11 AM"
        )

        label = ctk.CTkLabel(frame, text=summary, font=("Arial", 18), justify="left")
        label.pack(pady=40)

        btn = ctk.CTkButton(frame, text=self.t("download_pdf"), command=self.download_summary_pdf)
        btn.pack(pady=10)

        self.add_nav_buttons(frame)

    def download_summary_pdf(self):
        from fpdf import FPDF
        import os

        filename = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Save PDF"
        )

        print(f"Selected filename: {filename}")  # DEBUG

        if not filename:
            messagebox.showwarning("Cancelled", "No file selected. PDF not saved.")
            return

        try:
            # Prepare PDF
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            # Safe, emoji-free summary
            summary = (
                f"{self.t('summary_title')}\n\n"
                f"{self.t('start_point')}: {self.trip_data.get('start_point', '')}\n"
                f"{self.t('start_date')}: {self.trip_data.get('start_date').strftime('%d-%m-%Y')}\n"
                f"{self.t('days')}: {self.trip_data.get('days')}\n"
                f"{self.t('persons')}: {self.trip_data.get('persons')}\n"
                f"{self.t('rooms')}: {self.trip_data.get('rooms')}\n"
                f"Price per Head: ₹13500\n"
                f"Total Price: ₹{self.trip_data.get('total_cost')}\n\n"
                f"Check-in: 2 PM | Double Room\n"
                f"Return: {self.trip_data.get('return_date').strftime('%d-%m-%Y')} | Checkout: 11 AM"
            )

            print("PDF content prepared.")  # DEBUG

            pdf.multi_cell(0, 10, summary)
            pdf.output(filename)

            print(f"PDF saved to: {filename}")  # DEBUG

            if os.path.exists(filename):
                messagebox.showinfo("Success", f"PDF saved at:\n{filename}")
            else:
                raise FileNotFoundError("PDF not created!")

        except Exception as e:
            print("PDF generation error:", e)
            messagebox.showerror("Error", f"Failed to save PDF.\n{e}")


    def add_nav_buttons(self, frame):
        back_btn = ctk.CTkButton(frame, text=self.t("back"), command=self.show_main_menu)
        back_btn.pack(side="left", padx=20, pady=20)

        home_btn = ctk.CTkButton(frame, text=self.t("home"), command=self.show_main_menu)
        home_btn.pack(side="right", padx=20, pady=20)

if __name__ == "__main__":
    root = ctk.CTk()
    app = GoaTravelApp(root)
    root.mainloop()