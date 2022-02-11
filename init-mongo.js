const database = "coffee"
const collection = "coffee_information"

db = new Mongo().getDB(database);
db.createCollection(collection, { capped: false });

db.coffee_information.insertMany([
    {
        "_id": "209f4328-001c-48ff-925a-bc4319443340",
        "title": "Black",
        "description": "Coffee served as a beverage without cream or milk.",
        "ingredients": [
            "Coffee"
        ]
    },
    {
        "_id": "17575fe7-034c-4f5a-97c9-9ee8fc762c9a",
        "title": "Latte",
        "description": "A coffee drink of Italian origin made with espresso and steamed milk.",
        "ingredients": [
            "Espresso",
            "Steamed Milk",
            "Foamed Milk"
        ]
    },
    {
        "_id": "01d8ddd3-f437-4313-991d-7d8bea95aee1",
        "title": "Cappuccino",
        "description": "An espresso-based coffee drink that originated in Austria with later development taking place in Italy, and is prepared with steamed milk foam.",
        "ingredients": [
            "Espresso",
            "Steamed Milk"
        ]
    },
    {
        "_id": "0cb2619e-cf1d-4858-b0cc-1e9fcc5a4c19",
        "title": "Americano",
        "description": "A type of coffee drink prepared by diluting an espresso with hot water.",
        "ingredients": [
            "Espresso",
            "Hot Water"
        ]
    },
    {
        "_id": "2432f5d4-72de-4590-ad83-e00f97dc499e",
        "title": "Espresso",
        "description": "A coffee-brewing method of Italian origin, in which a small amount of nearly boiling water (about 90 °C or 190 °F) is forced under 9–10 bars (900–1,000 kPa; 130–150 psi) of pressure through finely-ground coffee beans.",
        "ingredients": [
            "1oz Espresso"
        ]
    },
    {
        "_id": "abca39fb-9f0c-433a-9a6b-e6bcaa4639ec",
        "title": "Doppio",
        "description": "Doppio espresso is a double shot which is extracted using double the amount of ground coffee in a larger-sized portafilter basket.",
        "ingredients": [
            "2oz Espresso"
        ]
    },
    {
        "_id": "bd9fcd2b-99c6-4287-8f9c-fd66d74b6e38",
        "title": "Cortado",
        "description": "A cortado is a beverage consisting of espresso mixed with a roughly equal amount of warm milk to reduce the ac_idity.",
        "ingredients": [
            "1oz Espresso",
            "1oz Steamed Milk"
        ]
    },
    {
        "_id": "8306053f-ee19-4cc7-9f59-b846e586cfbb",
        "title": "Red Eye",
        "description": "A fortified coffee drink in which espresso is combined with normal drip coffee.",
        "ingredients": [
            "Coffee",
            "Espresso"
        ]
    },
    {
        "_id": "108184db-f366-46e2-9868-4ac1a0003de8",
        "title": "Galão",
        "description": "A hot drink from Portugal made by adding foamed milk to espresso coffee in a 3 to 1 ratio",
        "ingredients": [
            "Espresso",
            "Foamed milk"
        ]
    },
    {
        "_id": "77b9107f-b9b1-47b9-8537-6e9a7786eaab",
        "title": "Lungo",
        "description": "A coffee drink made by using a single espresso shot with more water (generally twice as much)",
        "ingredients": [
            "Long Pulled Espresso"
        ]
    },
    {
        "_id": "25f54388-e68c-4696-bc80-df19c480c29e",
        "title": "Macchiato",
        "description": "An espresso coffee drink with a small amount of milk, usually foamed",
        "ingredients": [
            "Espresso",
            "Foamed milk"
        ]
    },
    {
        "_id": "13533308-e281-4ace-b9c8-4dcf3893804d",
        "title": "Mocha",
        "description": "A chocolate-flavoured warm beverage that is a variant of a latte",
        "ingredients": [
            "Espresso",
            "Steamed Milk",
            "Chocolate"
        ]
    },
    {
        "_id": "03862a52-bc0a-45f5-995d-4bdbeeb74c49",
        "title": "Ristretto",
        "description": "A coffee drink made by using a single espresso shot with less water (generally half as much)",
        "ingredients": [
            "Short Pulled Espresso"
        ]
    },
    {
        "_id": "f8905afc-9fa4-454b-adc2-29faa1b5d3e8",
        "title": "Flat White",
        "description": "A coffee drink consisting of espresso with microfoam (finely textured milk)",
        "ingredients": [
            "Espresso",
            "Steamed Milk"
        ]
    },
    {
        "_id": "57855521-91d8-45c2-8d1b-42eb93800bfa",
        "title": "Affogato",
        "description": "An Italian coffee-based dessert served with espresso and topped with ice cream",
        "ingredients": [
            "Espresso",
            "Ice Cream"
        ]
    },
    {
        "_id": "cf778f0a-00b9-4f7e-947d-4ce2d7aaa9f7",
        "title": "Café au Lait",
        "description": "Café au lait is perfect for the coffee minimalist who wants a bit more flavor. Just add a splash of warm milk to your coffee and you’re all set!",
        "ingredients": [
            "Coffee",
            "Steamed Milk"
        ]
    },
    {
        "_id": "f0fd02bd-f780-46ee-8e03-c9500646da0a",
        "title": "Irish",
        "description": "Irish coffee consists of black coffee, whiskey and sugar, topped with whipped cream.",
        "ingredients": [
            "Coffee",
            "Whiskey",
            "Sugar",
            "Cream"
        ]
    },
    {
        "_id": "a8f020c2-bbfd-4023-a783-faf9ea5a548b",
        "title": "Guayoyo",
        "description": "Traditional venezuelan coffee prepared by filtering the ground coffee in a cone of cloth and pouring hot water on top of it. It's prefferably drinked wihout milk nor cream.",
        "ingredients": [
            "Coffee",
            "Traditional",
            "Hot Water"
        ]
    },
    {
        "_id": "c51ef7a8-30b2-4ba7-9f7f-377533dc3204",
        "title": "Cortadito",
        "description": "Traditional cuban coffee method where a bit of freshly brewed coffee is mixed with sugar to create a highly sugared paste. Then add the rest of the coffee and stir adding milk until a 50/50 ratio is achieved.",
        "ingredients": [
            "Coffee",
            "Traditional",
            "Sugar",
            "Milk"
        ]
    },
    {
        "_id": "e013f553-0ad5-4d4d-af19-3bec9b002a53",
        "title": "Aguapanela Coffee",
        "description": "Bring panela and coffee to a boil in a small pan for 30 minutes until panela is melted. Brew your coffee using your favorite brewing technique but add the hot aguapanela instead of hot water. Delicious sweetened coffee is ready.",
        "ingredients": [
            "Coffee",
            "Sweet",
            "Panela",
            "Traditional"
        ]
    }
]);
