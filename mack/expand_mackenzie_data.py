import json

# Load existing data
with open('/home/captainanime/mackenzie_scott_comprehensive.json', 'r') as f:
    data = json.load(f)

# Add more detailed information from additional sources
expanded_data = data.copy()

# Add information about controversies and news coverage
expanded_data["controversies_and_criticism"].extend([
    {
        "issue": "Amazon labor practices criticism",
        "context": "Some critics note Mackenzie Scott accumulated wealth from Amazon, which has faced labor rights criticism",
        "source_url": "Various news outlets"
    },
    {
        "issue": "Philanthropic approach differs from traditional foundations",
        "context": "Her approach of giving unrestricted funds to nonprofits is sometimes discussed as unconventional",
        "source_url": "Forbes, NYT, Chronicle of Philanthropy"
    }
])

# Add information about her personal life
expanded_data["personal_life"] = {
    "residence": {
        "current": "Multiple properties including California",
        "former": "Seattle, Washington (during Amazon years)",
        "source_url": "Various sources"
    },
    "hobbies_and_interests": {
        "writing": "Novelist and author",
        "philanthropy": "Primary focus since 2019",
        "source_url": "Wikipedia"
    },
    "naturalization": {
        "date": "June 14, 2016",
        "event": "U.S. naturalization ceremony",
        "photo_location": "Back center",
        "source_url": "Wikipedia"
    }
}

# Add detailed philanthropic recipients
expanded_data["philanthropy"]["notable_recipient_categories"] = {
    "higher_education": {
        "focus": "Historically Black Colleges and Universities, minority-serving institutions",
        "total_amount_billions": 1.06,
        "examples": [
            "Howard University - $80M",
            "Philander Smith University - $19M",
            "Bowie State University",
            "Clark Atlanta University",
            "Norfolk State University",
            "North Carolina A&T",
            "Prairie View A&M",
            "University of Maryland Eastern Shore",
            "Voorhees University",
            "Winston-Salem State University",
            "Xavier University of Louisiana"
        ]
    },
    "housing": {
        "focus": "Affordable housing and housing development",
        "major_grants": [
            {
                "organization": "Habitat for Humanity",
                "amount_billions": 0.436,
                "scope": "International + 84 US affiliates"
            }
        ]
    },
    "reproductive_health": {
        "focus": "Reproductive rights and women's health",
        "major_grants": [
            {
                "organization": "Planned Parenthood",
                "amount_billions": 0.275,
                "year": 2022
            }
        ]
    },
    "lgbtq_support": {
        "focus": "LGBTQ+ equality and suicide prevention",
        "major_grants": [
            {
                "organization": "The Trevor Project",
                "amount_millions": 45,
                "year": 2025,
                "significance": "Largest single donation in organization history"
            }
        ]
    },
    "youth_and_mentorship": {
        "major_grants": [
            {
                "organization": "Girl Scouts of the USA",
                "amount_millions": 84.5,
                "year": 2022,
                "significance": "Largest individual donation in Girl Scouts history"
            },
            {
                "organization": "Big Brothers Big Sisters",
                "amount_millions": 122.6,
                "year": 2022
            }
        ]
    },
    "disaster_relief": {
        "major_grants": [
            {
                "organization": "Hawaii Community Foundation",
                "amount_millions": 5,
                "year": 2023,
                "purpose": "Maui wildfire recovery"
            }
        ]
    },
    "small_nonprofits": {
        "description": "Open call targeting nonprofits with $1-5M annual budgets",
        "year": 2023,
        "total_amount_millions": 640,
        "organizations_funded": 361,
        "breakdown": {
            "organizations_receiving_2_million": 279,
            "organizations_receiving_1_million": 82
        },
        "source_url": "Yield Giving"
    }
}

# Add information about her public statements and philosophy
expanded_data["philanthropy"]["giving_philosophy"] = {
    "key_principles": [
        "Trust in organizations operating on front lines",
        "Preference for unrestricted grants",
        "Rapid, large-scale disbursement",
        "Minimal publicity about donor",
        "Belief in 'giving up control' for better outcomes",
        "Support for systemic change"
    ],
    "quoted_statements": [
        {
            "quote": "Teams with experience on the front lines of challenges will know best how to put the money to good use",
            "source": "Wikipedia/NYT reporting"
        },
        {
            "quote": "When I make gifts, rather than withdrawing funds from a bank account, or from a stock portfolio that increases the wealth and influence of leaders who already have it, I'd like to withdraw them from a portfolio of investments in mission-aligned ventures",
            "date": "December 2024",
            "source": "Yield Giving - Investing essay"
        }
    ]
}

# Add network and connections information
expanded_data["network_and_connections"] = {
    "professional_mentors": [
        {
            "name": "Toni Morrison",
            "role": "Literature professor at Princeton, Nobel Laureate",
            "relationship": "Taught Mackenzie Scott, guided literary career",
            "quote": "One of the best students I've ever had in my creative writing classes",
            "source_url": "Wikipedia"
        }
    ],
    "business_connections": [
        {
            "name": "Jeff Bezos",
            "relationship": "Ex-husband, Amazon co-founder",
            "connection_type": "Former spouse and business partner",
            "source_url": "Wikipedia"
        }
    ],
    "philanthropic_collaborators": [
        {
            "name": "Melinda French Gates",
            "collaboration": "Equality Can't Wait Challenge",
            "year": 2021,
            "focus": "Gender equality",
            "source_url": "Wikipedia"
        }
    ]
}

# Add media and PR information
expanded_data["media_profile"] = {
    "time_100_influential": {
        "year": 2020,
        "ranking": "One of 100 most influential people in the world",
        "source": "Time Magazine"
    },
    "forbes_power_women": {
        "years": [2021, 2023, 2025],
        "ranking": 11,
        "latest_year": 2025
    },
    "media_coverage_frequency": "Frequent - Major announcements covered by major news outlets",
    "primary_communication_channel": "Medium.com (essays)",
    "official_platforms": [
        "Yield Giving website (yieldgiving.com)",
        "Medium (essays)",
        "Social media presence"
    ]
}

# Add Forbes List appearances
expanded_data["forbes_lists"] = {
    "billionaires_2026": {
        "ranking": 84,
        "net_worth": "$32.9 billion",
        "as_of": "April 29, 2026"
    },
    "power_women_2025": {
        "ranking": 11,
        "category": "Most powerful women"
    }
}

# Add book details
expanded_data["literary_career"]["book_details"] = {
    "testing_of_luther_albright": {
        "title": "The Testing of Luther Albright",
        "publisher": "Fourth Estate",
        "isbn": "006075141X",
        "lccn": "2004063235",
        "pages": None,
        "genre": "Fiction/Literary Fiction",
        "publication_date": "2005",
        "awards": {
            "american_book_award": 2006
        },
        "critical_reviews": [
            {
                "reviewer": "Toni Morrison",
                "quote": "A rarity: a sophisticated novel that breaks and swells the heart"
            }
        ],
        "sales_performance": "Modest (according to NPD BookScan)",
        "writing_process": {
            "duration": "10 years",
            "context": "While building Amazon and raising family"
        }
    },
    "traps": {
        "title": "Traps",
        "publisher": "Knopf",
        "isbn": "9780307959737",
        "lccn": "2012029032",
        "publication_date": "2013",
        "genre": "Fiction"
    }
}

# Add detailed timeline
expanded_data["timeline"] = {
    "1970": "Born April 7 in San Francisco",
    "1988": "Graduated from Hotchkiss School",
    "1992": "Earned BA from Princeton University; Met Jeff Bezos at D.E. Shaw",
    "1993": "Married Jeff Bezos",
    "1994": "Moved to Seattle, Bezos founded Amazon with Scott's support",
    "1996": "Reduced involvement in Amazon to focus on writing and family",
    "2000": "Oldest son born",
    "2005": "Published debut novel 'The Testing of Luther Albright'",
    "2006": "Won American Book Award",
    "2013": "Published second novel 'Traps'",
    "2014": "Founded Bystander Revolution (anti-bullying organization)",
    "2016": "June 14 - U.S. naturalization ceremony",
    "2019": "May - Signed Giving Pledge; January - Divorced Jeff Bezos (received $35.6B in Amazon stock)",
    "2020": "July - Announced $1.7B to 116 nonprofits; December - Announced $4.15B to 384 organizations",
    "2021": "June - Announced $2.7B to 286 organizations; Married Dan Jewett",
    "2022": "Multiple major donations announced; September - Filed for divorce from Jewett; Founded Yield Giving",
    "2023": "January - Divorce finalized; March - Launched open call for nonprofits; Donated $640M to 361 organizations",
    "2024": "December - Announced shift to mission-aligned investing",
    "2025": "Donated $7.1B total; Continued major education and equity grants",
    "2026": "Current net worth $32.9B (as of April 29, 2026)"
}

# Add controversies and public perception
expanded_data["public_perception"] = {
    "positive_aspects": [
        "Innovative, unrestricted giving approach",
        "Trust in nonprofit leadership",
        "Large-scale rapid disbursement",
        "Transparency through Yield Giving",
        "Focus on systemic inequality",
        "Support for underrepresented communities"
    ],
    "criticisms": [
        "Some argue wealth came from Amazon, which has labor practices controversies",
        "Debates about whether individual philanthropy should replace government funding",
        "Questions about whether fast giving is sustainable long-term"
    ],
    "impact_assessment": "Generally viewed positively by nonprofit sector; seen as revolutionary in philanthropic approach"
}

# Save expanded data
with open('/home/captainanime/mackenzie_scott_comprehensive_expanded.json', 'w') as f:
    json.dump(expanded_data, f, indent=2)

print("Expanded data saved to mackenzie_scott_comprehensive_expanded.json")
print(f"File size: {len(str(expanded_data))} characters")

