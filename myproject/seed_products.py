from reviews.models import Product

products_data = [
    {"name": "Смартфон Samsung Galaxy S23", "descriptions": "Мощный флагман с отличной камерой и экраном 120 Гц."},
    {"name": "Смартфон iPhone 14 Pro", "descriptions": "Инновационный смартфон с Dynamic Island и мощным процессором A16."},
    {"name": "Смартфон Xiaomi 13 Ultra", "descriptions": "Камерофон с оптикой Leica и огромным сенсором."},
    {"name": "Ноутбук MacBook Air M2", "descriptions": "Тонкий и легкий ноутбук с невероятной производительностью и автономностью."},
    {"name": "Ноутбук ASUS ROG Strix", "descriptions": "Игровой ноутбук с видеокартой RTX 4080 и яркой подсветкой."},
    {"name": "Телевизор LG OLED C2", "descriptions": "Превосходный OLED экран с идеальным черным цветом для кино и игр."},
    {"name": "Беспроводные наушники Sony WH-1000XM5", "descriptions": "Лучшее в классе шумоподавление и кристально чистый звук."},
    {"name": "Умные часы Apple Watch Series 8", "descriptions": "Продвинутые функции для здоровья и фитнеса в стильном корпусе."},
    {"name": "Планшет iPad Pro 12.9 M2", "descriptions": "Профессиональный планшет с Liquid Retina XDR дисплеем."},
    {"name": "Фотоаппарат Sony A7 IV", "descriptions": "Полнокадровая беззеркальная камера для фото и видеосъемки."},
    {"name": "Игровая приставка PlayStation 5", "descriptions": "Консоль нового поколения с быстрой загрузкой и тактильной отдачей."},
    {"name": "Игровая приставка Xbox Series X", "descriptions": "Самая мощная консоль Xbox с поддержкой 4K и 120 FPS."},
    {"name": "Робот-пылесос Roborock S8", "descriptions": "Умная уборка с двойной щеткой и высокой силой всасывания."},
    {"name": "Кофемашина DeLonghi Magnifica S", "descriptions": "Автоматическая кофемашина для идеального эспрессо и капучино."},
    {"name": "Микроволновая печь Samsung MS23", "descriptions": "Надежная микроволновка с биокерамическим покрытием."},
    {"name": "Холодильник Haier C2F", "descriptions": "Вместительный холодильник с системой Total No Frost."},
    {"name": "Стиральная машина LG Vivace", "descriptions": "Умная стирка с технологией AI DD для бережного ухода за вещами."},
    {"name": "Электросамокат Xiaomi Scooter 4 Pro", "descriptions": "Удобный городской транспорт с запасом хода до 45 км."},
    {"name": "Монитор Dell UltraSharp U2723QE", "descriptions": "4K монитор с IPS Black матрицей для точной цветопередачи."},
    {"name": "Видеокарта NVIDIA RTX 4090", "descriptions": "Бескомпромиссная производительность для игр и графики."},
    {"name": "Клавиатура Logitech MX Keys", "descriptions": "Премиальная беспроводная клавиатура для комфортной работы."},
    {"name": "Мышь Logitech MX Master 3S", "descriptions": "Эргономичная мышь с точным сенсором и тихими кликами."},
    {"name": "Портативная колонка JBL Charge 5", "descriptions": "Мощный звук и защита от воды для вечеринок на открытом воздухе."},
    {"name": "Умная колонка Яндекс Станция 2", "descriptions": "Голосовой помощник Алиса с качественным звуком и Zigbee."},
    {"name": "Внешний SSD Samsung T7", "descriptions": "Компактный и быстрый накопитель для ваших данных."},
    {"name": "Маршрутизатор ASUS RT-AX88U", "descriptions": "Высокоскоростной Wi-Fi 6 роутер для геймеров и дома."},
    {"name": "Электронная книга PocketBook 743G", "descriptions": "Комфортное чтение с экраном E-Ink и защитой от воды."},
    {"name": "Велосипед горный Specialized Rockhopper", "descriptions": "Надежный байк для поездок по пересеченной местности."},
    {"name": "Квадрокоптер DJI Mini 3 Pro", "descriptions": "Легкий дрон с отличной камерой 4K/60fps."},
    {"name": "Экшн-камера GoPro HERO11", "descriptions": "Запись видео в экстремальных условиях с отличной стабилизацией."},
    {"name": "Электробритва Braun Series 9", "descriptions": "Сеточная бритва для максимально гладкого бритья."},
    {"name": "Фен Dyson Supersonic", "descriptions": "Быстрая сушка волос без экстремального перегрева."},
    {"name": "Увлажнитель воздуха Xiaomi Mi Smart", "descriptions": "Поддержание комфортного климата в помещении."},
    {"name": "Гриль электрический Tefal Optigrill+", "descriptions": "Идеальная прожарка стейков в автоматическом режиме."},
    {"name": "Блендер стационарный KitchenAid", "descriptions": "Мощный помощник на кухне для смузи и соусов."},
    {"name": "Тостер Smeg TSF01", "descriptions": "Стильный ретро-дизайн и хрустящие тосты."},
    {"name": "Электрочайник Bosch TWK8611", "descriptions": "Чайник с выбором температуры для разных сортов чая."},
    {"name": "Система очистки воды Гейзер Престиж", "descriptions": "Чистая питьевая вода прямо из-под крана."},
    {"name": "Вертикальный пылесос Dyson V15 Detect", "descriptions": "Мощный беспроводной пылесос с лазерной подсветкой пыли."},
    {"name": "Кондиционер Daikin FTXM", "descriptions": "Тихий и энергоэффективный инверторный кондиционер."},
    {"name": "Мультиварка REDMOND RMC-M90", "descriptions": "Множество программ для автоматического приготовления блюд."},
    {"name": "Электроинструмент Шуруповерт Makita DDF485", "descriptions": "Надежный бесщеточный инструмент для дома и профи."},
    {"name": "Набор инструментов Ombra OMT94S", "descriptions": "Универсальный набор для ремонта автомобиля и техники."},
    {"name": "Кресло игровое Razer Iskur", "descriptions": "Эргономичная поддержка спины для долгих игровых сессий."},
    {"name": "Стол с регулировкой высоты IKEA UPPSPEL", "descriptions": "Удобное рабочее место для работы сидя и стоя."},
    {"name": "Акустическая система Edifier R1280DB", "descriptions": "Классические полочные колонки с Bluetooth."},
    {"name": "Проектор Epson EH-TW7000", "descriptions": "4K проектор для создания домашнего кинотеатра."},
    {"name": "Микрофон Shure SM7B", "descriptions": "Легендарный динамический микрофон для подкастов и вокала."},
    {"name": "Звуковая карта Focusrite Scarlett 2i2", "descriptions": "Популярный аудиоинтерфейс для домашней записи."},
    {"name": "Оперативная память Kingston FURY Renegade", "descriptions": "Высокоскоростная память для современных ПК."},
]

for product_data in products_data:
    product, created = Product.objects.update_or_create(
        name=product_data["name"],
        defaults={"descriptions": product_data["descriptions"]}
    )
    if created:
        print(f"Продукт '{product.name}' успешно добавлен.")
    else:
        print(f"Продукт '{product.name}' обновлен.")

