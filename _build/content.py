# -*- coding: utf-8 -*-
# All site texts live here. Edit, then run: python3 _build/build.py

SITE = {
  "url": "https://isileisksaule.lt",
  "name": "Įsileisk Saulę",
  "legal_name": "MB „Atlas solutions“",
  "company_code": "306411787",
  "street": "Girulių g. 10",
  "phone_e164": "+37061458748",
  "phone_display": "+370 614 58748",
  "email": "info@isileisksaule.lt",
  "whatsapp": "https://wa.me/37061458748?text=Sveiki,%20noriu%20su%C5%BEinoti%20lang%C5%B3%20valymo%20kain%C4%85.",
  "viber": "viber://chat?number=%2B37061458748",
  "ga4": "G-DL4VGZ7YQM",
  "since": "2014",
  "opens": "07:00", "closes": "18:00", "days_label": "I–VI",
  "min_order": 60,
  "google_reviews": 42,
  "gbp": "https://www.google.com/maps/search/?api=1&query=%C4%AEsileisk%20Saul%C4%99%20lang%C5%B3%20valymas%20Vilniuje",
  "same_as": ["https://www.skelbiu.lt/skelbimai/profesionalus-langu-valymas-vilniuje-23179579.html"],
  "home_title": "Langų valymas Vilniuje – butai, namai, verslas | Įsileisk Saulę",
  "home_desc": "Profesionalus langų valymas Vilniuje ir rajone nuo 2014 m. Periodinis butų ir namų langų valymas, balkonai, vitrinos, postatybinis valymas, kalkių ir lipdukų šalinimas. Vidutiniškai ~8 € už stiklą, 5,0 Google.",
  "nav": [("Paslaugos", "/#paslaugos"), ("Kainos", "/#kainos"), ("Darbai", "/#darbai"), ("Atsiliepimai", "/#atsiliepimai"), ("Patarimai", "/papildoma-informacija/")],
  # third field True = highlighted row
  "prices": [
    ("Periodinis (profilaktinis) langų valymas iš abiejų pusių", "~8 € / stiklas", False),
    ("&nbsp;&nbsp;· standartinis virtuvės langas daugiabutyje", "8 €", False),
    ("&nbsp;&nbsp;· platus vitrininis stiklas nuo grindų iki lubų", "20 €", False),
    ("&nbsp;&nbsp;· siauras vonios langelis", "4 €", False),
    ("Postatybinis ir generalinis langų valymas", "~3× periodinio kainos", False),
    ("Lipdukų šalinimas, laiptinių langai", "pagal nuotraukas", False),
    ("Dideli plotai (nuo 400 m²)", "skaičiuojame kvadratais", False),
    ("Kalkių šalinimas – <strong>į valymo kainą neįeina</strong>", "+10–30 € / stiklas", True),
    ("Minimali užsakymo suma", "60 €", True),
  ],
  "notice": "<strong>Svarbu:</strong> minimali užsakymo suma – <strong>60 €</strong>. Kalkių (kieto vandens dėmių) šalinimas į valymo kainą <strong>neįeina</strong> – papildomai <strong>10–30 € už stiklą</strong>.",
  "mail_subject": "Langų valymo kaina",
  "mail_body": "Sveiki,\n\nnoriu sužinoti langų valymo kainą.\n\nAdresas / rajonas:\nLangų skaičius (apytiksliai):\nPageidaujamas laikas:\n\nNuotraukas prisegu prie laiško.\n",
  "steps": [
    ("Sutariame kainą ir laiką.", "Telefonu arba pagal atsiųstas nuotraukas – taip taupome jūsų laiką."),
    ("Apžiūrime vietoje.", "Prieš darbus kartu apeiname langus – gal kas pasikeitė nuo pokalbio."),
    ("Valome.", "Pastebėję kalkes ar stiklo defektus, iškart jus informuojame."),
    ("Patikriname kartu.", "Apeiname ir peržiūrime rezultatą. Jei ką praleidome – ištaisome vietoje."),
    ("Primename.", "Jei norite, po 3 ar 6 mėnesių priminsime apie kitą valymą."),
  ],
}

GALLERY = [
  ("biuro-langu-valymas-vilniuje.webp", "Biuro langai po valymo"),
  ("privataus-namo-stiklo-fasadas.webp", "Privataus namo stiklinis fasadas"),
  ("kavines-stiklines-sienos-senamiestyje.webp", "Kavinės stiklinės sienos senamiestyje"),
  ("senamiescio-terasos-stiklai.webp", "Terasos stiklai senamiestyje"),
  ("balkono-langu-valymas-daugiabutyje.webp", "Balkono langai daugiabutyje"),
  ("postatybinis-terasos-langu-valymas.webp", "Postatybinis terasos langų valymas"),
  ("svarus-buto-langai.webp", "Buto langai po valymo"),
  ("stiklinio-stogelio-valymas.webp", "Stiklinio stogelio valymas"),
  ("lipduku-salinimas-pries-ir-po.webp", "Lipdukų šalinimas: prieš ir po"),
]

REVIEWS = [
  ("Jau nebe pirmi metai šios įmonės darbuotojai nuskaidrina mūsų gyvenimą. Mūsų langai labai dideli, jų daug, dar ir žiemos sodas – jie puikiai viską išvalo, dirba kruopščiai ir atsakingai.", "Vilija"),
  ("Dėkojame vaikinų komandai, sėkmingai, tvarkingai, kruopščiai ir gana greitai išvaliusiai per 100 mūsų įstaigos langų!", "Lopšelis-darželis „Vaidilutė“"),
  ("Darbas atliktas nepriekaištingai, kruopščiai ir svarbiausia – švariai. Nereikia rūpintis priemonėmis, po darbo nepalieka aptaškytų palangių ir grindų.", "Violeta"),
  ("Vyrai gerai padirbėjo ir, nors valė darbo metu, netrukdė ir neblaškė ofise dirbančių žmonių.", "Ofisas, Konstitucijos pr. 12"),
  ("Puikus darbas už gerą kainą, lengvas bendravimas, greita reakcija. Ne visus langus pavyko pasiekti – dalį pinigų pasiūlė grąžinti. Tai retas atvejis.", "Dmitrijus"),
  ("Tobulai atlikta paslauga! Vaikinai mandagūs ir tvarkingi. Valomės jau trejus metus!", "Elena"),
]

FAQ_HOME = [
  ("Kiek kainuoja langų valymas Vilniuje?", "Periodinis valymas iš abiejų pusių kainuoja vidutiniškai apie 8 € už stiklą – tiek kainuoja standartinis virtuvės langas daugiabutyje. Platus vitrininis stiklas nuo grindų iki lubų – 20 €. Minimali užsakymo suma – 60 €, kalkių šalinimas – papildomai."),
  ("Kaip sužinoti tikslią kainą?", "Paskambinkite – telefonu pasakysime preliminarią kainą „nuo–iki“. Tikslią kainą pasakysime, kai atsiųsite langų nuotraukas el. paštu info@isileisksaule.lt (arba per WhatsApp ar Viber)."),
  ("Kuo skiriasi periodinis ir postatybinis valymas?", "Periodinis (profilaktinis) – įprastas valymas, kai langai valomi bent kartą per metus. Postatybinis ar generalinis reikalingas po remonto arba jei langai nevalyti 3 metus ir ilgiau; jis kainuoja apie 3 kartus daugiau."),
  ("Ar kalkių šalinimas įeina į kainą?", "Ne. Kalkių (kieto vandens dėmių) šalinimas užsakomas papildomai – 10–30 € už stiklą, priklausomai nuo užterštumo. Ar kalkių yra, paaiškėja tik atlikus periodinį valymą."),
  ("Ar reikia pasiruošti prieš valymą?", "Užtenka atlaisvinti priėjimą prie langų: nuimti daiktus ir gėles nuo palangių. Priemones ir įrangą atsivežame patys."),
  ("Kokiose vietovėse dirbate?", "Vilniuje ir Vilniaus rajone. Valome butų, namų, biurų, kavinių ir įstaigų langus."),
]

def _svc(**k): return k

SERVICES = [
  _svc(slug="periodinis-langu-valymas", card_price='~8 € / stiklas', facts=['Stiklai iš vidaus ir iš lauko pusės', 'Rekomenduojama bent kartą per metus', 'Savo įranga ir priemonės', '-Kalkių šalinimas neįeina'], short="Periodinis langų valymas",
    h1="Periodinis (profilaktinis) langų valymas", price_short="~8 € / stiklas",
    title="Periodinis langų valymas Vilniuje – butai ir namai | Įsileisk Saulę",
    desc="Periodinis (profilaktinis) butų ir namų langų valymas Vilniuje iš abiejų pusių. Vidutiniškai ~8 € už stiklą, primename apie kitą valymą po 3 ar 6 mėn.",
    card="Dažniausiai užsakoma paslauga: butų ir namų langai iš abiejų pusių kartą ar du per metus.",
    lead="Įprastas langų valymas butams, namams ir biurams – stiklai iš abiejų pusių. Rekomenduojame valyti bent kartą per metus, o dažniausiai klientai valosi pavasarį ir rudenį.",
    image="svarus-buto-langai.webp", image_alt="Buto langai po periodinio valymo",
    price_detail="Vidutiniškai <strong>~8 € už stiklą</strong> iš abiejų pusių – tiek kainuoja standartinis virtuvės langas daugiabutyje. Platus vitrininis stiklas nuo grindų iki lubų – 20 €.",
    body="""<h2>Kas įeina</h2>
<ul><li>Visų užsakytų langų stiklų valymas iš vidaus ir iš lauko pusės.</li><li>Balkonų ir lodžijų stiklai – jei užsakote kartu.</li><li>Savo įranga ir priemonės – jums nieko nereikia pirkti.</li><li>Po darbų – tvarka: nepaliekame aptaškytų palangių ir grindų.</li></ul>
<h2>Kaip dažnai valyti langus</h2>
<p>Bent kartą per metus. Tuomet užtenka periodinio valymo, o gatvės purvas ir kalkės nespėja įsigerti į stiklą. Jei langai nevalyti 3 metus ir ilgiau arba ką tik baigėte remontą, reikės <a href="/postatybinis-langu-valymas/">postatybinio (generalinio) valymo</a>.</p>
<p>Po valymo pasiūlome priminti apie kitą – po 3 ar 6 mėnesių. Nereikės atsiminti ar vėl ieškoti mūsų kontaktų.</p>
<h2>Kas neįeina</h2>
<p>Įsisenėjusių kalkių dėmių šalinimas į periodinio valymo kainą neįeina. Ar jų yra, paaiškėja tik išvalius langus – tada jas parodome jums ir sutariame dėl <a href="/kalkiu-salinimas-nuo-stiklo/">kalkių šalinimo</a>.</p>
<h2>Kaip užsakyti</h2>
<p>Paskambinkite – pasakysime preliminarią kainą ir laisvus laikus. Arba atsiųskite langų nuotraukas el. paštu ir gausite tikslią kainą.</p>""",
    faq=[("Kiek kainuoja periodinis langų valymas?", "Vidutiniškai ~8 € už stiklą iš abiejų pusių. Minimali užsakymo suma – 60 €."),
         ("Ar reikia būti namuose?", "Taip. Prieš darbus ir po jų kartu apžiūrime langus, kad viskas būtų taip, kaip sutarta."),
         ("Ar galite priminti apie kitą valymą?", "Taip, po valymo pasiūlome priminti po 3 ar 6 mėnesių.")]),

  _svc(slug="balkono-langu-valymas", card_price='~8 € / stiklas', facts=['Stiklai iš abiejų pusių, ir iš lauko', 'Stumdomi ir varstomi rėmai', 'Galima kartu su buto langais – vienas atvykimas'], short="Balkono langų valymas",
    h1="Balkono langų valymas Vilniuje", price_short="~8 € / stiklas",
    title="Balkono langų valymas Vilniuje – ~8 € už stiklą | Įsileisk Saulę",
    desc="Balkonų ir lodžijų stiklų valymas Vilniuje iš abiejų pusių. Stumdomi ir varstomi rėmai, aiški kaina už stiklą, minimali suma 60 €.",
    card="Įstiklinti balkonai ir lodžijos – stumdomi ir varstomi stiklai iš abiejų pusių.",
    lead="Įstiklinto balkono stiklus iš lauko pusės išsivalyti patiems sunku ir nesaugu. Mes tai padarome greitai – iš abiejų pusių, su savo įranga.",
    image="balkono-langu-valymas-daugiabutyje.webp", image_alt="Išvalyti balkono langai daugiabutyje",
    price_detail="Kaip ir periodinis valymas – vidutiniškai <strong>~8 € už stiklą</strong> iš abiejų pusių, priklausomai nuo dydžio.",
    body="""<h2>Ką atliekame</h2>
<ul><li>Balkono ir lodžijos stiklų valymą iš vidaus ir iš lauko pusės.</li><li>Stumdomų ir varstomų balkono rėmų stiklus.</li><li>Kartu galime išvalyti ir buto langus – tuomet vienas atvykimas.</li></ul>
<h2>Verta žinoti</h2>
<p>Balkonų stiklai greitai pasidengia dulkėmis ir gatvės purvu, o lietaus vanduo ant jų palieka mineralų dėmes. Jei stiklai nevalyti kelerius metus, gali prireikti ir kalkių šalinimo – tai paaiškės išvalius stiklus.</p>
<h2>Kaip užsakyti</h2>
<p>Atsiųskite balkono nuotrauką el. paštu – pasakysime tikslią kainą ir pasiūlysime laiką. Arba paskambinkite ir sužinokite preliminarią kainą iš karto.</p>""",
    faq=[("Ar valote balkono stiklus iš lauko pusės?", "Taip, stiklus valome iš abiejų pusių – kaina už stiklą tai ir apima."),
         ("Kiek kainuoja balkono langų valymas?", "Vidutiniškai ~8 € už stiklą, priklausomai nuo dydžio. Minimali užsakymo suma – 60 €, todėl dažnai verta kartu išsivalyti ir buto langus."),
         ("Ar reikia būti namuose?", "Taip, reikia prieigos prie balkono. Prieš ir po darbų kartu apžiūrime langus.")]),

  _svc(slug="postatybinis-langu-valymas", card_price='~3× periodinio kainos', facts=['Po remonto, statybų arba jei nevalyta 3+ metus', 'Dažų, tinko, putų, silikono, plėvelių likučiai', '-Kalkių šalinimas neįeina'], short="Postatybinis langų valymas",
    h1="Postatybinis langų valymas", price_short="~3× profilaktinio",
    title="Postatybinis langų valymas Vilniuje po remonto | Įsileisk Saulę",
    desc="Langų valymas po statybų ir remonto Vilniuje: dažų, tinko, silikono, putų ir apsauginių plėvelių likučiai. Taip pat generalinis valymas, jei langai nevalyti 3+ metus.",
    card="Po remonto ar statybų: dažų, tinko, putų likučiai. Taip pat seniai nevalyti langai.",
    lead="Po remonto ar statybų ant langų lieka dažų, tinko, silikono, montavimo putų ir plėvelių likučių. Juos reikia šalinti atsargiai, kad nesubraižytumėte stiklo.",
    image="postatybinis-terasos-langu-valymas.webp", image_alt="Terasos langai naujos statybos name prieš postatybinį valymą",
    price_detail="Apie <strong>3 kartus daugiau nei periodinis</strong> valymas (periodinis – vidutiniškai ~8 € už stiklą). Tikslią kainą pasakysime iš nuotraukų.",
    body="""<h2>Kada reikalingas šis valymas</h2>
<ul><li>Baigus remontą ar naujos statybos darbus.</li><li>Įsikeliant į naują būstą ar biurą.</li><li>Jei langai nevalyti 3 metus ir ilgiau – tuomet tai vadiname generaliniu valymu.</li></ul>
<h2>Ką pašaliname</h2>
<p>Dažų ir tinko purslus, statybines dulkes, silikono ir montavimo putų likučius, apsauginių plėvelių ir lipdukų klijus. Stiklą, rėmus ir palanges paliekame švarius.</p>
<h2>Atsargiai su stiklu</h2>
<p>Statybiniai nešvarumai dažnai prikepę, o netinkamai grandant stiklą galima subraižyti. Prieš darbus apžiūrime langus ir, pastebėję esamus defektus ar įsigėrusias kalkes, iškart jus informuojame. Taip ramiau ir jums, ir mums.</p>
<h2>Kaip užsakyti</h2>
<p>Atsiųskite kelias langų nuotraukas – iš arti ir bendrą vaizdą. Pasakysime kainą ir laisvus laikus.</p>""",
    faq=[("Kiek kainuoja postatybinis langų valymas?", "Apie 3 kartus daugiau nei periodinis valymas, nes darbas daug imlesnis. Tikslią kainą pasakome iš nuotraukų."),
         ("Ar kalkių šalinimas įeina?", "Ne, kalkių dėmių šalinimas užsakomas papildomai – 10–30 € už stiklą."),
         ("Ar valote naujos statybos namus ir biurus?", "Taip – ir butus, ir privačius namus, ir komercines patalpas.")]),

  _svc(slug="kalkiu-salinimas-nuo-stiklo", card_price='+10–30 € / stiklas', facts=['Pilkos dėmės ir „upeliai“, kurių nenuima valymas', 'Paaiškėja tik išvalius langus', 'Užsakoma kartu su langų valymu'], short="Kalkių šalinimas nuo stiklo",
    h1="Kalkių šalinimas nuo langų stiklo", price_short="10–30 € / stiklas",
    title="Kalkių dėmių šalinimas nuo langų stiklo Vilniuje | Įsileisk Saulę",
    desc="Pilkos dėmės ir „upeliai“ ant stiklo, kurių nepašalina įprastas valymas? Šaliname kieto vandens (kalkių) nuosėdas nuo langų ir stiklinių sienų Vilniuje. 10–30 € už stiklą.",
    card="Pilkos dėmės ir „upeliai“, kurių nepašalina įprastas valymas.",
    lead="Jei ir išvalius langus matyti pilkų dėmių ar „upelių“ – tai kieto vandens mineralai (kalkės), įsigėrę į stiklo paviršių. Įprastu valymu jų nepašalinsite.",
    image="privataus-namo-stiklo-fasadas.webp", image_alt="Privataus namo stiklinis fasadas po kalkių šalinimo",
    price_detail="<strong>10–30 € už stiklą</strong>, priklausomai nuo to, kiek giliai kalkės įsigėrusios. Ar jų yra, paaiškėja tik atlikus periodinį valymą.",
    body="""<h2>Iš kur atsiranda kalkių dėmės</h2>
<p>Stiklo paviršius porėtas. Ant jo nuolat patenka lietaus, laistymo ar plovimo vanduo su mineralais. Kaitinant saulei mineralai po truputį įsigeria į stiklą, ir susidaro pilkšvos dėmės, dryžiai ir „upeliai“ po palangėmis.</p>
<h2>Kodėl verta šalinti laiku</h2>
<p>Kuo ilgiau kalkės lieka ant stiklo, tuo giliau įsigeria ir tuo brangiau jas pašalinti. Ilgainiui vienintelė išeitis gali būti stiklo poliravimas ar net keitimas. Reguliarus langų valymas neleidžia kalkėms kauptis.</p>
<h2>Kaip dirbame</h2>
<p>Pirmiausia atliekame periodinį valymą. Tik tada tampa aišku, ar ant stiklo liko kalkių: kai kurie „upeliai“ būna visai nauji ir puikiai nusivalo. Likusias kalkes parodome jums ir tik tada sutariame dėl jų šalinimo. Jokių netikėtų papildomų sumų.</p>
<h2>Ar galima įvertinti iš nuotraukos?</h2>
<p>Ne. Iš nuotraukos neįmanoma atskirti kalkių nuo įprasto purvo. Galime tik nuspėti, kad kalkių greičiausiai bus, jei langai nevalyti kelerius metus, jei patys bandėte valyti ir kažkas nenusivalė, arba jei tai tipinė vieta – pavyzdžiui, viršutinė neatidaromo lango dalis.</p>""",
    faq=[("Kiek kainuoja kalkių šalinimas?", "10–30 € už stiklą, priklausomai nuo užterštumo. Tikslią kainą galime pasakyti tik išvalę langus ir pamatę, kas liko."),
         ("Ar galima kalkes pašalinti visiškai?", "Dažniausiai – taip. Jei kalkės įsigėrusios labai giliai, prieš šalindami apie tai pasakysime atvirai."),
         ("Kaip išvengti kalkių dėmių?", "Valykite langus reguliariai – bent kartą per metus. Po valymo galime priminti apie kitą valymą po 3 ar 6 mėnesių.")]),

  _svc(slug="lipduku-salinimas-nuo-stiklo", card_price='Kaina pagal nuotraukas', facts=['Reklaminiai lipdukai, užrašai, plėvelės', 'Nuimame ir klijų likučius', 'Po to stiklą išvalome'], short="Lipdukų šalinimas nuo stiklo",
    h1="Lipdukų ir plėvelių šalinimas nuo stiklo", price_short="Pagal nuotraukas",
    title="Lipdukų ir reklaminių plėvelių šalinimas nuo vitrinų Vilniuje | Įsileisk Saulę",
    desc="Šaliname reklaminius lipdukus, plėveles ir klijų likučius nuo verslo vitrinų ir langų Vilniuje. Stiklas lieka švarus, be klijų dėmių.",
    card="Reklaminiai lipdukai, plėvelės ir klijų likučiai nuo vitrinų.",
    lead="Keičiate iškabą, išsikraustote ar atnaujinate vitriną? Nuimame reklaminius lipdukus ir plėveles kartu su klijų likučiais, o stiklą paliekame švarų.",
    image="lipduku-salinimas-pries-ir-po.webp", image_alt="Vitrina prieš ir po lipdukų šalinimo",
    price_detail="Kaina priklauso nuo ploto ir lipdukų tipo – <strong>atsiųskite nuotrauką</strong> ir pasakysime tikslią sumą.",
    body="""<h2>Ką šaliname</h2>
<ul><li>Reklaminius lipdukus ir užrašus nuo vitrinų.</li><li>Matines, spalvotas ir apsaugines plėveles.</li><li>Senų lipdukų klijų likučius.</li></ul>
<h2>Kam tai aktualu</h2>
<p>Parduotuvėms, kavinėms ir biurams, kurie keičia vitrinų dizainą, patalpų nuomotojams prieš naują nuomininką, taip pat po remonto.</p>
<h2>Rezultatas</h2>
<p>Nuėmus lipdukus stiklą išvalome – be klijų dėmių ir dryžių. Jei reikia, kartu išvalome ir kitas vitrinas bei langus.</p>""",
    faq=[("Kiek kainuoja lipdukų šalinimas?", "Priklauso nuo ploto ir lipdukų – pasakome iš nuotraukos."),
         ("Ar liks klijų dėmės?", "Ne, klijų likučius pašaliname ir stiklą išvalome."),
         ("Ar dirbate su įmonėmis?", "Taip, dirbame su verslu – biurais, kavinėmis, parduotuvėmis ir įstaigomis.")]),

  _svc(slug="vitrinu-ir-biuro-langu-valymas", card_price='~8 € / stiklas · vitrininis 20 €', facts=['Biurai, kavinės, parduotuvės, įstaigos', 'Nuo 400 m² skaičiuojame kvadratais', 'Galime valyti reguliariai'], short="Vitrinų ir biurų langai",
    h1="Vitrinų ir biuro langų valymas", price_short="~8 € / stiklas",
    title="Vitrinų ir biuro langų valymas Vilniuje verslui | Įsileisk Saulę",
    desc="Biurų, kavinių, parduotuvių vitrinų ir įstaigų langų valymas Vilniuje. Dirbame netrukdydami darbui. Dideli plotai nuo 400 m² skaičiuojami kvadratais.",
    card="Biurai, kavinės, parduotuvės ir įstaigos. Dirbame netrukdydami jūsų darbui.",
    lead="Švarios vitrinos ir langai – pirmas dalykas, kurį pamato jūsų klientai. Valome biurų, kavinių, parduotuvių ir įstaigų langus Vilniuje.",
    image="kavines-stiklines-sienos-senamiestyje.webp", image_alt="Kavinės stiklinės sienos Vilniaus senamiestyje po valymo",
    price_detail="Vidutiniškai <strong>~8 € už stiklą</strong>, platus vitrininis stiklas nuo grindų iki lubų – 20 €. Dideli plotai nuo 400 m² skaičiuojami kvadratais.",
    body="""<h2>Kam valome</h2>
<ul><li>Biurams ir verslo centrams.</li><li>Kavinėms, restoranams ir terasoms.</li><li>Parduotuvių vitrinoms.</li><li>Įstaigoms – mums teko valyti ir per 100 vieno darželio langų.</li></ul>
<h2>Dirbame netrukdydami</h2>
<p>Valome tvarkingai ir tyliai, kad darbuotojai ir klientai galėtų užsiimti savo reikalais. Laiką suderiname iš anksto.</p>
<h2>Reguliarus valymas</h2>
<p>Vitrinoms ir biurams tinka reguliarus valymas. Sutarsime periodiškumą ir priminsime apie kitą valymą, kad jums nereikėtų to sekti.</p>""",
    faq=[("Ar galite valyti reguliariai?", "Taip, sutariame periodiškumą ir iš anksto primename apie kitą valymą."),
         ("Kaip skaičiuojama kaina dideliems objektams?", "Nuo 400 m² stiklo ploto kainą skaičiuojame kvadratais, mažesnius – stiklais."),
         ("Ar galite valyti ne darbo metu?", "Laiką derinkime telefonu – pasistengsime prisitaikyti prie jūsų darbo grafiko.")]),

  _svc(slug="laiptiniu-langu-valymas", card_price='Kaina pagal nuotraukas', facts=['Bendrijoms ir administratoriams', 'Visi aukštai per vieną atvykimą', 'Išrašome sąskaitas'], short="Laiptinių langų valymas",
    h1="Daugiabučių laiptinių langų valymas", price_short="Pagal nuotraukas",
    title="Daugiabučių laiptinių langų valymas Vilniuje | Įsileisk Saulę",
    desc="Daugiabučių laiptinių langų valymas Vilniuje bendrijoms ir administratoriams. Kaina pagal nuotraukas, sąskaitos įmonėms.",
    card="Bendrijoms ir administratoriams – visos laiptinės langai per vieną atvykimą.",
    lead="Laiptinių langai dažnai nevalomi metų metus. Išvalome visų aukštų laiptinės langus per vieną atvykimą – bendrijoms, administratoriams ir gyventojų grupėms.",
    image="buto-langu-valymas.webp", image_alt="Švarūs langai po valymo",
    price_detail="Kaina priklauso nuo aukštų ir langų skaičiaus – <strong>atsiųskite nuotraukas</strong> arba paskambinkite.",
    body="""<h2>Kam tinka</h2>
<ul><li>Daugiabučių namų savininkų bendrijoms.</li><li>Namų administratoriams.</li><li>Gyventojams, kurie susitarė kartu užsakyti valymą.</li></ul>
<h2>Kaip užsakyti</h2>
<p>Parašykite, kiek aukštų ir laiptinių, atsiųskite kelias langų nuotraukas. Pasakysime kainą ir laisvus laikus.</p>
<p>Jei langai labai seniai nevalyti, gali prireikti generalinio valymo – tai įvertinsime iš nuotraukų. Ar yra kalkių, paaiškės tik išvalius langus.</p>""",
    faq=[("Kiek kainuoja laiptinės langų valymas?", "Priklauso nuo aukštų ir langų skaičiaus bei užterštumo. Pasakysime iš nuotraukų."),
         ("Ar išrašote sąskaitas bendrijoms?", "Taip, dirbame kaip MB „Atlas solutions“."),
         ("Ar galima valyti reguliariai?", "Taip, galime susitarti dėl reguliaraus valymo, pvz., pavasarį ir rudenį.")]),
]

ARTICLES = [
  dict(slug="svariu-langu-svarba-nauda-sveikatai-ir-namu-vertei",
    title="Švarių langų svarba: nauda sveikatai ir namų vertei",
    desc="Kodėl verta reguliariai valyti langus: daugiau dienos šviesos, geresnė nuotaika, sveikesnė aplinka, ilgiau tarnaujantys langai ir didesnė namų vertė.",
    author="Stanislav Teliatnikov", date="2025-03-02",
    body="""<p>Langai dažnai vadinami namų akimis – pro juos matome pasaulį ir įsileidžiame saulės šviesą. Tačiau daug kas neįvertina, kiek švarūs langai veikia gyvenamąją erdvę, savijautą ir net būsto vertę. Pažiūrėkime, kodėl reguliarus langų valymas turėtų būti įprasta namų priežiūros dalis.</p>
<h2>Daugiau natūralios šviesos ir geresnė nuotaika</h2>
<p>Lietuvoje dienos šviesos kiekis per metus labai skiriasi – nuo ilgų vasaros dienų iki trumpų žiemos. Švarūs langai įleidžia daugiau šviesos, o tai ypač svarbu tamsiuoju metų laiku. Natūrali šviesa padeda reguliuoti miego ritmą, gerina nuotaiką ir susikaupimą dirbant iš namų.</p>
<p>Nešvarūs langai sulaiko pastebimą dalį šviesos. Reguliarus valymas padeda išnaudoti visą turimą dienos šviesą ištisus metus.</p>
<h2>Geresnė išvaizda ir būsto vertė</h2>
<p>Pirmas įspūdis svarbus. Švarūs, žvilgantys langai – vienas pirmųjų dalykų, kuriuos pastebi svečias ar potencialus pirkėjas. Gerai prižiūrėtas būstas atrodo patraukliau ir dažnai greičiau randa pirkėją ar nuomininką.</p>
<h2>Sveikesnė aplinka</h2>
<p>Ant langų, rėmų ir palangių kaupiasi dulkės, žiedadulkės ir kiti alergenai, o drėgnose vietose gali atsirasti pelėsis. Reguliariai valant jų mažėja – tai aktualu šeimoms su vaikais, vyresnio amžiaus žmonėms ir alergiškiems.</p>
<h2>Ilgiau tarnaujantys langai</h2>
<p>Langai – didelė investicija, o šaltos žiemos ir temperatūrų svyravimai juos alina. Reguliarus valymas:</p>
<ul><li>neleidžia kalkėms ir kitoms nuosėdoms įsigerti į stiklą;</li><li>padeda anksti pastebėti sandarinimo ar rėmų problemas, kol remontas dar pigus;</li><li>apsaugo nuo įsisenėjusių dėmių, kurių vėliau nebepavyksta pašalinti.</li></ul>
<p>Profesionalaus langų valymo kaina nedidelė, palyginti su stiklo poliravimo ar langų keitimo išlaidomis.</p>
<h2>Energijos taupymas</h2>
<p>Pro švarius langus žiemą patenka daugiau saulės šilumos, o dieną reikia mažiau dirbtinio apšvietimo. Kylant energijos kainoms, net nedidelis sutaupymas yra malonus.</p>
<h2>Malonesni namai</h2>
<p>Pro krištolo švarumo langus matyti sodas, kiemas ar miestas, o kambariai atrodo erdvesni ir šviesesni. Tai ypač jaučiama žiemą, kai daugiau laiko praleidžiame viduje.</p>
<h2>Išvada</h2>
<p>Švarūs langai – ne prabanga, o sveikų, šviesių ir vertingų namų dalis. Langus galima valyti ir patiems, tačiau aukštai esantiems, dideliems ar sunkiai pasiekiamiems langams patogiau ir saugiau pasikviesti profesionalus – su tinkama įranga ir patirtimi.</p>"""),
]

PRIVACY = """<section><div class="wrap article">
<p class="crumbs"><a href="/">Pradžia</a> › Privatumo politika</p>
<h1>Privatumo politika</h1>
<p>Duomenų valdytojas: MB „Atlas solutions“, įm. k. 306411787, Girulių g. 10, Vilnius, el. paštas <a href="mailto:info@isileisksaule.lt">info@isileisksaule.lt</a>.</p>
<h2>Kokius duomenis tvarkome</h2>
<p>Kai jūs mums skambinate, rašote el. paštu, WhatsApp ar Viber, tvarkome jūsų pateiktus kontaktinius duomenis, adresą ir langų nuotraukas – tik tam, kad galėtume įvertinti kainą, suderinti ir atlikti darbus bei, jei sutinkate, priminti apie kitą valymą.</p>
<h2>Slapukai ir analitika</h2>
<p>Svetainėje naudojame „Google Analytics“ ir „Google Ads“ slapukus tik jums sutikus. Jie padeda suprasti, kaip lankytojai randa svetainę, ir vertinti reklamos veiksmingumą (pvz., kiek kartų paspaustas mygtukas „Skambinti“). Nesutikus šie slapukai nenaudojami. Savo pasirinkimą galite bet kada pakeisti <a href="#" data-open-consent>slapukų nustatymuose</a>.</p>
<h2>Saugojimas ir jūsų teisės</h2>
<p>Duomenis saugome tiek, kiek reikia paslaugai suteikti ir teisės aktų reikalavimams įvykdyti. Turite teisę susipažinti su savo duomenimis, juos ištaisyti ar prašyti ištrinti – parašykite mums el. paštu. Taip pat galite kreiptis į Valstybinę duomenų apsaugos inspekciją.</p>
</div></section>"""
SITE["privacy_html"] = PRIVACY

# ---------- Texts in the style of the original site ----------
HOME = {
  "hero_h1": "Profesionalus langų valymas Vilniuje ir rajone.",
  "hero_h2": "Aiškios kainos. Geri atsiliepimai.",
  "order_call": "Norėdami sužinoti savo langų valymo kainą, spauskite mygtuką „Skambinti“ – telefonu pasakysime preliminarią „nuo–iki“ kainą ir galėsite pasirinkti iš poros laisvų laikų.",
  "order_photos": "Norėdami sužinoti tikslią kainą, atsiųskite savo langų nuotraukas paspaudę „Siųsti nuotraukas“ – atsidarys laiškas mūsų el. paštu. Trumpam klausimui – žalias „WhatsApp“ mygtukas dešinėje ekrano pusėje.",
  "process_intro": "Jau seniai valome langus, todėl sukūrėme procesą, leidžiantį mums kaskart patikimai teikti tokią pačią paslaugą:",
  "process_icons": ["telefonas", "apziura", "informuojame", "patikriname", "priminimas"],
  "about_lead": "Esame nedidelė mandagių specialistų komanda, teikianti langų valymo paslaugas Vilniuje. Dirbame nuo 2014 metų. Suprantame, kad langai (ar vitrinos) yra jūsų namų (ar verslo) „veidas“, todėl savo darbą atliekame itin atsakingai. Mums būtų malonu įleisti saulę ir į jūsų namus!",
  "about": [
    "Langų valymo paskirtis – ne vien švarūs, bet ir sveiki langai. Gatvės purvas, kieto vandens mineralai (kalkės), organinės kilmės nešvarumai ne tik atrodo neestetiškai, bet ir gadina stiklą. Stiklo paviršius porėtas, todėl, kaitinant saulei, mineralai palaipsniui į jį įsigeria. Būtent todėl net išvalius langus vis tiek matyti įsisenėjusių kalkių klodų ar „upelių“.",
    "Tokiu atveju tenka užsakyti brangias kalkių šalinimo procedūras arba keisti stiklus. Viso to galima išvengti reguliariai valant langus – taip visada džiaugsitės ryškia saulės šviesa ir sutaupysite.",
  ],
  "reviews_note": "Visus šiuos atsiliepimus ir daugiau galima rasti mūsų skelbiu.lt puslapyje – tada dar neturėjome svetainės :)",
}

KALKES = dict(slug="kas-yra-kalkes",
  h1="Kas yra kalkės ant langų ir kodėl jų nepašalina įprastas valymas?",
  title="Kas yra kalkės ant langų ir kodėl jų nepašalina įprastas valymas | Įsileisk Saulę",
  desc="Kalkės ant langų – pilkos dėmės ir „upeliai“, kurie lieka net išvalius stiklą. Paaiškiname, iš kur jos atsiranda, kodėl periodinis valymas jų nepašalina ir kodėl jų neįmanoma įvertinti iš nuotraukos.",
  lead="Jei ir po valymo ant stiklo matyti pilkšvų dėmių, dryžių ar „upelių“ – tai kalkės. Tai ne purvas ant stiklo paviršiaus, todėl įprastas valymas jų nepašalina.",
  body="""<h2>Kas tai yra</h2>
<p>Kalkės – tai kieto vandens mineralų nuosėdos. Vanduo ant langų patenka su lietumi, laistant gėles, plaunant fasadą ar balkoną, varvant nuo stogo ar stogelio. Vandeniui išdžiūvus mineralai lieka ant stiklo.</p>
<p>Stiklo paviršius porėtas. Kaitinant saulei mineralai po truputį į jį įsigeria, ir susidaro sluoksnis, kuris tampa tarsi stiklo dalimi. Todėl jo nenuplauna nei vanduo, nei įprastos valymo priemonės.</p>
<h2>Kaip jos atrodo</h2>
<ul><li>Pilkšvos ar baltos dėmės, ypač gerai matomos prieš saulę.</li><li>Dryžiai ir „upeliai“ po palangėmis, stogeliais, balkonų atbrailomis.</li><li>Matinis, tarsi aprasojęs stiklas, kuris nežvilga net išvalytas.</li></ul>
<h2>Kodėl periodinis valymas jų nepašalina</h2>
<p><strong>Periodinis (profilaktinis) valymas nuima purvą, dulkes ir dėmes nuo stiklo paviršiaus.</strong> Kalkės yra ne ant paviršiaus, o įsigėrusios į jį. Joms pašalinti reikia specialių priemonių ir kelis kartus daugiau darbo kiekvienam stiklui.</p>
<p>Todėl kalkių šalinimas yra <strong>atskira paslauga</strong> ir į valymo kainą neįeina. Jis kainuoja <strong>10–30 € už stiklą</strong>, priklausomai nuo to, kiek giliai kalkės įsigėrusios.</p>
<h2>Kodėl jų neįmanoma įvertinti iš nuotraukos</h2>
<p>Iš nuotraukos kalkių neatskirsi nuo įprasto purvo. Kai kurie „upeliai“ būna visai nauji ir išvalius puikiai nusivalo. <strong>Ar kalkių tikrai yra, paaiškėja tik atlikus periodinį valymą.</strong></p>
<p>Galime tik gana tiksliai nuspėti, kad kalkių greičiausiai bus, jei:</p>
<ul><li>langai nevalyti kelerius metus;</li><li>patys bandėte valyti, bet kažkas nenusivalė;</li><li>tai tipinė vieta, pavyzdžiui, viršutinė neatidaromo lango dalis.</li></ul>
<p>Išvalę langus kartu su jumis juos apžiūrime. Jei liko kalkių, jas parodome ir sutariame, ar norite jas šalinti. Jokių netikėtų sumų sąskaitoje.</p>
<h2>Kaip išvengti kalkių</h2>
<ul><li><strong>Valykite langus reguliariai</strong> – bent kartą per metus. Tada mineralai nespėja įsigerti į stiklą.</li><li>Laistydami gėles ar plaudami balkoną stenkitės neaptaškyti stiklų. Jei aptaškėte, nušluostykite, kol vanduo dar neišdžiūvo.</li><li>Po valymo galime priminti apie kitą valymą po 3 ar 6 mėnesių.</li></ul>
<p>Jei kalkių jau yra, daugiau apie jų šalinimą rasite puslapyje <a href="/kalkiu-salinimas-nuo-stiklo/">Kalkių šalinimas nuo stiklo</a>.</p>""")
