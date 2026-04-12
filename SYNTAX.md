### 🛠️ Key Transformations (V0.5.0)
 
The standard BNF grammar (`python.gram`) has been modified to support the following dual-syntax:
 
## Simple Statements
| Standard Python | Custom Turkish Syntax |
| --- | --- |
| `return` | `döndür` |
| `yield` | `döndürdur` |
| `break` | `kaçış` |
| `raise` | `fırlat` |
| `pass` | `atla` |
| `except` | `yakala` |
| `finally` | `nihayet` |
| `del` | `azlet` |
| `assert` | `teyit` |
| `continue` | `sürdür` |
| `global` | `umumi` |
| `nonlocal` | `harici` |
 
## Structural
| Standard Python | Custom Turkish Syntax |
| --- | --- |
| `:` | `ise` |
| `as` | `olarak` |
 
**Note: `ise` is a clause terminator (used within if, for, def, etc.)**
 
## Compound Statements
| Standard Python | Custom Turkish Syntax |
| --- | --- |
| `with` | `birlikte` |
| `else` | `değilse` |
| `try` | `dene` |
| `if` | `eğer` |
| `while` | `iken` |
| `def` | `işlev` |
| `class` | `sınıf` |
| `for` | `ozyinele` |
| `in (for)` | `içinde` |
| `match` | `eslestir` |
| `case` | `durum` |
 
## Expression Level
| Standard Python | Custom Turkish Syntax |
| --- | --- |
| `x if cond else y` | `x eğer koşul değilse y` |
| `x in y` | `x içinde y` |
| `x not in y` | `x not içinde y` |
 
## Comprehensions
| Standard Python | Custom Turkish Syntax |
| --- | --- |
| `[x for x in y]` | `[x for x içinde y]` |
| `[x for x in y]` | `[x ozyinele x içinde y]` |
| `{x for x in y}` | `{x for x içinde y}` |
| `{k: v for k, v in y}` | `{k: v for k, v içinde y}` |
 
## Atom Expressions
| Standard Python | Custom Turkish Syntax |
| --- | --- |
| `None` | `Bos` |
| `True` | `Dogru` |
| `False` | `Yanlis` |
 
## Boolean Operators
| Standard Python | Custom Turkish Syntax |
| --- | --- |
| `not` | `degil` |
| `and` | `ve` |
| `or` | `veya` |
 
## Builtins
| Standard Python | Custom Turkish Syntax |
| --- | --- |
| `input` | `girdi` |
| `abs` | `mutlak` |
| `len` | `uzunluk` |
| `print` | `yazdir` |
| `int` | `tamsayi` |
| `list` | `liste` |
| `range` | `aralik` |
| `bool` | `mantiksal` |
| `float` | `ondalik` |
| `str` | `dizgi` |
| `tuple` | `demet` |
| `dict` | `sözlük` |
| `sum` | `toplam` |
 
## List Methods
| Standard Python | Custom Turkish Syntax |
| --- | --- |
| `list.append` | `liste.ekle` |
| `list.remove` | `liste.sil` |
| `list.count` | `liste.say` |
| `list.extend` | `liste.genislet` |
| `list.index` | `liste.dizin` |
| `list.insert` | `liste.araya_ekle` |
| `list.pop` | `liste.cikar` |
| `list.sort` | `liste.sirala` |
| `list.reverse` | `liste.ters_cevir` |
| `list.copy` | `liste.kopyala` |
| `list.clear` | `liste.temizle` |
 
## dizgi (str) Methods
| Standard Python | Custom Turkish Syntax |
| --- | --- |
| `str.upper` | `dizgi.büyüt` |
| `str.lower` | `dizgi.küçült` |
| `str.capitalize` | `dizgi.ilk_büyüt` |
| `str.title` | `dizgi.başlık` |
| `str.swapcase` | `dizgi.büyüklüğü_değiştir` |
| `str.casefold` | `dizgi.küçült_agresif` |
| `str.strip` | `dizgi.kırp` |
| `str.lstrip` | `dizgi.soldan_kırp` |
| `str.rstrip` | `dizgi.sağdan_kırp` |
| `str.split` | `dizgi.böl` |
| `str.rsplit` | `dizgi.sağdan_böl` |
| `str.splitlines` | `dizgi.satırlara_böl` |
| `str.join` | `dizgi.birleştir` |
| `str.partition` | `dizgi.parçala` |
| `str.rpartition` | `dizgi.sağdan_parçala` |
| `str.find` | `dizgi.bul` |
| `str.rfind` | `dizgi.sağdan_bul` |
| `str.index` | `dizgi.indeks` |
| `str.rindex` | `dizgi.sağdan_indeks` |
| `str.count` | `dizgi.say` |
| `str.replace` | `dizgi.değiştir` |
| `str.startswith` | `dizgi.ile_başlar` |
| `str.endswith` | `dizgi.ile_biter` |
| `str.removeprefix` | `dizgi.önek_kaldır` |
| `str.removesuffix` | `dizgi.sonek_kaldır` |
| `str.center` | `dizgi.ortala` |
| `str.ljust` | `dizgi.sola_yasla` |
| `str.rjust` | `dizgi.sağa_yasla` |
| `str.zfill` | `dizgi.sıfır_doldur` |
| `str.expandtabs` | `dizgi.sekme_genişlet` |
| `str.isalpha` | `dizgi.harf_mi` |
| `str.isdigit` | `dizgi.rakam_mı` |
| `str.isalnum` | `dizgi.alfasayısal_mı` |
| `str.isspace` | `dizgi.boşluk_mu` |
| `str.isupper` | `dizgi.büyük_mü` |
| `str.islower` | `dizgi.küçük_mü` |
| `str.istitle` | `dizgi.başlık_mı` |
| `str.isascii` | `dizgi.ascii_mi` |
| `str.isdecimal` | `dizgi.ondalık_mı` |
| `str.isnumeric` | `dizgi.sayısal_mı` |
| `str.isprintable` | `dizgi.yazılabilir_mi` |
| `str.isidentifier` | `dizgi.tanımlayıcı_mı` |
| `str.encode` | `dizgi.kodla` |
| `str.translate` | `dizgi.çevir` |
| `str.maketrans` | `dizgi.çeviri_tablosu` |
| `str.format` | `dizgi.biçimle` |
| `str.format_map` | `dizgi.eşlemden_biçimle` |
 
## sözlük (dict) Methods
| Standard Python | Custom Turkish Syntax |
| --- | --- |
| `dict.keys` | `sözlük.anahtarlar` |
| `dict.values` | `sözlük.değerler` |
| `dict.items` | `sözlük.ögeler` |
| `dict.get` | `sözlük.al` |
| `dict.update` | `sözlük.güncelle` |
| `dict.setdefault` | `sözlük.varsayılan_ata` |
| `dict.pop` | `sözlük.çıkar` |
| `dict.popitem` | `sözlük.öge_çıkar` |
| `dict.copy` | `sözlük.kopyala` |
| `dict.clear` | `sözlük.temizle` |
| `dict.fromkeys` | `sözlük.anahtarlardan` |
 
## Standart Library
| Standard Python | Custom Turkish Syntax |
| --- | --- |
| `import math` | `temin matematik` |
| `import random` | `temin rastgele` |
| `import tkinter` | `temin pencere` |
 
### matematik (math) Aliases
| Standard Python | Hazer |
| --- | --- |
| `math.ceil` | `matematik.tavan` |
| `math.floor` | `matematik.taban` |
| `math.trunc` | `matematik.kirp` |
| `math.fabs` | `matematik.mutlak` |
| `math.sqrt` | `matematik.karekök` |
| `math.pow` | `matematik.üs` |
| `math.exp` | `matematik.üstel` |
| `math.log` | `matematik.logaritma` |
| `math.log2` | `matematik.log2` |
| `math.log10` | `matematik.log10` |
| `math.sin` | `matematik.sin` |
| `math.cos` | `matematik.kos` |
| `math.tan` | `matematik.tan` |
| `math.asin` | `matematik.arcsin` |
| `math.acos` | `matematik.arckos` |
| `math.atan` | `matematik.arctan` |
| `math.atan2` | `matematik.arctan2` |
| `math.degrees` | `matematik.dereceye_cevir` |
| `math.radians` | `matematik.radyana_cevir` |
| `math.hypot` | `matematik.hipotenüs` |
| `math.factorial` | `matematik.faktoriyel` |
| `math.gcd` | `matematik.obeb` |
| `math.lcm` | `matematik.okek` |
| `math.comb` | `matematik.komb` |
| `math.perm` | `matematik.perm` |
| `math.isfinite` | `matematik.sonlu_mu` |
| `math.isinf` | `matematik.sonsuz_mu` |
| `math.isnan` | `matematik.tanimsiz_mi` |
| `math.isclose` | `matematik.yakin_mi` |
| `math.remainder` | `matematik.kalan` |
| `math.fmod` | `matematik.mod` |
| `math.modf` | `matematik.ayrıştır` |
| `math.frexp` | `matematik.mantis` |
| `math.ldexp` | `matematik.ikili_üs` |
| `math.fsum` | `matematik.kesin_toplam` |
| `math.prod` | `matematik.çarpım` |
| `math.copysign` | `matematik.işaret_kopyala` |
| `math.nextafter` | `matematik.sonraki` |
 
### rastgele (random) Aliases
| Standard Python | Hazer |
| --- | --- |
| `random.random` | `rastgele.sayi` |
| `random.randint` | `rastgele.tam_sayi` |
| `random.randrange` | `rastgele.aralik` |
| `random.uniform` | `rastgele.ondalik` |
| `random.randbytes` | `rastgele.bayt` |
| `random.getrandbits` | `rastgele.bit` |
| `random.triangular` | `rastgele.ucgen` |
| `random.choice` | `rastgele.sec` |
| `random.choices` | `rastgele.secimler` |
| `random.sample` | `rastgele.ornekle` |
| `random.shuffle` | `rastgele.karistir` |
| `random.seed` | `rastgele.tohum` |
| `random.getstate` | `rastgele.durum_al` |
| `random.setstate` | `rastgele.durum_set` |
 
### pencere (tkinter) Aliases
| tkinter | Hazer |
| --- | --- |
| `Tk` | `p.Pencere` |
| `Frame` | `p.Çerçeve` |
| `Label` | `p.Etiket` |
| `Button` | `p.Düğme` |
| `Entry` | `p.Giriş` |
| `Text` | `p.Metin` |
| `Canvas` | `p.Tuval` |
| `Listbox` | `p.ListeKutusu` |
| `Scrollbar` | `p.KaydırmaÇubuğu` |
| `Scale` | `p.Ölçek` |
| `Checkbutton` | `p.OnayKutusu` |
| `Radiobutton` | `p.SeçenekDüğmesi` |
| `Spinbox` | `p.DöndürmeKutusu` |
| `Menu` | `p.Menü` |
| `Toplevel` | `p.ÜstPencere` |
| `LabelFrame` | `p.EtiketliÇerçeve` |
| `StringVar` | `p.DizgiDeğişkeni` |
| `IntVar` | `p.TamSayıDeğişkeni` |
| `DoubleVar` | `p.OndalıkDeğişkeni` |
| `BooleanVar` | `p.MantıksalDeğişkeni` |
| `mainloop` | `p.döngüyü_başlat` |
 
---
