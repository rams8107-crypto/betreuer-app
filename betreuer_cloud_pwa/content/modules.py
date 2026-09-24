"""Lerninhalte GBB Lernen – Sachkunde nach BtRegV (Anlage zu § 3 Abs. 4).

Hinweis: Lernhilfe zur Wiederholung. Kein anerkannter Sachkundelehrgang.
"""

MODULES = [
    {
        "id": 1,
        "title": "Betreuerbestellung und Zusammenarbeit mit dem Betreuungsgericht",
        "hours": 15,
        "area": "Rechtliche Grundlagen",
        "summary": "Voraussetzungen der Bestellung, Einwilligungsvorbehalt und Pflichten gegenüber Gericht und betreuter Person.",
        "topics": [
            "Voraussetzungen der Betreuerbestellung (§§ 1814 ff. BGB)",
            "Einwilligungsvorbehalt: Voraussetzungen und Wirkung",
            "Aufgabenkreis und Erforderlichkeitsgrundsatz",
            "Berichtspflichten und Genehmigungsvorbehalte",
            "Zusammenarbeit mit Betreuungsgericht und Betreuungsbehörde",
        ],
        "cards": [
            {
                "q": "Wann darf eine Betreuung angeordnet werden?",
                "a": "Wenn ein volljähriger Mensch aufgrund von Krankheit oder Behinderung seine Angelegenheiten ganz oder teilweise nicht besorgen kann und keine milderen Mittel (z. B. Vorsorgevollmacht) ausreichen.",
            },
            {
                "q": "Was bewirkt ein Einwilligungsvorbehalt?",
                "a": "Für bestimmte Willenserklärungen der betreuten Person ist die Einwilligung des Betreuers erforderlich; ohne sie sind die Erklärungen in der Regel schwebend unwirksam.",
            },
            {
                "q": "Was bedeutet der Erforderlichkeitsgrundsatz?",
                "a": "Betreuung und Aufgabenkreis dürfen nur so weit gehen, wie nötig. Wo die Person selbst oder mit Unterstützung handeln kann, entfällt Betreuung.",
            },
        ],
        "quiz": [
            {
                "id": "1-1",
                "question": "Wofür steht der Erforderlichkeitsgrundsatz in der rechtlichen Betreuung?",
                "options": [
                    "Betreuung so umfassend wie möglich",
                    "Betreuung nur soweit nötig und so wenig eingreifend wie möglich",
                    "Immer Einwilligungsvorbehalt anordnen",
                    "Nur Vermögenssorge erlaubt",
                ],
                "correct": 1,
                "explain": "§ 1814 BGB / Betreuungsrecht: mildestes wirksames Mittel und begrenzter Aufgabenkreis.",
            },
            {
                "id": "1-2",
                "question": "Ein Einwilligungsvorbehalt bedeutet vor allem:",
                "options": [
                    "Der Betreuer entscheidet allein ohne Rücksicht auf Wünsche",
                    "Bestimmte Geschäfte der betreuten Person brauchen die Einwilligung des Betreuers",
                    "Das Gericht führt die Betreuung selbst",
                    "Die Betreuung endet automatisch nach einem Jahr",
                ],
                "correct": 1,
                "explain": "Schutz vor nachteiligen Rechtsgeschäften bei fehlender Geschäftsfähigkeit in Teilbereichen.",
            },
            {
                "id": "1-3",
                "question": "An wen richtet sich die Berichtspflicht des beruflichen Betreuers?",
                "options": [
                    "Nur an die Krankenkasse",
                    "An das Betreuungsgericht (und in der Praxis oft abgestimmt mit der Behörde)",
                    "Nur an Angehörige",
                    "Nur an den Vermieter",
                ],
                "correct": 1,
                "explain": "Das Gericht überwacht die Betreuung; Berichte und Rechnungslegung sind zentral.",
            },
            {
                "id": "1-4",
                "question": "Eine Vorsorgevollmacht ist gegenüber einer Betreuung in der Regel:",
                "options": [
                    "Immer unwirksam",
                    "Ein milderes Mittel, das eine Betreuung oft entbehrlich macht",
                    "Nur für Minderjährige gedacht",
                    "Nur für Sozialleistungen gültig",
                ],
                "correct": 1,
                "explain": "Bestehende wirksame Vorsorge kann Bestellung verhindern oder einschränken.",
            },
            {
                "id": "1-5",
                "question": "Wer registriert berufliche Betreuerinnen und Betreuer?",
                "options": [
                    "Das Finanzamt",
                    "Die Stammbehörde (Betreuungsbehörde)",
                    "Die Krankenkasse",
                    "Das Jobcenter allein",
                ],
                "correct": 1,
                "explain": "BtOG / BtRegV: Registrierung bei der zuständigen Betreuungsbehörde.",
            },
        ],
    },
    {
        "id": 2,
        "title": "Betreuungsführung",
        "hours": 30,
        "area": "Rechtliche Grundlagen",
        "summary": "Pflichten aus § 1821 BGB, Wunsch- und Wille-Orientierung, Vertretung und Grenzen der Entscheidungsbefugnis.",
        "topics": [
            "Wünsche, mutmaßlicher Wille und Wohl der betreuten Person",
            "Persönliche Betreuung und Kontakthäufigkeit",
            "Vertretungsmacht und Innenverhältnis",
            "Haftungsgrundlagen und Sorgfaltspflichten",
            "Dokumentation der Betreuungsführung",
        ],
        "cards": [
            {
                "q": "Wonach richtet sich die Betreuungsführung vorrangig?",
                "a": "Nach den Wünschen der betreuten Person; hilfsweise nach dem mutmaßlichen Willen. Das objektive „Wohl“ allein ersetzt nicht den Willen.",
            },
            {
                "q": "Was bedeutet persönliche Betreuung?",
                "a": "Der Betreuer muss die Betreuung grundsätzlich persönlich führen, Kontakt halten und darf Aufgaben nur begrenzt und verantwortbar übertragen.",
            },
        ],
        "quiz": [
            {
                "id": "2-1",
                "question": "Vorrang bei der Entscheidungsfindung hat:",
                "options": [
                    "Der Wille der Angehörigen",
                    "Der Wunsch bzw. mutmaßliche Wille der betreuten Person",
                    "Immer die kostengünstigste Lösung",
                    "Die Meinung der Nachbarn",
                ],
                "correct": 1,
                "explain": "§ 1821 BGB: Wunsch- und Wille-Orientierung steht im Zentrum.",
            },
            {
                "id": "2-2",
                "question": "Persönliche Betreuung bedeutet vor allem:",
                "options": [
                    "Alles an Dritte outsourcen",
                    "Regelmäßiger persönlicher Kontakt und eigene Verantwortung",
                    "Nur schriftliche Kommunikation",
                    "Nur einmal jährlich Besuch",
                ],
                "correct": 1,
                "explain": "Persönliche Wahrnehmung ist Kernpflicht beruflicher Betreuung.",
            },
            {
                "id": "2-3",
                "question": "Dokumentation in der Betreuung dient vor allem:",
                "options": [
                    "Nur der Werbung",
                    "Nachweisbarkeit, Qualität und gerichtlicher Kontrolle",
                    "Der Steuerhinterziehung",
                    "Dem Ersatz von Berichten",
                ],
                "correct": 1,
                "explain": "Nachvollziehbare Aktenführung schützt betreute Person und Betreuer.",
            },
            {
                "id": "2-4",
                "question": "Der Betreuer handelt im Außenverhältnis typischerweise als:",
                "options": [
                    "Zeuge",
                    "Gesetzlicher Vertreter im zugewiesenen Aufgabenkreis",
                    "Richter",
                    "Sozialarbeiter ohne Vertretungsmacht",
                ],
                "correct": 1,
                "explain": "Im Aufgabenkreis vertritt der Betreuer die betreute Person.",
            },
            {
                "id": "2-5",
                "question": "Widerspricht ein aktueller Wille einer alten Patientenverfügung, gilt in der Regel:",
                "options": [
                    "Immer nur die alte Verfügung",
                    "Der aktuelle, frei gebildete Wille hat Vorrang, soweit erkennbar",
                    "Nur Arztentscheidung zählt",
                    "Immer Gerichtsgutachten ohne Gespräch",
                ],
                "correct": 1,
                "explain": "Aktueller Wille und Auslegung der Verfügung sind sorgfältig zu prüfen.",
            },
        ],
    },
    {
        "id": 3,
        "title": "Recht der Unterbringung und der ärztlichen Zwangsmaßnahmen",
        "hours": 15,
        "area": "Rechtliche Grundlagen",
        "summary": "Freiheitsentzug, Fixierung, Zwangsbehandlung: Voraussetzungen, Verfahren und Aufgaben des Betreuers.",
        "topics": [
            "Freiheitsentziehende Unterbringung nach Betreuungsrecht",
            "Sonstige freiheitsentziehende Maßnahmen",
            "Ärztliche Zwangsmaßnahmen: Voraussetzungen",
            "Gerichtliche Genehmigung und Verfahren",
            "Aufgaben während des Vollzugs",
        ],
        "cards": [
            {
                "q": "Wann kommt eine freiheitsentziehende Unterbringung in Betracht?",
                "a": "Nur bei erheblicher Selbstgefährdung (oder in engen gesetzlichen Fällen) und wenn mildere Mittel nicht ausreichen; gerichtliche Genehmigung ist erforderlich.",
            },
            {
                "q": "Was gilt für ärztliche Zwangsmaßnahmen?",
                "a": "Hohe Hürden: u. a. Einwilligungsunfähigkeit, drohender erheblicher Gesundheitsschaden, Ultima Ratio, richterliche Genehmigung und begleitende Pflichten.",
            },
        ],
        "quiz": [
            {
                "id": "3-1",
                "question": "Freiheitsentziehende Unterbringung nach Betreuungsrecht bedarf in der Regel:",
                "options": [
                    "Nur einer ärztlichen Empfehlung",
                    "Gerichtlicher Genehmigung",
                    "Nur Zustimmung der Angehörigen",
                    "Nur Krankenkassenbewilligung",
                ],
                "correct": 1,
                "explain": "Richtervorbehalt schützt die Freiheit der Person.",
            },
            {
                "id": "3-2",
                "question": "Ärztliche Zwangsmaßnahmen sind:",
                "options": [
                    "Alltag in jeder Betreuung",
                    "Ultima Ratio mit strengen gesetzlichen Voraussetzungen",
                    "Immer ohne Genehmigung erlaubt",
                    "Nur Sache des Betreuers allein",
                ],
                "correct": 1,
                "explain": "Hohes Schutzgut: körperliche Unversehrtheit und Selbstbestimmung.",
            },
            {
                "id": "3-3",
                "question": "Eine Fixierung als freiheitsentziehende Maßnahme:",
                "options": [
                    "Braucht nie richterliche Kontrolle",
                    "Kann ebenfalls genehmigungspflichtig sein",
                    "Ist immer unzulässig",
                    "Ersetzt die Betreuung",
                ],
                "correct": 1,
                "explain": "Auch FEM unterliegen strengen Voraussetzungen und Verfahren.",
            },
            {
                "id": "3-4",
                "question": "Während einer Unterbringung soll der Betreuer vor allem:",
                "options": [
                    "Kontakt abbrechen",
                    "Interessen wahren, Milderungen prüfen und Verfahren begleiten",
                    "Nur Kosten prüfen",
                    "Die Klinik leiten",
                ],
                "correct": 1,
                "explain": "Begleitung, Kontrolle der Erforderlichkeit und Wille der Person bleiben zentral.",
            },
            {
                "id": "3-5",
                "question": "Mildere Mittel vor Unterbringung können sein:",
                "options": [
                    "Ambulante Hilfen, Krisenintervention, Wohnanpassung",
                    "Sofortige Dauerfixierung",
                    "Vertragsstrafe",
                    "Entzug des Wahlrechts",
                ],
                "correct": 0,
                "explain": "Erforderlichkeit verlangt Prüfung weniger eingreifender Alternativen.",
            },
        ],
    },
    {
        "id": 4,
        "title": "Personensorge 1",
        "hours": 15,
        "area": "Personensorge",
        "summary": "Krankheitsbilder, Behinderungen und Strategien zur Vermeidung von Freiheitsentzug.",
        "topics": [
            "Typische betreuungsrelevante Erkrankungen und Behinderungen",
            "Auswirkungen auf Alltag und Entscheidungsfähigkeit",
            "Behandlungsmöglichkeiten und Risiken",
            "Vermeidung von Unterbringung und Zwangsmaßnahmen",
            "Ressourcen- und Teilhabeorientierung",
        ],
        "cards": [
            {
                "q": "Warum sind Grundkenntnisse zu Erkrankungen wichtig?",
                "a": "Um Auswirkungen auf Willensbildung und Alltag zu verstehen, ohne zu pathologisieren – und um passende Hilfen statt Zwang zu finden.",
            },
        ],
        "quiz": [
            {
                "id": "4-1",
                "question": "Ziel von Personensorge-Kenntnissen ist vor allem:",
                "options": [
                    "Diagnosen stellen wie ein Arzt",
                    "Auswirkungen verstehen und passende Unterstützung finden",
                    "Medikamente verschreiben",
                    "Therapie ersetzen",
                ],
                "correct": 1,
                "explain": "Betreuer diagnostizieren nicht, brauchen aber Orientierungswissen.",
            },
            {
                "id": "4-2",
                "question": "Vermeidung von Freiheitsentzug gelingt oft durch:",
                "options": [
                    "Frühe Krisenplanung, Netzwerke, ambulante Hilfen",
                    "Sofortige Zwangsmedikation",
                    "Kontaktverbot zu allen Helfern",
                    "Ignorieren von Warnzeichen",
                ],
                "correct": 0,
                "explain": "Prävention und milde Mittel stehen vor Zwang.",
            },
            {
                "id": "4-3",
                "question": "Eine Demenz kann Entscheidungsfähigkeit:",
                "options": [
                    "Immer vollständig aufheben",
                    "Bereichsweise und zeitweise beeinträchtigen",
                    "Nie betreuungsrelevant sein",
                    "Nur das Mietrecht betreffen",
                ],
                "correct": 1,
                "explain": "Einwilligungsfähigkeit ist situativ und bereichsspezifisch zu prüfen.",
            },
            {
                "id": "4-4",
                "question": "Behinderung im Sinne der UN-BRK betont:",
                "options": [
                    "Nur Defizite",
                    "Teilhabe und Wechselwirkung mit Barrieren",
                    "Ausschluss aus der Gesellschaft",
                    "Nur medizinische Heilung",
                ],
                "correct": 1,
                "explain": "Menschenrechts- und Teilhabeperspektive prägen moderne Betreuung.",
            },
            {
                "id": "4-5",
                "question": "Bei Suchtproblemen ist oft zentral:",
                "options": [
                    "Nur Bestrafung",
                    "Zugang zu Behandlung, Wohnstabilität und unterstützter Entscheidung",
                    "Sofortige Entmündigung ohne Gespräch",
                    "Kontosperre ohne Aufgabenkreis",
                ],
                "correct": 1,
                "explain": "Hilfen und Wille der Person stehen im Vordergrund.",
            },
        ],
    },
    {
        "id": 5,
        "title": "Personensorge 2",
        "hours": 15,
        "area": "Personensorge",
        "summary": "Behandlungsvertrag, Einwilligungsfähigkeit, Patientenrechte, Wohnraum und Aufenthalt.",
        "topics": [
            "Behandlungsvertragsrecht und Patientenrechte",
            "Einwilligungsfähigkeit",
            "Patientenverfügung und Behandlungswünsche",
            "Gefährliche Maßnahmen und Genehmigungen",
            "Wohnraumaufgabe, Umgang und Aufenthalt",
        ],
        "cards": [
            {
                "q": "Was ist Einwilligungsfähigkeit?",
                "a": "Die Fähigkeit, Wesen, Bedeutung und Tragweite einer konkreten Maßnahme zu verstehen und einen Willen danach zu bilden – situationsbezogen.",
            },
            {
                "q": "Was gilt für die Aufgabe der Wohnung?",
                "a": "Oft genehmigungspflichtig und besonders eingreifend; Wille, Alternativen und soziale Bezüge sind sorgfältig zu prüfen.",
            },
        ],
        "quiz": [
            {
                "id": "5-1",
                "question": "Einwilligungsfähigkeit bezieht sich auf:",
                "options": [
                    "Eine pauschale Lebensentscheidung für immer",
                    "Die konkrete Maßnahme und Situation",
                    "Nur das Alter",
                    "Nur das Vermögen",
                ],
                "correct": 1,
                "explain": "Sie ist nicht global „vorhanden/nicht vorhanden“.",
            },
            {
                "id": "5-2",
                "question": "Eine Patientenverfügung:",
                "options": [
                    "Ist immer unverbindlich",
                    "Kann für konkrete Behandlungssituationen verbindlich sein",
                    "Ersetzt jede Betreuung",
                    "Gilt nur für Minderjährige",
                ],
                "correct": 1,
                "explain": "Bei Passung der Situation ist sie bindend auszulegen und umzusetzen.",
            },
            {
                "id": "5-3",
                "question": "Aufgabe von Wohnraum durch den Betreuer:",
                "options": [
                    "Ist immer formlos möglich",
                    "Ist oft genehmigungspflichtig und besonders eingreifend",
                    "Braucht nie den Willen der Person",
                    "Ist Sache der Polizei",
                ],
                "correct": 1,
                "explain": "Wohnung ist zentrales Lebensgut; Verfahren und Wille beachten.",
            },
            {
                "id": "5-4",
                "question": "Patientenrechte umfassen unter anderem:",
                "options": [
                    "Aufklärung, Einwilligung, Einsicht in Unterlagen",
                    "Nur Kostenübernahme",
                    "Nur Klinikhausordnung",
                    "Verzicht auf Information",
                ],
                "correct": 0,
                "explain": "Selbstbestimmung und Informationsrechte sind zentral.",
            },
            {
                "id": "5-5",
                "question": "Bei gefährlichen ärztlichen Maßnahmen braucht es oft:",
                "options": [
                    "Nur Nachbarzustimmung",
                    "Sorgfältige Prüfung und ggf. gerichtliche Genehmigung",
                    "Gar keine Prüfung",
                    "Nur Online-Formular ohne Arzt",
                ],
                "correct": 1,
                "explain": "Je höher das Risiko, desto strenger Verfahren und Dokumentation.",
            },
        ],
    },
    {
        "id": 6,
        "title": "Vermögenssorge 1",
        "hours": 15,
        "area": "Vermögenssorge",
        "summary": "Geschäftsfähigkeit, Stellvertretung, Schuldrecht, Haftung, Zwangsvollstreckung und Insolvenzgrundlagen.",
        "topics": [
            "Geschäftsfähigkeit und Willenserklärungen",
            "Recht der Stellvertretung",
            "Schuldrecht und Haftungsfragen",
            "Zwangsvollstreckung im Überblick",
            "Insolvenzverfahren – Grundkenntnisse",
        ],
        "cards": [
            {
                "q": "Was muss der Betreuer bei Verträgen prüfen?",
                "a": "Ob die betreute Person selbst wirksam handeln kann, ob Vertretung nötig ist und ob Genehmigungen oder Einwilligungsvorbehalt greifen.",
            },
        ],
        "quiz": [
            {
                "id": "6-1",
                "question": "Geschäftsunfähigkeit bedeutet grob:",
                "options": [
                    "Man darf wählen, aber nicht mieten",
                    "Willenserklärungen sind in der Regel nichtig",
                    "Man ist automatisch betreut",
                    "Nur Ausländer sind betroffen",
                ],
                "correct": 1,
                "explain": "§§ 104 ff. BGB – mit wichtigen Ausnahmen und Nuancen.",
            },
            {
                "id": "6-2",
                "question": "Stellvertretung durch den Betreuer wirkt:",
                "options": [
                    "Nur intern ohne Außenwirkung",
                    "Im Außenverhältnis für die betreute Person im Aufgabenkreis",
                    "Nur gegenüber dem Gericht",
                    "Nie bei Mietverträgen",
                ],
                "correct": 1,
                "explain": "Vertretungsmacht folgt dem Aufgabenkreis.",
            },
            {
                "id": "6-3",
                "question": "Bei drohender Zahlungsunfähigkeit sollte der Betreuer:",
                "options": [
                    "Schulden ignorieren",
                    "Überblick schaffen, Fristen wahren und geeignete Verfahren prüfen",
                    "Sofort alles bar abheben ohne Dokumentation",
                    "Nur das Gericht anrufen ohne Zahlen",
                ],
                "correct": 1,
                "explain": "Vermögenssorge verlangt aktive Sicherung und Ordnung der Finanzen.",
            },
            {
                "id": "6-4",
                "question": "Haftungsrisiken entstehen besonders bei:",
                "options": [
                    "Sorgfältiger Dokumentation",
                    "Pflichtverletzung und fehlender Sorgfalt",
                    "Regelmäßigen Berichten",
                    "Wunschermittlung",
                ],
                "correct": 1,
                "explain": "Sorgfaltspflichten und Grenzen der Vertretung beachten.",
            },
            {
                "id": "6-5",
                "question": "Zwangsvollstreckung betrifft oft:",
                "options": [
                    "Nur Strafrecht",
                    "Durchsetzung von Geldforderungen in Vermögen/Einkommen",
                    "Nur Sozialhilfe",
                    "Nur Erbschaftsteuer",
                ],
                "correct": 1,
                "explain": "Pfändungsschutz und Verfahrenskenntnisse sind praxisrelevant.",
            },
        ],
    },
    {
        "id": 7,
        "title": "Vermögenssorge 2",
        "hours": 15,
        "area": "Vermögenssorge",
        "summary": "Vermögensverzeichnis, Rechnungslegung, Genehmigungen, Miet-/Heimrecht sowie Erb- und Familienrecht.",
        "topics": [
            "Vermögensverzeichnis und Rechnungslegung",
            "Genehmigungsvorbehalte bei Vermögensgeschäften",
            "Miet- und Heimrecht in der Betreuung",
            "Erb- und familienrechtliche Bezüge",
            "Geldanlage und Verfügungen über Vermögen",
        ],
        "cards": [
            {
                "q": "Wozu dient das Vermögensverzeichnis?",
                "a": "Zur Transparenz gegenüber dem Gericht: Ausgangslage des Vermögens zu Beginn der Betreuung.",
            },
            {
                "q": "Was ist bei Heimverträgen wichtig?",
                "a": "Verbraucherschutz, Leistungen, Kosten, Kündigung und das Zusammenspiel mit Sozialleistungen und Wunsch der Person.",
            },
        ],
        "quiz": [
            {
                "id": "7-1",
                "question": "Das Vermögensverzeichnis wird typischerweise erstellt:",
                "options": [
                    "Am Ende der Betreuung ohne Anlass",
                    "Zu Beginn der Vermögenssorge für das Gericht",
                    "Nur bei Umzug",
                    "Nur auf Wunsch der Bank",
                ],
                "correct": 1,
                "explain": "Ausgangsbestand macht spätere Kontrolle möglich.",
            },
            {
                "id": "7-2",
                "question": "Rechnungslegung dient:",
                "options": [
                    "Der gerichtlichen Kontrolle der Vermögensverwaltung",
                    "Nur interner Buchhaltung ohne Pflicht",
                    "Der Steuerberatung der Nachbarn",
                    "Dem Ersatz der Betreuung",
                ],
                "correct": 0,
                "explain": "Einnahmen/Ausgaben nachvollziehbar belegen.",
            },
            {
                "id": "7-3",
                "question": "Viele riskante Vermögensgeschäfte sind:",
                "options": [
                    "Immer frei",
                    "Genehmigungspflichtig durch das Betreuungsgericht",
                    "Nur notariell ohne Gericht",
                    "Verboten ohne Ausnahme",
                ],
                "correct": 1,
                "explain": "Schutz vor Vermögensschäden durch Vorbehalt.",
            },
            {
                "id": "7-4",
                "question": "Im Mietrecht der betreuten Person ist oft zentral:",
                "options": [
                    "Erhalt der Wohnung und Prüfung von Kündigungen",
                    "Sofortige Kündigung ohne Gespräch",
                    "Nur Schönheitsreparaturen",
                    "Nur Kaution der Nachbarn",
                ],
                "correct": 0,
                "explain": "Wohnraumschutz und soziale Bezüge haben hohen Stellenwert.",
            },
            {
                "id": "7-5",
                "question": "Erbschaftsangelegenheiten in der Betreuung:",
                "options": [
                    "Sind nie relevant",
                    "Können Annahme/Ausschlagung und Genehmigungen betreffen",
                    "Erledigt immer das Finanzamt allein",
                    "Brauchen keine Fristenkenntnis",
                ],
                "correct": 1,
                "explain": "Fristen und Vermögensfolgen sorgfältig prüfen.",
            },
        ],
    },
    {
        "id": 8,
        "title": "Sozialrecht 1: Kenntnisse des Sozialrechts",
        "hours": 30,
        "area": "Sozialrecht",
        "summary": "Leistungen zur Existenzsicherung, Kranken-/Renten-/Pflegeversicherung und Durchsetzung von Ansprüchen.",
        "topics": [
            "SGB II und SGB XII: Lebensunterhalt und KdU",
            "Leistungen nach SGB V, VI und XI",
            "Mitwirkungspflichten",
            "Ermittlung und Durchsetzung von Ansprüchen",
            "Widerspruch und Klage im Sozialrecht",
        ],
        "cards": [
            {
                "q": "Unterschied SGB II / SGB XII?",
                "a": "SGB II (Bürgergeld) für erwerbsfähige Leistungsberechtigte; SGB XII u. a. Hilfe zum Lebensunterhalt / Grundsicherung bei Erwerbsminderung bzw. Alter.",
            },
            {
                "q": "Was sind Mitwirkungspflichten?",
                "a": "Pflichten, an der Aufklärung mitzuwirken (Angaben, Nachweise). Verletzung kann Leistungskürzung drohen – Aufklärung und Begleitung sind wichtig.",
            },
        ],
        "quiz": [
            {
                "id": "8-1",
                "question": "SGB II regelt vor allem:",
                "options": [
                    "Bürgergeld für erwerbsfähige Leistungsberechtigte",
                    "Nur Pflegeheimkosten",
                    "Nur Kindergeld",
                    "Nur Beamtenversorgung",
                ],
                "correct": 0,
                "explain": "Zentrale Existenzsicherungsnorm für erwerbsfähige Personen.",
            },
            {
                "id": "8-2",
                "question": "SGB XII ist u. a. relevant bei:",
                "options": [
                    "Nur Arbeitslosengeld I",
                    "Grundsicherung im Alter und bei Erwerbsminderung / Hilfe zum Lebensunterhalt",
                    "Nur Kfz-Steuer",
                    "Nur Elterngeld",
                ],
                "correct": 1,
                "explain": "Häufig in Betreuungen mit längerfristiger Erwerbsminderung.",
            },
            {
                "id": "8-3",
                "question": "SGB XI betrifft:",
                "options": [
                    "Pflegeversicherung",
                    "Nur Rentenversicherung",
                    "Nur Unfallversicherung",
                    "Nur Asylbewerberleistungen",
                ],
                "correct": 0,
                "explain": "Pflegegrade, Sach- und Geldleistungen.",
            },
            {
                "id": "8-4",
                "question": "Bei Ablehnung eines Sozialantrags hilft oft zuerst:",
                "options": [
                    "Widerspruch innerhalb der Frist",
                    "Sofort Bundesverfassungsgericht",
                    "Nur Facebook-Post",
                    "Ignorieren der Frist",
                ],
                "correct": 0,
                "explain": "Fristenwahrung ist entscheidend; danach ggf. Klage.",
            },
            {
                "id": "8-5",
                "question": "Kosten der Unterkunft (KdU) sind typischerweise:",
                "options": [
                    "Teil der Existenzsicherung nach SGB II/XII",
                    "Immer Privatsache ohne Leistung",
                    "Nur BAföG",
                    "Nur Kindergeld",
                ],
                "correct": 0,
                "explain": "Angemessenheit und Nachweise sind praxisrelevant.",
            },
        ],
    },
    {
        "id": 9,
        "title": "Sozialrecht 2: Sozial- und Hilfestrukturen in der Praxis",
        "hours": 45,
        "area": "Sozialrecht",
        "summary": "Teilhabe (SGB IX), Pflege im Leistungskombi und Netzwerkarbeit vor Ort.",
        "topics": [
            "Rehabilitation und Teilhabe (SGB IX)",
            "Eingliederungshilfe und Leistungsformen",
            "Pflegeleistungen in Kombination mit anderen Leistungen",
            "Fallbezogene Erschließung von Hilfen",
            "Netzwerke, Beratungsstellen, Träger",
        ],
        "cards": [
            {
                "q": "Was ist Eingliederungshilfe?",
                "a": "Leistungen zur Teilhabe für Menschen mit Behinderung (u. a. soziale Teilhabe, Bildung, Arbeit) – Träger und Verfahren nach SGB IX kennen.",
            },
            {
                "q": "Warum Netzwerke?",
                "a": "Betreuung wirkt über Anspruchserschließung: wer hilft wofür vor Ort (Pflege, Teilhabe, Schuldnerberatung, Wohnen).",
            },
        ],
        "quiz": [
            {
                "id": "9-1",
                "question": "SGB IX steht zentral für:",
                "options": [
                    "Rehabilitation und Teilhabe von Menschen mit Behinderungen",
                    "Nur Strafvollzug",
                    "Nur Steuerrecht",
                    "Nur Beamtenrecht",
                ],
                "correct": 0,
                "explain": "Teilhabeleistungen und Verfahren der Rehabilitationsträger.",
            },
            {
                "id": "9-2",
                "question": "Eingliederungshilfe kann umfassen:",
                "options": [
                    "Teilhabe am Arbeitsleben, Bildung, soziale Teilhabe",
                    "Nur Bußgelder",
                    "Nur Kfz-Zulassung",
                    "Nur Erbrecht",
                ],
                "correct": 0,
                "explain": "Leistungsformen sind vielfältig und einzelfallbezogen.",
            },
            {
                "id": "9-3",
                "question": "Pflege und Eingliederungshilfe:",
                "options": [
                    "Schließen sich immer aus",
                    "Können zusammentreffen und müssen abgegrenzt/kombiniert werden",
                    "Sind identisch",
                    "Betrifft nur Kinder",
                ],
                "correct": 1,
                "explain": "Schnittstellenkenntnis ist prüfungs- und praxisrelevant.",
            },
            {
                "id": "9-4",
                "question": "Fallbezogene Erschließung von Hilfen heißt:",
                "options": [
                    "Bedarf klären und passende Träger/Leistungen finden",
                    "Immer denselben Standardbrief senden",
                    "Nur Google ohne Antrag",
                    "Nur Gericht anrufen",
                ],
                "correct": 0,
                "explain": "Methodisches Vorgehen statt Zufall.",
            },
            {
                "id": "9-5",
                "question": "Ein gutes regionales Netzwerk enthält oft:",
                "options": [
                    "Betreuungsverein, Pflegestützpunkt, Sozialpsychiatrie, Schuldnerberatung",
                    "Nur Fitnessstudios",
                    "Nur Autohäuser",
                    "Nur Auslandsbanken",
                ],
                "correct": 0,
                "explain": "Praxiswissen über Akteure vor Ort.",
            },
        ],
    },
    {
        "id": 10,
        "title": "Grundlagen der Kommunikation und Praxistransfer",
        "hours": 30,
        "area": "Kommunikation",
        "summary": "Kommunikationsmodelle, Haltung, Diversität, Konflikte und Selbstreflexion.",
        "topics": [
            "Theoretische Konzepte und Methoden",
            "Grundhaltungen und Gesprächstechniken",
            "Diversitätssensible Kommunikation",
            "Ressourcenorientierung",
            "Konfliktmanagement und Machtreflexion",
        ],
        "cards": [
            {
                "q": "Welche Haltung ist zentral?",
                "a": "Respekt, Empathie, Klarheit und Verzicht auf Bevormundung – bei gleichzeitiger Verantwortung im Aufgabenkreis.",
            },
        ],
        "quiz": [
            {
                "id": "10-1",
                "question": "Ressourcenorientierte Kommunikation betont:",
                "options": [
                    "Nur Defizite",
                    "Stärken, Fähigkeiten und vorhandene Netze",
                    "Nur Diagnosen",
                    "Nur Gerichtssprache",
                ],
                "correct": 1,
                "explain": "Anschlussfähig für unterstützte Entscheidungsfindung.",
            },
            {
                "id": "10-2",
                "question": "Diversitätssensible Kommunikation heißt u. a.:",
                "options": [
                    "Sprache, Kultur, Beeinträchtigung und Biografie beachten",
                    "Alle gleich behandeln ohne Anpassung",
                    "Nur Hochdeutsch ohne Hilfsmittel",
                    "Nur schriftlich kommunizieren",
                ],
                "correct": 0,
                "explain": "Zugänglichkeit und Respekt vor Unterschieden.",
            },
            {
                "id": "10-3",
                "question": "Machtreflexion in der Betreuung ist wichtig, weil:",
                "options": [
                    "Betreuer strukturell Macht haben und sie kontrollieren müssen",
                    "Es keine Machtasymmetrie gibt",
                    "Nur Gerichte Macht haben",
                    "Macht irrelevant ist",
                ],
                "correct": 0,
                "explain": "Bewusste Begrenzung von Bevormundung.",
            },
            {
                "id": "10-4",
                "question": "Im Konflikt hilft oft:",
                "options": [
                    "Aktives Zuhören, Klärung von Interessen, klare Grenzen",
                    "Sofortiger Abbruch ohne Gespräch",
                    "Nur Drohungen",
                    "Ignorieren aller Emotionen",
                ],
                "correct": 0,
                "explain": "Konfliktfähigkeit ist Kernkompetenz.",
            },
            {
                "id": "10-5",
                "question": "Praxistransfer bedeutet:",
                "options": [
                    "Theorie in konkrete Gesprächs- und Fallarbeit übersetzen",
                    "Nur auswendig lernen",
                    "Nur Paragraphen zitieren",
                    "Theorie vermeiden",
                ],
                "correct": 0,
                "explain": "Module 10/11 sind übungsstark angelegt.",
            },
        ],
    },
    {
        "id": 11,
        "title": "Betreuungsspezifische Kommunikation / Unterstützte Entscheidungsfindung",
        "hours": 45,
        "area": "Kommunikation",
        "summary": "Unterstützte Entscheidungsfindung, Willenserkundung und Methoden der Begleitung.",
        "topics": [
            "Unterstützte Entscheidungsfindung statt Ersatzentscheidung",
            "Erkennen von Wünschen und Präferenzen",
            "Methoden der Unterstützung bei Entscheidungen",
            "Umgang mit Uneinigkeit und Risikolagen",
            "Dokumentation von Willensermittlung",
        ],
        "cards": [
            {
                "q": "Was ist unterstützte Entscheidungsfindung?",
                "a": "Die Person soll möglichst selbst entscheiden; der Betreuer hilft beim Verstehen und Abwägen, statt vorschnell zu ersetzen.",
            },
            {
                "q": "Wann Ersatzentscheidung?",
                "a": "Nur wenn trotz Unterstützung keine eigene Entscheidung möglich ist – dann am mutmaßlichen Willen orientiert.",
            },
        ],
        "quiz": [
            {
                "id": "11-1",
                "question": "Unterstützte Entscheidungsfindung bedeutet:",
                "options": [
                    "Möglichst eigene Entscheidung der Person ermöglichen",
                    "Immer allein entscheiden",
                    "Nur Angehörige entscheiden lassen",
                    "Nie erklären, nur anordnen",
                ],
                "correct": 0,
                "explain": "Paradigmenwechsel im modernen Betreuungsrecht.",
            },
            {
                "id": "11-2",
                "question": "Ersatzentscheidungen sind:",
                "options": [
                    "Erste Wahl",
                    "Nachrangig, wenn Unterstützung nicht ausreicht",
                    "Verboten",
                    "Nur bei Mietrecht erlaubt",
                ],
                "correct": 1,
                "explain": "Unterstützung vor Ersetzung.",
            },
            {
                "id": "11-3",
                "question": "Willensermittlung sollte:",
                "options": [
                    "Dokumentiert und nachvollziehbar sein",
                    "Nur mündlich ohne Notiz bleiben",
                    "Nur einmal im Leben erfolgen",
                    "Nur per E-Mail an das Gericht ohne Gespräch",
                ],
                "correct": 0,
                "explain": "Qualität und Nachweisbarkeit der Orientierung am Willen.",
            },
            {
                "id": "11-4",
                "question": "Bei riskanten Wünschen gilt oft:",
                "options": [
                    "Gespräch, Aufklärung, Abwägung – nicht sofortiger Zwang",
                    "Sofortige Unterbringung ohne Prüfung",
                    "Ignorieren aller Risiken",
                    "Nur Polizei ohne Betreuungsrecht",
                ],
                "correct": 0,
                "explain": "Selbstbestimmung und Schutz sorgfältig ausbalancieren.",
            },
            {
                "id": "11-5",
                "question": "Präferenzen der betreuten Person erkennt man u. a. durch:",
                "options": [
                    "Gespräche, Biografie, wiederkehrende Aussagen, Bezugspersonen",
                    "Nur Kontoauszüge",
                    "Nur Google-Suche zum Namen",
                    "Nur Diagnoseschlüssel",
                ],
                "correct": 0,
                "explain": "Mehrquellenansatz für mutmaßlichen Willen.",
            },
        ],
    },
]


def get_module(module_id: int):
    for module in MODULES:
        if module["id"] == module_id:
            return module
    return None


def progress_meta():
    return {
        "module_count": len(MODULES),
        "total_hours": sum(m["hours"] for m in MODULES),
        "total_questions": sum(len(m["quiz"]) for m in MODULES),
        "disclaimer": (
            "Lernhilfe zur Vorbereitung und Wiederholung. "
            "Kein anerkannter Sachkundelehrgang nach BtRegV § 6."
        ),
    }
