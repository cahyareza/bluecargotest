# BlueCargo Test Web Application Documentation

## [HomePage](http://34.73.171.215/en/)
Home page merupakan beranda BlueCargo Test Web App, di page ini user akan diarahkan ke login dan register account.

## Account
Untuk mengakses dashboard page maka harus memiliki account terlebih dahulu. 
- Jika belum memiliki account maka dapat klik link [register](http://34.73.171.215/en/accounts/register/).
- Setelah memiliki account maka dapat mengakses link [Login](http://34.73.171.215/en/login/?next=/en/dashboard/).

## [Dashboard Page](http://34.73.171.215/en/dashboard/) 
Pada dashboard page dapat mengakses informasi antara lain:
- Daftar Country
  Daftar country memiliki informasi sbb: Country name, Country flag, dan Country currency.
- Daftar Category
  Daftar category memiliki informasi sbb: country id, category title, dan price per kilo

## [Countries Page](http://34.73.171.215/en/countries/)
Pada countries page ini dapat melihat keseluruhan list country dan melakukan manipulasi seperti menambahkan, menghapus, dan merubah data country.

## [Categories Page](http://34.73.171.215/en/categories/)
Pada categories page ini dapat melihat keseluruhan list category dan melakukan manipulasi seperti menambahkan, menghapus, dan merubah data category.

## [Calculate Page](http://34.73.171.215/en/calculation/)
Calculate Page ini merupakan halaman untuk simulasi perhitungan International Shipping Price, Domestic Shipping Price, dan Total Shipping Price dengan data2 yang diinput berupa Origin, Destination, Product Category, Total Weight(kg).


## Api
Selain menyediakan web app BlueCargo Test, juga menyediakan api, agar mempermudah komunikasi dengan aplikasi lain.

Berikut list Api yang disediakan oleh BlueCargo Test:
### 1. Countries Api
Method "countries" digunakan untuk mendapatkan daftar country yang ada.

### List

```
http://34.73.171.215/en/api/countries/
```

contoh hasil:
```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "country_name": "Singapore",
        "country_flag": "https://flagcdn.com/w320/sg.png",
        "country_currency": "SGD"
    },
    {
        "country_name": "Thailand",
        "country_flag": "https://flagcdn.com/w320/th.png",
        "country_currency": "THB"
    },
    {
        "country_name": "China",
        "country_flag": "https://flagcdn.com/w320/cn.png",
        "country_currency": "CNY"
    },
    {
        "country_name": "United States",
        "country_flag": "https://flagcdn.com/w320/us.png",
        "country_currency": "USD"
    },
    {
        "country_name": "Vietnam",
        "country_flag": "https://flagcdn.com/w320/vn.png",
        "country_currency": "VND"
    },
    {
        "country_name": "Japan",
        "country_flag": "https://flagcdn.com/w320/jp.png",
        "country_currency": "JPY"
    }
]

```

### Search
Untuk mencari spesific country dapat mengunakan link sbb
```python
# pattern
(http://34.73.171.215/en/api/countries/?search={example})

# contoh
http://34.73.171.215/en/api/countries/?search=vietnam
```
- note : example dapat diganti dengan informasi yang ada pada tabel Country name, Country flag, atau Country currency

contoh hasil:
```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "country_name": "Vietnam",
        "country_flag": "https://flagcdn.com/w320/vn.png",
        "country_currency": "VND"
    }
]




```
### 2. Categories
Method "categories" digunakan untuk mendapatkan daftar category yang ada.

### List category

```
http://34.73.171.215/en/api/categories/
```

contoh hasil
```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "country_id": 21,
        "category_title": "Chip",
        "price_per_kilo": 300000
    },
    {
        "country_id": 21,
        "category_title": "Laptop and Computer",
        "price_per_kilo": 220000
    },
    {
        "country_id": 21,
        "category_title": "Electronic",
        "price_per_kilo": 250000
    },
    {
        "country_id": 22,
        "category_title": "Garmens",
        "price_per_kilo": 200000
    },
    {
        "country_id": 23,
        "category_title": "Spare parts",
        "price_per_kilo": 210000
    },
    {
        "country_id": 23,
        "category_title": "Fashion",
        "price_per_kilo": 482135
    },
    {
        "country_id": 22,
        "category_title": "Electronic",
        "price_per_kilo": 560000
    },
    {
        "country_id": 22,
        "category_title": "Spare parts",
        "price_per_kilo": 375000
    },
    {
        "country_id": 24,
        "category_title": "Electronic",
        "price_per_kilo": 635000
    },
    {
        "country_id": 25,
        "category_title": "Electronic",
        "price_per_kilo": 600000
    },
    {
        "country_id": 24,
        "category_title": "Chip",
        "price_per_kilo": 400000
    },
    {
        "country_id": 26,
        "category_title": "Electronic",
        "price_per_kilo": 350000
    },
    {
        "country_id": 25,
        "category_title": "Garmens",
        "price_per_kilo": 200000
    }
]
```

### Search category from origin country
Untuk mencari category dari country asal dapat mengunakan link sbb
```python
# pattern
http://34.73.171.215/en/api/categories/?country_id={example_1}&search={example_2}})

# contoh
http://34.73.171.215/en/api/categories/?country_id=6&search=chip
```
- note : example_1 dapat diganti dengan informasi country_id dan example_2 dapat diganti informasi pada tabel category title atau price per kilo.

contoh hasil:
```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "country_id": 21,
        "category_title": "Chip",
        "price_per_kilo": 300000
    }
]
```

### 3. Destination search
Method "destination search" digunakan untuk mendapatkan informasi kota, link yang dapat diakses:

```
# pattern
http://34.73.171.215/en/api/destination/?search={City}

# contoh
http://34.73.171.215/en/api/destination/?search=Bandung
```
Contoh hasil
```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "city_id": "22",
        "province_id": "9",
        "province": "Jawa Barat",
        "type": "Kabupaten",
        "city_name": "Bandung",
        "postal_code": "40311"
    },
    {
        "city_id": "23",
        "province_id": "9",
        "province": "Jawa Barat",
        "type": "Kota",
        "city_name": "Bandung",
        "postal_code": "40111"
    }
]
```

### 4. Calculate Freight

Merupakan api untuk mendapatkan informasi negara asal(origin), kota/kabupaten tujuan(destination), nama kategori barang(category_name), harga internasional, harga domestik, dan harga total. Data yang dibutuhkan untuk mendapatkan hasil berupa country_id, category_id, destination_id, dan weight.

Alamat api yang dapat diakses sbb;
```
#pattern
http://34.73.171.215/en/api/calculate/


#payload
# contoh 1
{"country_id":21, "category_id":"15", "destination_id":"39", "weight":46} 
```

hasil
```
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "origin": "China",
    "destination": {
        "city_id": "39",
        "province_id": "5",
        "province": "DI Yogyakarta",
        "type": "Kabupaten",
        "city_name": "Bantul",
        "postal_code": "55715"
    },
    "category_name": "Laptop and Computer",
    "international_price": 10120000,
    "domestic_price": "Cannot get data domestic cost from raja ongkir",
    "total_price": "Cannot get data domestic cost from raja ongkir"
}
```