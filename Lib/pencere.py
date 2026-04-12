# Hazer v0.5.0 — pencere (tkinter) wrapper modülü
from tkinter import *
from tkinter import (
    mainloop as döngüyü_başlat,
    getint as tam_sayı_al,
    getdouble as ondalık_al,
    getboolean as mantıksal_al,
    StringVar as DizgiDeğişkeni,
    IntVar as TamSayıDeğişkeni,
    DoubleVar as OndalıkDeğişkeni,
    BooleanVar as MantıksalDeğişkeni,
)

# ── Ortak widget metod mixin'i ──────────────────────────
class _TürkçeWidget:
    def paketle(self, **kwargs):       return self.pack(**kwargs)
    def izgara(self, **kwargs):        return self.grid(**kwargs)
    def yerleştir(self, **kwargs):     return self.place(**kwargs)
    def yok_et(self):                  return self.destroy()
    def yapılandır(self, **kwargs):    return self.config(**kwargs)
    def al(self, anahtar):             return self.cget(anahtar)
    def güncelle(self):                return self.update()
    def odaklan(self):                 return self.focus()
    def bağla(self, olay, callback):      return self.bind(olay, callback)
    def göster(self):                  return self.deiconify()
    def gizle(self):                   return self.withdraw()

# ── Pencere (Tk) ────────────────────────────────────────
class Pencere(_TürkçeWidget, Tk):
    def geometri(self, boyut=None):    return self.geometry(boyut)
    def başlık(self, metin=None):      return self.title(metin)
    def yeniden_boyutlandır(self, g, d): return self.resizable(g, d)
    def simge(self, dosya=None):       return self.iconphoto(True, PhotoImage(file=dosya)) if dosya else None
    def döngü(self):                   return self.mainloop()

# ── Çerçeve (Frame) ─────────────────────────────────────
class Çerçeve(_TürkçeWidget, Frame):
    pass

# ── Etiket (Label) ──────────────────────────────────────
class Etiket(_TürkçeWidget, Label):
    def metin_ayarla(self, metin):     return self.config(text=metin)
    def metin_al(self):                return self.cget("text")

# ── Düğme (Button) ──────────────────────────────────────
class Düğme(_TürkçeWidget, Button):
    def metin_ayarla(self, metin):     return self.config(text=metin)
    def etkinleştir(self):             return self.config(state=NORMAL)
    def devre_dışı(self):              return self.config(state=DISABLED)

# ── Giriş (Entry) ───────────────────────────────────────
class Giriş(_TürkçeWidget, Entry):
    def metin_al(self):                return self.get()
    def metin_ayarla(self, metin):
        self.delete(0, END)
        self.insert(0, metin)
    def temizle(self):                 return self.delete(0, END)
    def etkinleştir(self):             return self.config(state=NORMAL)
    def devre_dışı(self):              return self.config(state=DISABLED)

# ── Metin (Text) ────────────────────────────────────────
class Metin(_TürkçeWidget, Text):
    def metin_al(self):                return self.get("1.0", END)
    def metin_ekle(self, metin):       return self.insert(END, metin)
    def temizle(self):                 return self.delete("1.0", END)

# ── Tuval (Canvas) ──────────────────────────────────────
class Tuval(_TürkçeWidget, Canvas):
    def dikdörtgen(self, *args, **kwargs):  return self.create_rectangle(*args, **kwargs)
    def daire(self, *args, **kwargs):       return self.create_oval(*args, **kwargs)
    def çizgi(self, *args, **kwargs):       return self.create_line(*args, **kwargs)
    def yazı(self, *args, **kwargs):        return self.create_text(*args, **kwargs)
    def resim(self, *args, **kwargs):       return self.create_image(*args, **kwargs)
    def sil(self, *args):                   return self.delete(*args)

# ── ListeKutusu (Listbox) ───────────────────────────────
class ListeKutusu(_TürkçeWidget, Listbox):
    def ekle(self, *args):             return self.insert(END, *args)
    def sil(self, indeks):             return self.delete(indeks)
    def seçili_al(self):               return self.get(self.curselection())
    def temizle(self):                 return self.delete(0, END)

# ── KaydırmaÇubuğu (Scrollbar) ─────────────────────────
class KaydırmaÇubuğu(_TürkçeWidget, Scrollbar):
    pass

# ── Ölçek (Scale) ───────────────────────────────────────
class Ölçek(_TürkçeWidget, Scale):
    def değer_al(self):                return self.get()
    def değer_ayarla(self, değer):     return self.set(değer)

# ── OnayKutusu (Checkbutton) ────────────────────────────
class OnayKutusu(_TürkçeWidget, Checkbutton):
    def seç(self):                     return self.select()
    def kaldır(self):                  return self.deselect()

# ── SeçenekDüğmesi (Radiobutton) ────────────────────────
class SeçenekDüğmesi(_TürkçeWidget, Radiobutton):
    def seç(self):                     return self.select()

# ── DöndürmeKutusu (Spinbox) ────────────────────────────
class DöndürmeKutusu(_TürkçeWidget, Spinbox):
    def değer_al(self):                return self.get()

# ── Menü (Menu) ─────────────────────────────────────────
class Menü(_TürkçeWidget, Menu):
    def komut_ekle(self, **kwargs):    return self.add_command(**kwargs)
    def ayraç_ekle(self):              return self.add_separator()
    def alt_menü_ekle(self, **kwargs): return self.add_cascade(**kwargs)

# ── MenüDüğmesi (Menubutton) ────────────────────────────
class MenüDüğmesi(_TürkçeWidget, Menubutton):
    pass

# ── ÜstPencere (Toplevel) ───────────────────────────────
class ÜstPencere(_TürkçeWidget, Toplevel):
    def geometri(self, boyut=None):    return self.geometry(boyut)
    def başlık(self, metin=None):      return self.title(metin)

# ── EtiketliÇerçeve (LabelFrame) ────────────────────────
class EtiketliÇerçeve(_TürkçeWidget, LabelFrame):
    pass

# ── BölmePenceresi (PanedWindow) ────────────────────────
class BölmePenceresi(_TürkçeWidget, PanedWindow):
    def panel_ekle(self, widget, **kwargs): return self.add(widget, **kwargs)

# ── SeçenekMenüsü (OptionMenu) ──────────────────────────
class SeçenekMenüsü(_TürkçeWidget, OptionMenu):
    pass

# ── Mesaj (Message) ─────────────────────────────────────
class Mesaj(_TürkçeWidget, Message):
    pass
