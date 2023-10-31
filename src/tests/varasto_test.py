import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varastoon_menee_se_mita_mahtuu(self):
        self.varasto.lisaa_varastoon(20)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_varastosta_otetaan_enemman_varasto_ei_mene_pakkaselle(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_varastosta_otetaan_enemman_kun_on_varasto_antaa_kaiken_mita_on(self):
        self.varasto.lisaa_varastoon(5)
        saatu_maaara = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(saatu_maaara, 5)

    def test_ei_voi_luoda_negatiivista_varastoa(self):
        Negatiivinen_varasto = Varasto(-5.0)
        self.assertAlmostEqual(Negatiivinen_varasto.tilavuus, 0)

    def test_ei_voi_luoda_varastoa_liian_täydellä_alkusalolla(self):
        Negatiivinen_varasto = Varasto(5, 10)
        print(Negatiivinen_varasto)
        self.assertAlmostEqual(Negatiivinen_varasto.saldo, 5)

    def test_ei_voi_luoda_varastoa_negatiivisella_alkusalolla(self):
        Negatiivinen_varasto = Varasto(5, -10)
        self.assertAlmostEqual(Negatiivinen_varasto.saldo, 0)

    def test_ei_voi_ottaa_negatiivista_maaraa(self):
        self.varasto.ota_varastosta(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_ei_voi_lisata_negatiivista_maaraa(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_varaston_str_methodi_toimii(self):
        oikein = f"saldo = 0, vielä tilaa 10"
        tulostus = str(self.varasto)
        self.assertAlmostEqual(tulostus, oikein)
