## **Turkish Based Custom Syntax Python Core - Hazer**

A deep-level modification of the **CPython (Python 3.15+)** core that enables writing Python code with Turkish-based syntax by modifying the language's internal grammar and parser mechanics.

---

## 🚀 Overview

This project is **not** a simple search and replace script. It involves direct intervention in Python's **PEG Parser**, **Lexer**, and **Grammar** layers. The language has been recompiled from C source code to recognize Turkish keywords at the engine level. It supports both the original English and the new Turkish syntax simultaneously (Bilingual) (for example, you can use ‘if’ and ‘eğer’ in the same file).
Furthermore, with version v0.2.0, it offers UTF-8 and Turkish syntax support.

---

## 🤔 What It Aims to Do

A linguistic experiment exploring the flexibility of Python's grammar layer.

---

## 📖 Language Reference

Review the [complete dictionary list](./SYNTAX.md) for all Turkish keywords, list methods, and type conversions available in Hazer v0.2.0.

---

## 💻 Code Example

Behold, the new syntax in action (completely valid in this core):

```python
islev kontrol_et(sayi) ise
    # logic and 'return' test
    eger sayi > 0 ve degil sayi == 10 ise
        dondur "Gecerli"
    elif sayi == 10 ise
        dondur "Tam On"
    degilse ise
        dondur "Gecersiz"

# 'for' and 'in' test
liste = [2, 5, 10, -3]

ozyinele eleman icinde liste ise
    sonuc = kontrol_et(eleman)
    yazdir(f"Sayi: {eleman} -> Durum: {sonuc}")

```

---

## ⚙️ Technical Implementation

1. **Grammar Overhaul:** Modified `Grammar/python.gram` to introduce new rules for compound statements using the `('keyword' | 'yeni_kelime')` pattern.
2. **Parser Generation:** Integrated with Python's modern **PEG Parser**. Used `make regen-pegen` to re-generate `Parser/parser.c`.
3. **Keyword Recognition:** Updated the internal keyword mapping to ensure new terms are treated as first-class citizens (Lexical Analysis).
4. **Hardware:** Successfully built and tested on **Raspberry Pi (ARM64)** architecture.
5. **Source:** Built on the bleeding-edge CPython 3.15-dev branch to leverage the latest PEG parser optimizations.

---

## 🌐 Check Out the Website

For comprehensive documentation regarding the modified grammar and core functions, visit the official wiki: https://hazer.comblaster.net/

---

## 📁 Native `.hazer` Support

Hazer recognizes its own identity. You can execute files using the `.hazer` extension natively. This isn't just a file rename; the core is configured to treat `.hazer` files as first-class source units, equivalent to `.py` but symbolically representing the new syntax.

---

## 🏗️ How to Build

**Note: To build this project, gcc, make, and Python 3.x must be installed on your device.**

To build this custom core on your local machine:

1. **Clone the repository:**
```bash
git clone https://github.com/c0mblasterR/custom-syntax-python
cd custom-syntax-python

```


2. **Configure and Prepare:**
```bash
./configure
make regen-pegen  # Mandatory to apply grammar changes!

```


3. **Compile:**
```bash
make -j$(nproc)

```


4. **Launch:**
```bash
./python

```

---

## 📌 Important Note for Contributing

External Pull Requests (PRs) will not be accepted until the project reaches version 1.0.0. However, feel free to open Issues for bug reports or syntax suggestions. Thank you for your interest.

---

## 📜 License
- [![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](./LICENSE-AGPLV3.md)
- [![License: PSFL](https://img.shields.io/badge/License-PSF-blue.svg)](./LICENSE)
- This project is licensed under **AGPLv3**. (Note: Original CPython source files maintain their respective PSFL history where applicable.)

---