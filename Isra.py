import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class IsraelCommuneFinanceAnalyzer:
    def __init__(self, commune_name):
        self.commune = commune_name
        self.colors = ['#0055A4', '#F7E400', '#D21034', '#00A859', '#FF6B6B', 
                      '#4ECDC4', '#45B7D1', '#F9A602', '#6A0572', '#AB83A1']
        
        self.start_year = 2002
        self.end_year = 2025
        
        # Conversion shekel (1€ ≈ 4 shekels environ)
        self.eur_to_ils = 4.0
        
        # Configuration spécifique à chaque commune israélienne
        self.config = self._get_commune_config()
        
    def _get_commune_config(self):
        """Retourne la configuration spécifique pour chaque commune israélienne"""
        configs = {
            "Jérusalem": {
                "population_base": 950000,
                "budget_base": 8500,  # en millions de shekels
                "type": "capitale",
                "specialites": ["tourisme", "administration", "education", "culture", "religion"]
            },
            "Tel Aviv-Jaffa": {
                "population_base": 460000,
                "budget_base": 12000,
                "type": "metropolitaine",
                "specialites": ["finance", "technologie", "commerce", "tourisme", "culture"]
            },
            "Haïfa": {
                "population_base": 285000,
                "budget_base": 4800,
                "type": "portuaire",
                "specialites": ["port", "industrie", "technologie", "education", "tourisme"]
            },
            "Beer-Sheva": {
                "population_base": 220000,
                "budget_base": 3200,
                "type": "regionale",
                "specialites": ["desert", "technologie", "sante", "education", "cybersecurite"]
            },
            "Netanya": {
                "population_base": 220000,
                "budget_base": 2800,
                "type": "cotiere",
                "specialites": ["tourisme", "immobilier", "commerce", "diamants"]
            },
            "Ashdod": {
                "population_base": 225000,
                "budget_base": 3500,
                "type": "portuaire",
                "specialites": ["port", "industrie", "commerce", "logistique"]
            },
            "Rishon LeZion": {
                "population_base": 255000,
                "budget_base": 3800,
                "type": "banlieue",
                "specialites": ["vin", "commerce", "education", "services"]
            },
            "Petah Tikva": {
                "population_base": 250000,
                "budget_base": 3600,
                "type": "industrielle",
                "specialites": ["industrie", "sante", "technologie", "agriculture"]
            },
            "Eilat": {
                "population_base": 52000,
                "budget_base": 1800,
                "type": "touristique",
                "specialites": ["tourisme", "plongee", "commerce_libre", "loisirs"]
            },
            "Tiberiade": {
                "population_base": 44000,
                "budget_base": 850,
                "type": "touristique",
                "specialites": ["lac", "tourisme_religieux", "thermal", "histoire"]
            },
            "Nahariya": {
                "population_base": 58000,
                "budget_base": 950,
                "type": "cotiere",
                "specialites": ["tourisme", "agriculture", "commerce_frontalier"]
            },
            "Safed": {
                "population_base": 37000,
                "budget_base": 680,
                "type": "religieuse",
                "specialites": ["kabbalah", "art", "tourisme_religieux", "histoire"]
            },
            # Configuration par défaut
            "default": {
                "population_base": 50000,
                "budget_base": 800,
                "type": "locale",
                "specialites": ["commerce_local", "services", "education", "sante"]
            }
        }
        
        return configs.get(self.commune, configs["default"])
    
    def _convert_to_shekels(self, amount_eur):
        """Convertit un montant d'euros en shekels"""
        return amount_eur * self.eur_to_ils
    
    def generate_financial_data(self):
        """Génère des données financières pour la commune israélienne"""
        print(f"🏛️ Génération des données financières pour {self.commune} (Israël)...")
        
        # Créer une base de données annuelle
        dates = pd.date_range(start=f'{self.start_year}-01-01', 
                             end=f'{self.end_year}-12-31', freq='Y')
        
        data = {'Annee': [date.year for date in dates]}
        
        # Données démographiques (croissance israélienne typique)
        data['Population'] = self._simulate_population(dates)
        data['Menages'] = self._simulate_households(dates)
        
        # Recettes communales en shekels
        data['Recettes_Totales'] = self._simulate_total_revenue(dates)
        data['Impots_Locaux'] = self._simulate_tax_revenue(dates)
        data['Subventions_Gouvernement'] = self._simulate_government_grants(dates)
        data['Autres_Recettes'] = self._simulate_other_revenue(dates)
        
        # Dépenses communales en shekels
        data['Depenses_Totales'] = self._simulate_total_expenses(dates)
        data['Fonctionnement'] = self._simulate_operating_expenses(dates)
        data['Investissement'] = self._simulate_investment_expenses(dates)
        data['Charge_Dette'] = self._simulate_debt_charges(dates)
        data['Personnel'] = self._simulate_staff_costs(dates)
        
        # Indicateurs financiers
        data['Epargne_Brute'] = self._simulate_gross_savings(dates)
        data['Dette_Totale'] = self._simulate_total_debt(dates)
        data['Taux_Endettement'] = self._simulate_debt_ratio(dates)
        data['Taux_Fiscalite'] = self._simulate_tax_rate(dates)
        
        # Investissements spécifiques adaptés à Israël
        data['Investissement_Technologie'] = self._simulate_technology_investment(dates)
        data['Investissement_Tourisme'] = self._simulate_tourism_investment(dates)
        data['Investissement_Transport'] = self._simulate_transport_investment(dates)
        data['Investissement_Education'] = self._simulate_education_investment(dates)
        data['Investissement_Securite'] = self._simulate_security_investment(dates)
        data['Investissement_Environnement'] = self._simulate_environment_investment(dates)
        data['Investissement_Culture'] = self._simulate_culture_investment(dates)
        
        df = pd.DataFrame(data)
        
        # Ajouter des tendances spécifiques à la commune israélienne
        self._add_israeli_trends(df)
        
        return df
    
    def _simulate_population(self, dates):
        """Simule la population de la commune (croissance israélienne typique)"""
        base_population = self.config["population_base"]
        
        population = []
        for i, date in enumerate(dates):
            # Croissance démographique israélienne (relativement forte)
            if self.config["type"] == "capitale":
                growth_rate = 0.018  # Croissance modérée à Jérusalem
            elif self.config["type"] == "metropolitaine":
                growth_rate = 0.022  # Croissance forte à Tel Aviv
            elif self.config["type"] == "touristique":
                growth_rate = 0.025  # Croissance très forte dans les villes touristiques
            else:
                growth_rate = 0.020  # Croissance moyenne
                
            growth = 1 + growth_rate * i
            population.append(base_population * growth)
        
        return population
    
    def _simulate_households(self, dates):
        """Simule le nombre de ménages (taille moyenne plus petite en Israël)"""
        base_households = self.config["population_base"] / 3.0  # Taille des ménages plus petite
        
        households = []
        for i, date in enumerate(dates):
            growth = 1 + 0.018 * i
            households.append(base_households * growth)
        
        return households
    
    def _simulate_total_revenue(self, dates):
        """Simule les recettes totales de la commune en shekels"""
        base_revenue = self._convert_to_shekels(self.config["budget_base"])
        
        revenue = []
        for i, date in enumerate(dates):
            # Croissance économique israélienne (solide)
            if self.config["type"] == "metropolitaine":
                growth_rate = 0.038  # Croissance forte dans les zones économiques
            elif self.config["type"] == "technologie":
                growth_rate = 0.042  # Croissance très forte dans la tech
            else:
                growth_rate = 0.035  # Croissance moyenne
                
            growth = 1 + growth_rate * i
            noise = np.random.normal(1, 0.07)
            revenue.append(base_revenue * growth * noise)
        
        return revenue
    
    def _simulate_tax_revenue(self, dates):
        """Simule les recettes fiscales en shekels"""
        base_tax = self._convert_to_shekels(self.config["budget_base"] * 0.40)
        
        tax_revenue = []
        for i, date in enumerate(dates):
            growth = 1 + 0.032 * i
            noise = np.random.normal(1, 0.08)
            tax_revenue.append(base_tax * growth * noise)
        
        return tax_revenue
    
    def _simulate_government_grants(self, dates):
        """Simule les subventions gouvernementales (moins importantes qu'en Guyane)"""
        base_grants = self._convert_to_shekels(self.config["budget_base"] * 0.35)
        
        grants = []
        for i, date in enumerate(dates):
            year = date.year
            # Augmentation modérée des subventions
            if year >= 2010:
                increase = 1 + 0.008 * (year - 2010)
            else:
                increase = 1
            
            noise = np.random.normal(1, 0.05)
            grants.append(base_grants * increase * noise)
        
        return grants
    
    def _simulate_other_revenue(self, dates):
        """Simule les autres recettes en shekels"""
        base_other = self._convert_to_shekels(self.config["budget_base"] * 0.25)
        
        other_revenue = []
        for i, date in enumerate(dates):
            growth = 1 + 0.028 * i
            noise = np.random.normal(1, 0.09)
            other_revenue.append(base_other * growth * noise)
        
        return other_revenue
    
    def _simulate_total_expenses(self, dates):
        """Simule les dépenses totales en shekels"""
        base_expenses = self._convert_to_shekels(self.config["budget_base"] * 0.96)
        
        expenses = []
        for i, date in enumerate(dates):
            growth = 1 + 0.034 * i
            noise = np.random.normal(1, 0.06)
            expenses.append(base_expenses * growth * noise)
        
        return expenses
    
    def _simulate_operating_expenses(self, dates):
        """Simule les dépenses de fonctionnement en shekels"""
        base_operating = self._convert_to_shekels(self.config["budget_base"] * 0.60)
        
        operating = []
        for i, date in enumerate(dates):
            growth = 1 + 0.030 * i
            noise = np.random.normal(1, 0.05)
            operating.append(base_operating * growth * noise)
        
        return operating
    
    def _simulate_investment_expenses(self, dates):
        """Simule les dépenses d'investissement en shekels"""
        base_investment = self._convert_to_shekels(self.config["budget_base"] * 0.36)
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            # Plans d'investissement spécifiques à Israël
            if year in [2006, 2012, 2018, 2023]:
                multiplier = 1.6
            elif year in [2008, 2014, 2020]:
                multiplier = 0.8
            else:
                multiplier = 1.0
            
            growth = 1 + 0.028 * i
            noise = np.random.normal(1, 0.15)
            investment.append(base_investment * growth * multiplier * noise)
        
        return investment
    
    def _simulate_debt_charges(self, dates):
        """Simule les charges de la dette en shekels"""
        base_debt_charge = self._convert_to_shekels(self.config["budget_base"] * 0.06)
        
        debt_charges = []
        for i, date in enumerate(dates):
            year = date.year
            if year >= 2005:
                increase = 1 + 0.008 * (year - 2005)
            else:
                increase = 1
            
            noise = np.random.normal(1, 0.09)
            debt_charges.append(base_debt_charge * increase * noise)
        
        return debt_charges
    
    def _simulate_staff_costs(self, dates):
        """Simule les dépenses de personnel en shekels"""
        base_staff = self._convert_to_shekels(self.config["budget_base"] * 0.42)
        
        staff_costs = []
        for i, date in enumerate(dates):
            growth = 1 + 0.031 * i
            noise = np.random.normal(1, 0.04)
            staff_costs.append(base_staff * growth * noise)
        
        return staff_costs
    
    def _simulate_gross_savings(self, dates):
        """Simule l'épargne brute en shekels"""
        savings = []
        for i, date in enumerate(dates):
            base_saving = self._convert_to_shekels(self.config["budget_base"] * 0.04)
            
            year = date.year
            if year >= 2010:
                improvement = 1 + 0.010 * (year - 2010)
            else:
                improvement = 1
            
            noise = np.random.normal(1, 0.12)
            savings.append(base_saving * improvement * noise)
        
        return savings
    
    def _simulate_total_debt(self, dates):
        """Simule la dette totale en shekels"""
        base_debt = self._convert_to_shekels(self.config["budget_base"] * 0.75)
        
        debt = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2006, 2012, 2018, 2023]:
                change = 1.20
            elif year in [2008, 2014, 2020]:
                change = 0.88
            else:
                change = 1.0
            
            noise = np.random.normal(1, 0.08)
            debt.append(base_debt * change * noise)
        
        return debt
    
    def _simulate_debt_ratio(self, dates):
        """Simule le taux d'endettement"""
        ratios = []
        for i, date in enumerate(dates):
            base_ratio = 0.65  # Endettement initial plus modéré
            
            year = date.year
            if year >= 2010:
                improvement = 1 - 0.012 * (year - 2010)  # Amélioration plus rapide
            else:
                improvement = 1
            
            noise = np.random.normal(1, 0.06)
            ratios.append(base_ratio * improvement * noise)
        
        return ratios
    
    def _simulate_tax_rate(self, dates):
        """Simule le taux de fiscalité (moyen)"""
        rates = []
        for i, date in enumerate(dates):
            base_rate = 0.92  # Fiscalité initiale plus élevée
            
            year = date.year
            if year >= 2010:
                increase = 1 + 0.006 * (year - 2010)
            else:
                increase = 1
            
            noise = np.random.normal(1, 0.03)
            rates.append(base_rate * increase * noise)
        
        return rates
    
    def _simulate_technology_investment(self, dates):
        """Simule l'investissement technologique (spécifique à Israël)"""
        base_investment = self._convert_to_shekels(self.config["budget_base"] * 0.08)
        
        # Ajustement selon les spécialités
        multiplier = 1.8 if "technologie" in self.config["specialites"] else 0.7
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2005, 2010, 2015, 2020]:
                year_multiplier = 2.2  # Plans d'investissement technologique importants
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.045 * i  # Croissance très forte
            noise = np.random.normal(1, 0.18)
            investment.append(base_investment * growth * year_multiplier * multiplier * noise)
        
        return investment
    
    def _simulate_tourism_investment(self, dates):
        """Simule l'investissement touristique"""
        base_investment = self._convert_to_shekels(self.config["budget_base"] * 0.06)
        
        # Ajustement selon les spécialités
        multiplier = 1.7 if "tourisme" in self.config["specialites"] else 0.8
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2007, 2013, 2019, 2024]:
                year_multiplier = 1.8
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.035 * i
            noise = np.random.normal(1, 0.16)
            investment.append(base_investment * growth * year_multiplier * multiplier * noise)
        
        return investment
    
    def _simulate_transport_investment(self, dates):
        """Simule l'investissement en transport"""
        base_investment = self._convert_to_shekels(self.config["budget_base"] * 0.05)
        
        # Ajustement selon les spécialités
        multiplier = 1.4 if "transport" in self.config["specialites"] else 1.0
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2006, 2012, 2018, 2023]:
                year_multiplier = 1.7
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.032 * i
            noise = np.random.normal(1, 0.15)
            investment.append(base_investment * growth * year_multiplier * multiplier * noise)
        
        return investment
    
    def _simulate_education_investment(self, dates):
        """Simule l'investissement éducatif"""
        base_investment = self._convert_to_shekels(self.config["budget_base"] * 0.07)
        
        # Ajustement selon les spécialités
        multiplier = 1.5 if "education" in self.config["specialites"] else 1.0
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2008, 2014, 2020]:
                year_multiplier = 1.6
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.030 * i
            noise = np.random.normal(1, 0.14)
            investment.append(base_investment * growth * year_multiplier * multiplier * noise)
        
        return investment
    
    def _simulate_security_investment(self, dates):
        """Simule l'investissement en sécurité (spécifique à Israël)"""
        base_investment = self._convert_to_shekels(self.config["budget_base"] * 0.04)
        
        # Ajustement selon les spécialités et la localisation
        if "frontaliere" in self.config["specialites"] or self.config["type"] in ["capitale", "metropolitaine"]:
            multiplier = 1.6
        else:
            multiplier = 1.0
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            # Augmentation pendant les périodes de tension
            if year in [2002, 2006, 2009, 2014, 2021]:
                year_multiplier = 2.0
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.025 * i
            noise = np.random.normal(1, 0.20)  # Forte volatilité
            investment.append(base_investment * growth * year_multiplier * multiplier * noise)
        
        return investment
    
    def _simulate_environment_investment(self, dates):
        """Simule l'investissement environnemental"""
        base_investment = self._convert_to_shekels(self.config["budget_base"] * 0.03)
        
        # Ajustement selon les spécialités
        multiplier = 1.4 if "environnement" in self.config["specialites"] else 0.9
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2009, 2015, 2021]:
                year_multiplier = 1.8
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.028 * i
            noise = np.random.normal(1, 0.16)
            investment.append(base_investment * growth * year_multiplier * multiplier * noise)
        
        return investment
    
    def _simulate_culture_investment(self, dates):
        """Simule l'investissement culturel"""
        base_investment = self._convert_to_shekels(self.config["budget_base"] * 0.02)
        
        # Ajustement selon les spécialités
        multiplier = 1.7 if "culture" in self.config["specialites"] else 0.8
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2010, 2016, 2022]:
                year_multiplier = 1.9
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.025 * i
            noise = np.random.normal(1, 0.15)
            investment.append(base_investment * growth * year_multiplier * multiplier * noise)
        
        return investment
    
    def _add_israeli_trends(self, df):
        """Ajoute des tendances municipales réalistes adaptées à Israël"""
        for i, row in df.iterrows():
            year = row['Annee']
            
            # Seconde Intifada (2000-2005) - impact économique
            if 2002 <= year <= 2005:
                df.loc[i, 'Investissement_Tourisme'] *= 0.7
                df.loc[i, 'Recettes_Totales'] *= 0.95
            
            # Boom technologique israélien (2006-2008)
            if 2006 <= year <= 2008:
                df.loc[i, 'Investissement_Technologie'] *= 1.6
                df.loc[i, 'Recettes_Totales'] *= 1.08
            
            # Impact de la crise financière mondiale (2008-2009)
            if 2008 <= year <= 2009:
                df.loc[i, 'Recettes_Totales'] *= 0.92
                df.loc[i, 'Investissement'] *= 0.78
            
            # Croissance économique forte (2010-2019)
            elif 2010 <= year <= 2019:
                df.loc[i, 'Investissement_Technologie'] *= 1.2
                df.loc[i, 'Subventions_Gouvernement'] *= 1.05
            
            # Opérations militaires importantes (2014)
            if year == 2014:
                df.loc[i, 'Investissement_Securite'] *= 2.5
                df.loc[i, 'Depenses_Totales'] *= 1.08
            
            # Impact de la crise COVID-19 (2020-2021)
            if 2020 <= year <= 2021:
                if year == 2020:
                    df.loc[i, 'Recettes_Totales'] *= 0.85
                    df.loc[i, 'Investissement_Tourisme'] *= 0.6
                else:
                    df.loc[i, 'Subventions_Gouvernement'] *= 1.15
            
            # Plan de relance post-COVID (2022-2025)
            if year >= 2022:
                df.loc[i, 'Investissement_Technologie'] *= 1.25
                df.loc[i, 'Investissement_Transport'] *= 1.15
                df.loc[i, 'Investissement_Environnement'] *= 1.20
    
    def create_financial_analysis(self, df):
        """Crée une analyse complète des finances communales israéliennes"""
        plt.style.use('seaborn-v0_8')
        fig = plt.figure(figsize=(20, 24))
        
        # 1. Évolution des recettes et dépenses
        ax1 = plt.subplot(4, 2, 1)
        self._plot_revenue_expenses(df, ax1)
        
        # 2. Structure des recettes
        ax2 = plt.subplot(4, 2, 2)
        self._plot_revenue_structure(df, ax2)
        
        # 3. Structure des dépenses
        ax3 = plt.subplot(4, 2, 3)
        self._plot_expenses_structure(df, ax3)
        
        # 4. Investissements communaux
        ax4 = plt.subplot(4, 2, 4)
        self._plot_investments(df, ax4)
        
        # 5. Dette et endettement
        ax5 = plt.subplot(4, 2, 5)
        self._plot_debt(df, ax5)
        
        # 6. Indicateurs de performance
        ax6 = plt.subplot(4, 2, 6)
        self._plot_performance_indicators(df, ax6)
        
        # 7. Démographie
        ax7 = plt.subplot(4, 2, 7)
        self._plot_demography(df, ax7)
        
        # 8. Investissements sectoriels
        ax8 = plt.subplot(4, 2, 8)
        self._plot_sectorial_investments(df, ax8)
        
        plt.suptitle(f'Analyse des Comptes Communaux de {self.commune} - Israël ({self.start_year}-{self.end_year})\n(En millions de shekels)', 
                    fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(f'{self.commune}_financial_analysis_Israel.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Générer les insights
        self._generate_financial_insights(df)
    
    def _plot_revenue_expenses(self, df, ax):
        """Plot de l'évolution des recettes et dépenses"""
        ax.plot(df['Annee'], df['Recettes_Totales'], label='Recettes Totales', 
               linewidth=2, color='#0055A4', alpha=0.8)
        ax.plot(df['Annee'], df['Depenses_Totales'], label='Dépenses Totales', 
               linewidth=2, color='#D21034', alpha=0.8)
        
        ax.set_title('Évolution des Recettes et Dépenses (millions de shekels)', 
                    fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (millions ₪)')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _plot_revenue_structure(self, df, ax):
        """Plot de la structure des recettes"""
        years = df['Annee']
        width = 0.8
        
        bottom = np.zeros(len(years))
        categories = ['Impots_Locaux', 'Subventions_Gouvernement', 'Autres_Recettes']
        colors = ['#0055A4', '#F7E400', '#D21034']
        labels = ['Impôts Locaux', 'Subventions Gouvernement', 'Autres Recettes']
        
        for i, category in enumerate(categories):
            ax.bar(years, df[category], width, label=labels[i], bottom=bottom, color=colors[i])
            bottom += df[category]
        
        ax.set_title('Structure des Recettes (millions de shekels)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (millions ₪)')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    def _plot_expenses_structure(self, df, ax):
        """Plot de la structure des dépenses"""
        years = df['Annee']
        width = 0.8
        
        bottom = np.zeros(len(years))
        categories = ['Fonctionnement', 'Investissement', 'Charge_Dette', 'Personnel']
        colors = ['#0055A4', '#F7E400', '#D21034', '#00A859']
        labels = ['Fonctionnement', 'Investissement', 'Charge Dette', 'Personnel']
        
        for i, category in enumerate(categories):
            ax.bar(years, df[category], width, label=labels[i], bottom=bottom, color=colors[i])
            bottom += df[category]
        
        ax.set_title('Structure des Dépenses (millions de shekels)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (millions ₪)')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    def _plot_investments(self, df, ax):
        """Plot des investissements communaux"""
        ax.plot(df['Annee'], df['Investissement_Technologie'], label='Technologie', 
               linewidth=2, color='#0055A4', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Tourisme'], label='Tourisme', 
               linewidth=2, color='#F7E400', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Transport'], label='Transport', 
               linewidth=2, color='#D21034', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Education'], label='Éducation', 
               linewidth=2, color='#00A859', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Securite'], label='Sécurité', 
               linewidth=2, color='#6A0572', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Environnement'], label='Environnement', 
               linewidth=2, color='#45B7D1', alpha=0.8)
        
        ax.set_title('Répartition des Investissements (millions de shekels)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (millions ₪)')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _plot_debt(self, df, ax):
        """Plot de la dette et du taux d'endettement"""
        # Dette totale
        ax.bar(df['Annee'], df['Dette_Totale'], label='Dette Totale (millions ₪)', 
              color='#0055A4', alpha=0.7)
        
        ax.set_title('Dette Communale et Taux d\'Endettement', fontsize=12, fontweight='bold')
        ax.set_ylabel('Dette (millions ₪)', color='#0055A4')
        ax.tick_params(axis='y', labelcolor='#0055A4')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Taux d'endettement en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Taux_Endettement'], label='Taux d\'Endettement', 
                linewidth=3, color='#D21034')
        ax2.set_ylabel('Taux d\'Endettement', color='#D21034')
        ax2.tick_params(axis='y', labelcolor='#D21034')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _plot_performance_indicators(self, df, ax):
        """Plot des indicateurs de performance"""
        # Épargne brute
        ax.bar(df['Annee'], df['Epargne_Brute'], label='Épargne Brute (millions ₪)', 
              color='#00A859', alpha=0.7)
        
        ax.set_title('Indicateurs de Performance', fontsize=12, fontweight='bold')
        ax.set_ylabel('Épargne Brute (millions ₪)', color='#00A859')
        ax.tick_params(axis='y', labelcolor='#00A859')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Taux de fiscalité en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Taux_Fiscalite'], label='Taux de Fiscalité', 
                linewidth=3, color='#F9A602')
        ax2.set_ylabel('Taux de Fiscalité', color='#F9A602')
        ax2.tick_params(axis='y', labelcolor='#F9A602')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _plot_demography(self, df, ax):
        """Plot de l'évolution démographique"""
        ax.plot(df['Annee'], df['Population'], label='Population', 
               linewidth=2, color='#0055A4', alpha=0.8)
        
        ax.set_title('Évolution Démographique', fontsize=12, fontweight='bold')
        ax.set_ylabel('Population', color='#0055A4')
        ax.tick_params(axis='y', labelcolor='#0055A4')
        ax.grid(True, alpha=0.3)
        
        # Nombre de ménages en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Menages'], label='Ménages', 
                linewidth=2, color='#D21034', alpha=0.8)
        ax2.set_ylabel('Ménages', color='#D21034')
        ax2.tick_params(axis='y', labelcolor='#D21034')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _plot_sectorial_investments(self, df, ax):
        """Plot des investissements sectoriels"""
        years = df['Annee']
        width = 0.8
        
        bottom = np.zeros(len(years))
        categories = ['Investissement_Technologie', 'Investissement_Tourisme', 
                     'Investissement_Transport', 'Investissement_Education', 
                     'Investissement_Securite', 'Investissement_Environnement']
        
        colors = ['#0055A4', '#F7E400', '#D21034', '#00A859', '#6A0572', '#45B7D1']
        labels = ['Technologie', 'Tourisme', 'Transport', 'Éducation', 'Sécurité', 'Environnement']
        
        for i, category in enumerate(categories):
            ax.bar(years, df[category], width, label=labels[i], bottom=bottom, color=colors[i])
            bottom += df[category]
        
        ax.set_title('Répartition Sectorielle des Investissements (millions de shekels)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (millions ₪)')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    def _generate_financial_insights(self, df):
        """Génère des insights analytiques adaptés à Israël"""
        print(f"🏛️ INSIGHTS ANALYTIQUES - Commune de {self.commune} (Israël)")
        print("=" * 60)
        
        # 1. Statistiques de base
        print("\n1. 📈 STATISTIQUES GÉNÉRALES:")
        avg_revenue = df['Recettes_Totales'].mean()
        avg_expenses = df['Depenses_Totales'].mean()
        avg_savings = df['Epargne_Brute'].mean()
        avg_debt = df['Dette_Totale'].mean()
        
        print(f"Recettes moyennes annuelles: {avg_revenue:.2f} millions de shekels")
        print(f"Dépenses moyennes annuelles: {avg_expenses:.2f} millions de shekels")
        print(f"Épargne brute moyenne: {avg_savings:.2f} millions de shekels")
        print(f"Dette moyenne: {avg_debt:.2f} millions de shekels")
        
        # 2. Croissance
        print("\n2. 📊 TAUX DE CROISSANCE:")
        revenue_growth = ((df['Recettes_Totales'].iloc[-1] / 
                          df['Recettes_Totales'].iloc[0]) - 1) * 100
        population_growth = ((df['Population'].iloc[-1] / 
                             df['Population'].iloc[0]) - 1) * 100
        
        print(f"Croissance des recettes ({self.start_year}-{self.end_year}): {revenue_growth:.1f}%")
        print(f"Croissance de la population ({self.start_year}-{self.end_year}): {population_growth:.1f}%")
        
        # 3. Structure financière
        print("\n3. 📋 STRUCTURE FINANCIÈRE:")
        tax_share = (df['Impots_Locaux'].mean() / df['Recettes_Totales'].mean()) * 100
        gov_share = (df['Subventions_Gouvernement'].mean() / df['Recettes_Totales'].mean()) * 100
        investment_share = (df['Investissement'].mean() / df['Depenses_Totales'].mean()) * 100
        
        print(f"Part des impôts locaux dans les recettes: {tax_share:.1f}%")
        print(f"Part des subventions gouvernementales dans les recettes: {gov_share:.1f}%")
        print(f"Part de l'investissement dans les dépenses: {investment_share:.1f}%")
        
        # 4. Dette et fiscalité
        print("\n4. 💰 ENDETTEMENT ET FISCALITÉ:")
        avg_debt_ratio = df['Taux_Endettement'].mean() * 100
        avg_tax_rate = df['Taux_Fiscalite'].mean()
        last_debt_ratio = df['Taux_Endettement'].iloc[-1] * 100
        
        print(f"Taux d'endettement moyen: {avg_debt_ratio:.1f}%")
        print(f"Taux d'endettement final: {last_debt_ratio:.1f}%")
        print(f"Taux de fiscalité moyen: {avg_tax_rate:.2f}")
        
        # 5. Spécificités de la commune israélienne
        print(f"\n5. 🌟 SPÉCIFICITÉS DE {self.commune.upper()} (ISRAËL):")
        print(f"Type de commune: {self.config['type']}")
        print(f"Spécialités: {', '.join(self.config['specialites'])}")
        
        # 6. Événements marquants spécifiques à Israël
        print("\n6. 📅 ÉVÉNEMENTS MARQUANTS ISRAËL:")
        print("• 2002-2005: Période de la Seconde Intifada (impact économique)")
        print("• 2006-2008: Boom technologique et croissance économique")
        print("• 2008-2009: Crise financière mondiale")
        print("• 2010-2019: Croissance économique soutenue")
        print("• 2014: Opération militaire à Gaza (impact sécuritaire)")
        print("• 2020-2021: Crise COVID-19 et plans de soutien")
        print("• 2022-2025: Plan de relance post-COVID et développement technologique")
        
        # 7. Recommandations adaptées à Israël
        print("\n7. 💡 RECOMMANDATIONS STRATÉGIQUES:")
        if "technologie" in self.config["specialites"]:
            print("• Développer les parcs technologiques et les startups")
            print("• Attirer les investissements étrangers dans la high-tech")
        if "tourisme" in self.config["specialites"]:
            print("• Promouvoir le tourisme religieux, balnéaire et culturel")
            print("• Développer les infrastructures d'accueil internationales")
        if "sécurité" in self.config["specialites"] or self.config["type"] in ["capitale", "frontaliere"]:
            print("• Moderniser les infrastructures de sécurité")
            print("• Développer les systèmes de protection civile")
        print("• Investir dans les technologies vertes et durables")
        print("• Renforcer les partenariats universités-entreprises")
        print("• Développer les transports publics intelligents")
        print("• Promouvoir l'innovation dans l'agriculture et l'eau")

def main():
    """Fonction principale pour Israël"""
    # Liste des communes israéliennes
    communes = [
        "Jérusalem", "Tel Aviv-Jaffa", "Haïfa", "Beer-Sheva", "Netanya",
        "Ashdod", "Rishon LeZion", "Petah Tikva", "Eilat", "Tiberiade",
        "Nahariya", "Safed", "Herzliya", "Ramla", "Lod", "Modiin",
        "Kfar Saba", "Ra'anana", "Hadera", "Ashkelon", "Bat Yam", "Holon"
    ]
    
    print("🏛️ ANALYSE DES COMPTES COMMUNAUX D'ISRAËL (2002-2025)")
    print("=" * 60)
    print("💰 Devise: Shekel israélien (₪) - 1€ ≈ 4₪")
    print("=" * 60)
    
    # Demander à l'utilisateur de choisir une commune
    print("Liste des communes disponibles:")
    for i, commune in enumerate(communes, 1):
        print(f"{i}. {commune}")
    
    try:
        choix = int(input("\nChoisissez le numéro de la commune à analyser: "))
        if choix < 1 or choix > len(communes):
            raise ValueError
        commune_selectionnee = communes[choix-1]
    except (ValueError, IndexError):
        print("Choix invalide. Sélection de Tel Aviv-Jaffa par défaut.")
        commune_selectionnee = "Tel Aviv-Jaffa"
    
    # Initialiser l'analyseur
    analyzer = IsraelCommuneFinanceAnalyzer(commune_selectionnee)
    
    # Générer les données
    financial_data = analyzer.generate_financial_data()
    
    # Sauvegarder les données
    output_file = f'{commune_selectionnee}_financial_data_Israel_2002_2025.csv'
    financial_data.to_csv(output_file, index=False)
    print(f"💾 Données sauvegardées: {output_file}")
    
    # Aperçu des données
    print("\n👀 Aperçu des données (en millions de shekels):")
    print(financial_data[['Annee', 'Population', 'Recettes_Totales', 'Depenses_Totales', 'Dette_Totale']].head())
    
    # Créer l'analyse
    print("\n📈 Création de l'analyse financière...")
    analyzer.create_financial_analysis(financial_data)
    
    print(f"\n✅ Analyse des comptes communaux de {commune_selectionnee} terminée!")
    print(f"📊 Période: {analyzer.start_year}-{analyzer.end_year}")
    print("💰 Devise: Shekel israélien (₪)")
    print("📦 Données: Démographie, finances, investissements, dette")

if __name__ == "__main__":
    main()