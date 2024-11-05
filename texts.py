SYSTEM_INSTRUCTION = [
    "You are a document processing agent with a focus on RFP analysis, equipment identification, and synergy opportunities. Your knowledge base includes the documents or texts(MISCO, Shape and Southwest) provided in each session, which you should treat as the authoritative source for answering questions, extracting information, and generating outputs.",
    "Only use the information explicitly found in provided documents. Avoid hallucinations: do not infer details not directly located in any document.",
    
    # Key Features of the Agent
    """Your Key Features:
    * Persistent Question Answering
    * Document Summarization
    * Key Phrase Extraction
    * Named Entity Recognition
    * Code Generation for Document and Excel File Creation
    * Synergy Identification for specific brands and product categories
    """,
    
    # Instructions for Handling Excel and DOCX Generations
    "For queries involving phrases like 'extract to bluesheet', 'extract to excel', 'extract to spreadsheet', 'extract to .xlsx', or 'extract to .csv', generate Python code as a string. This code should create an Excel file formatted for readability and saved to 'C:/Users/User/Desktop/google_geminiProj/generated_files'.",
    "If the task involves a document analysis output (e.g., '[Project Name] – Basic RFP Bid Analysis'), generate code to create a .docx file with structured sections as specified in the instructions, pulling content directly from the uploaded RFP.",
    
    # Formatting and Code Requirements
    "For Excel and DOCX generation, ensure headers, fonts, and spacing are clear and professional. Include a worksheet title (for Excel) or document title (for DOCX) based on the project name. Avoid comments in the output except for code formatting as needed.",
    "Use triple quotes '''...''' for multi-line strings in Python code. Ensure the code is well-formatted and follows the provided template for generating Excel and DOCX files.",
    
    # Handling Missing Data
    "If required data is not specified in the document, label it as 'Not specified' in the output file.",
    
    # Library and Path Requirements
    """Do not include any import statements in the code; the environment already has libraries available. Use these libraries:
        # For Excel Files:
        from openpyxl import Workbook  # Create and save new Excel workbooks
        from openpyxl.utils import get_column_letter  # Adjust column widths by letter reference
        from openpyxl.styles import Font, Alignment, PatternFill  # Styling and formatting cells
        from openpyxl.worksheet.worksheet import Worksheet  # Handling worksheets specifically
        from openpyxl.drawing.image import Image  # Insert images into Excel files (if needed)
        # For Word Documents:
        from docx import Document  # Create and manipulate Word documents
        from docx.shared import Pt  # Set font sizes
        from docx.enum.text import WD_ALIGN_PARAGRAPH  # Align paragraph text (left, right, center)
        from docx.oxml.ns import qn  # For advanced formatting (e.g., setting font type)
        from docx.shared import RGBColor  # Set font colors
        from docx.table import Table  # Handle tables in Word documents
        from docx.oxml import OxmlElement  # For custom XML styling elements (advanced use cases)
        from docx.enum.table import WD_TABLE_ALIGNMENT  # Align tables in Word documents
        # For General File Operations:
        import os  # Handle file paths and directory operations
        from os import path  # Check if files or directories exist, get file paths
        # For alternative to excel:
        import csv  # If generating CSV files as an alternative to Excel
        # Utulity Libraries:
        import datetime  # For adding timestamps to file names, if needed
        import re  # Use regular expressions for text processing
        )""",
    
    "Use os to ensure files save without permission errors. Save all files to 'C:/Users/User/Desktop/google_geminiProj/generated_files'. Make sure path exists before saving. If path dose not exist, create the path using os.makedirs().",
]


MISCO = """
MISCO Water

Here is a list of your product categories and represented manufacturers in Northern California. Search the attached 
document and identify the relevant sections and equipment for your business.

Manufacturers:
- Acrison, Aero-Mod, Andritz, Anua, Aqua-Aerobic Systems, Bioforcetech, Cambi, ChemScan, De Nora/Tetra, Diamond Fiberglass, 
Dupont/Memcor, Dupont/Desalitech, Dumpster-veyor, EDI, Evoqua, Golden Harvest, Hallsten, Hayward Gordon, Hellan Fluid 
Strainers, Heron Innovators, INVENT, Jaeger (Raschig), JMS, JWC Environmental, Kaeser Blower, Komax, Lone Star Blower, 
Marcab, Mazzei, MFG Water Treatment, Ostara, Poly Processing, OVIVO, Plasti-Fab, Prominent, PULSCO, RDP Company, Seepex, 
Shand & Jurs, Smith & Loveless, Unison Solutions, Watson-Marlow, WesTech, World Water Works, Xylem/WEDECO

Product Categories:
- Aerators, Anaerobic Digestion, Biological Treatment, Clarification, Disinfection/Chemical Feed, Filtration, Headworks/
Grit Removal, Packaged Treatment Plants, Septage & Receiving, Sludge Conveyance, Sludge Dewatering/Drying, Pumps, 
Odor Control

Specific Technologies:
- Fine Bubble Diffusers, Coarse Bubble Diffusers, INVENT Mixer/Aerators, STM Aerator, Surface Aerators, Thermal Hydrolysis, 
Digester Mixers, Digester Covers, Gas Holding Covers, Gas Conditioning/Scrubbing, Gas Safety Equipment, Sludge Heaters, 
Aerobic Granular Sludge, Anoxic Mixers, Deammonification/DEMON, IFAS/MBBR, Membrane Bioreactors, Oxidation Ditches, Rotary 
Distributors, SEQUOX, Sequencing Batch Reactors, Trickling Filter Media, Turbo Blowers, PD Blowers, Ballasted Floc 
Clarifiers, Chain & Flight Collectors, DAF Thickeners, SAF Thickeners, Spiral Blade Clarifiers, Suction Clarifiers, 
Peristaltic Metering Pumps, Ozone Generators, UV Disinfection, Advanced Oxidation, Polyethylene Storage Tanks, FRP Storage 
Tanks, Chlorine Analyzer, Static and Dynamic Mixers, Polymer Activation, Dry Chemical Feed, Compressed Media Filters, 
Continuous Backwash Filters, Denitrification Filters, Disc Filters, Filter Underdrains, Pulsed Bed Filters, TRIDENT/
Microfloc - 2 Stage Filtration, Band Screens, Chain and Rake Screens, Sewage Grinders, Drum Screens, Vortex Grit Separation, 
Grit Washing/Dewatering, Perforated Plate Screens, Reciprocating Rake Screens, Screenings Washer/Compactors, Spiral Screw 
Screens, Step Screens, Vertical Spiral Screens, FOG Systems, Progressive Cavity Pumps, Hose Pumps, Septage Receiving 
Stations, Belt Conveyors, Screw Conveyors, Dumpsterveyor, Belt Filter Presses, Centrifuges, Screw Presses, Plate & Frame 
Presses, Sludge Hoppers, Sludge Pumps, Paddle Dryers, Drum Dryers, Belt Dryers, BioDryers, Pyrolysis, Chemical Metering 
Pumps, Grit Pumps, Screw Centrifugal Pumps, Airashell Scrubbers, Aluminum Covers, Bio-Scrubbers, Carbon Scrubbers, LOPRO 
Packed Tower Scrubbers, FRP Ducting, BNR Analyzers, Struvite Removal, Sluice & Slide Gates, Strainers, Surge Tanks
"""

SHAPE = """
Shape’s Represented Manufacturers and Categories

ABB – Variable Frequency Drives 
Old Castle – One Lift Package Pump Station 
Netzsch – Progressive Cavity and Rotary Lobe Pumps 
USCP – Steel Reinforced Polymer Concrete Manholes, Microtunnel Pipe & Industrial Pipe Structures. 
Flygt – Submersible Pumps, Mixers, Controls, Check & Mix-Flush Valves 
ITT Gould Pumps – Standard Cast Iron, Bronze, End Suction, Vertical Turbine & Split Case Pumps 
E/One – Packaged Low Pressure Sewer Systems complete with collection basin and grinder pump(s) serving residential and commercial markets 
Lakeside Equipment – Equipment for virtually all stages of wastewater equipment, from influent to discharge. 
Next Turbo – Geared Turbo Compressors 
USF Fabrication – Aluminum Access Hatches, Fall Through Safety Grate System 

The equipment we represent, service and repair comes from the largest trusted manufacturers in the industry. We make it our business to deal with the best and demand that our technicians know the manufacturer’s equipment inside and out. As a supplier of pump, process, control and specialty equipment for over 40 years, we know our business. 

Pumps 
Pumps and process equipment are at the center of every water treatment and processing system. Shape Inc. works directly with the largest and most trusted manufacturers to deliver the highest level of reliability and cutting-edge innovation. 

Process 
The proper integration of process water treatment and purification technologies allow for each system to function at its highest level of efficiency to ensure specific treatment needs are met. 

Controls 
With systems like Flygt Multismart, ABB Drives, Stacon Controls and pump monitoring, we help deliver the most user-friendly control systems for water treatment applications. 

Specialty 
With a wide range of accessories and services for all of our pump equipment, we specialize in unique pump control panels, cellular remote monitoring solutions, manual equipment removal, and access covers for every job.
"""

SOUTH_WEST = """
Southwest Valve Manufacturers and Product Categories:

o Manufacturers:
A-T Controls
Alfa Laval (AS-H Coplastix)
AUMA
DHC Valves and Controls
Echologics
Fresno Valves & Castings
Galli & Cassina
Henry Pratt Company
Hydro Gate Corporation
International Valve Marketing (Vent-Tech)
J & S Valve
Kinetrol
Lined Valve Company
Milliken Valve Company
Mokveld
OMC Controls
Onyx Valve Company
Penn-Troy Manufacturing
Pratt Industrial
Singer Valve
Versa Valves
Virtual Polymer Compounds
Wapro

o Valve Technologies:
Air/Vacuum Relief Valves
Ball Valves: Stainless Steel, V-Port, Segmented
Butterfly Valves: Metal-Seated, Industrial, AWWA
Check Valves
Control Valves: Globe Style, Diaphragm, Axial
Pinch Valves
Plug Valves: Lubricated, Metal Seated
Surge Relief Valves
Telescoping Valves

o Gate Technologies:
Canal Gates, Flap Gates, Knife Gates, Shear Gates, Slide Gates, Sluice Gates, Stop Logs

o Control & Automation:
Electric Actuators, Industrial Valve Automation, Solenoid Systems, Process Control Systems

o Flow Management:
Globe Mixing Systems, Pressure Control, Pressure Isolator Rings

o Monitoring & Assessment:
Acoustic Leak Detection, Pipe Condition Assessment, Metering Systems, Manholes, Flumes

o Water Infrastructure:
AWWA Certified Products, Sewage Solutions, Water Control Systems

o Materials:
Cast Iron, Fiberglass, Stainless Steel, Virtual Polymer Compounds

o Industrial Applications:
Heavy-Duty Systems, Process Control, Specialty Applications
"""
