# 🛠️ Key Transformations (V0.3.0)

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
| `import` | `temin` |

## Structural
| Standard Python | Custom Turkish Syntax |
| --- | --- |
| `:` | `ise` |

**Note: This is a clause terminator (used within if, for, def, etc.)**

## Compound Statements
| Standard Python | Custom Turkish Syntax |
| --- | --- |
| `with` | `birlikte` |
| `try` | `dene` |
| `if` | `eğer` |
| `else` | `değilse` |
| `while` | `iken` |
| `def` | `işlev` |
| `for` | `ozyinele` |
| `in(for)` | `içinde` |
| `match` | `eslestir` |
| `case` | `durum` |

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


## Standart Library
| Standard Python | Custom Turkish Syntax |
| --- | --- |
| `import math` | `temin matematik` |
| `import random` | `temin rastgele` |

---

# matematik (math) — Turkish Alias Proposals

## Constants
| math | matematik |
|------|-----------|
| `math.pi` | `matematik.pi` |
| `math.e` | `matematik.e` |
| `math.tau` | `matematik.tau` |
| `math.inf` | `matematik.sonsuz` |
| `math.nan` | `matematik.tanimsiz` |

## Rounding & Absolute Value
| math | matematik |
|------|-----------|
| `math.floor` | `matematik.taban` |
| `math.ceil` | `matematik.tavan` |
| `math.trunc` | `matematik.kirp` |
| `math.fabs` | `matematik.mutlak` |

## Power & Logarithm
| math | matematik |
|------|-----------|
| `math.sqrt` | `matematik.karekök` |
| `math.pow` | `matematik.üs` |
| `math.exp` | `matematik.üstel` |
| `math.log` | `matematik.logaritma` |
| `math.log2` | `matematik.log2` |
| `math.log10` | `matematik.log10` |

## Trigonometry
| math | matematik |
|------|-----------|
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

## Number Theory
| math | matematik |
|------|-----------|
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
| `math.ulp` | `matematik.ulp` |

---

# rastgele (random) Module

## Basic Functions
| Standard Python | Custom Turkish Syntax |
| --- | --- |
| `random.random` | `rastgele.sayi` |
| `random.randint` | `rastgele.tam_sayi` |
| `random.randrange` | `rastgele.aralik` |
| `random.uniform` | `rastgele.ondalik` |
| `random.randbytes` | `rastgele.bayt` |
| `random.getrandbits` | `rastgele.bit` |
| `random.triangular` | `rastgele.ucgen` |

## Collection Operations
| Standard Python | Custom Turkish Syntax |
| --- | --- |
| `random.choice` | `rastgele.sec` |
| `random.choices` | `rastgele.secimler` |
| `random.sample` | `rastgele.ornekle` |
| `random.shuffle` | `rastgele.karistir` |

## Situation Management
| Standard Python | Custom Turkish Syntax |
| --- | --- |
| `random.seed` | `rastgele.tohum` |
| `random.getstate` | `rastgele.durum_al` |
| `random.setstate` | `rastgele.durum_set` |

## Distribution Functions
| Standard Python | Custom Turkish Syntax |
| --- | --- |
| `random.gauss` | `rastgele.gauss` |
| `random.normalvariate` | `rastgele.normalvariate` |
| `random.lognormvariate` | `rastgele.lognormvariate` |
| `random.expovariate` | `rastgele.expovariate` |
| `random.gammavariate` | `rastgele.gammavariate` |
| `random.betavariate` | `rastgele.betavariate` |
| `random.paretovariate` | `rastgele.paretovariate` |
| `random.vonmisesvariate` | `rastgele.vonmisesvariate` |
| `random.weibullvariate` | `rastgele.weibullvariate` |

---