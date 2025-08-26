import streamlit as st
import pandas as pd
import math
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="DC Engineering Tools Suite | Abhishek Diwanji",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Advanced CSS for Professional Dark Theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styling */
    .main > div {
        padding-top: 1rem;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f1419 0%, #1a1f2e 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Header Styling */
    .main-header {
        background: linear-gradient(135deg, #14b8a6 0%, #06b6d4 100%);
        padding: 2rem;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(20, 184, 166, 0.3);
    }
    
    .main-header h1 {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-header h2 {
        font-size: 1.2rem;
        font-weight: 400;
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
    }
    
    /* Developer Credit */
    .developer-credit {
        background: linear-gradient(135deg, #f59e0b 0%, #ef4444 100%);
        padding: 1rem 2rem;
        border-radius: 12px;
        color: white;
        text-align: center;
        font-weight: 600;
        margin: 1rem 0 2rem 0;
        box-shadow: 0 4px 15px rgba(245, 158, 11, 0.3);
    }
    
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
        background: rgba(15, 20, 25, 0.8);
        border-radius: 12px;
        padding: 0.5rem;
        margin-bottom: 2rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 8px;
        color: #e2e8f0;
        font-weight: 600;
        padding: 1rem 2rem;
        border: 1px solid rgba(100, 116, 139, 0.2);
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #14b8a6 0%, #06b6d4 100%);
        color: white;
        border-color: rgba(20, 184, 166, 0.4);
        box-shadow: 0 4px 15px rgba(20, 184, 166, 0.3);
    }
    
    /* Section Headers */
    .section-header {
        background: rgba(20, 184, 166, 0.1);
        border-left: 4px solid #14b8a6;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        margin: 1.5rem 0 1rem 0;
        backdrop-filter: blur(10px);
    }
    
    .section-header h2 {
        color: #14b8a6;
        margin: 0;
        font-size: 1.5rem;
        font-weight: 600;
    }
    
    /* Cards */
    .metric-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(20, 184, 166, 0.2);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, #14b8a6, #06b6d4);
    }
    
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(20, 184, 166, 0.2);
        border-color: rgba(20, 184, 166, 0.4);
    }
    
    .metric-card h3 {
        color: #94a3b8;
        font-size: 0.9rem;
        font-weight: 500;
        margin: 0 0 0.5rem 0;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .metric-card .value {
        color: #14b8a6;
        font-size: 2rem;
        font-weight: 700;
        margin: 0;
        line-height: 1;
    }
    
    .metric-card .subtitle {
        color: #64748b;
        font-size: 0.8rem;
        margin: 0.5rem 0 0 0;
    }
    
    /* Study Cards */
    .study-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(100, 116, 139, 0.2);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    
    .study-card:hover {
        border-color: rgba(20, 184, 166, 0.4);
        box-shadow: 0 4px 20px rgba(20, 184, 166, 0.1);
    }
    
    .study-card h4 {
        color: #f1f5f9;
        font-size: 1.1rem;
        font-weight: 600;
        margin: 0 0 1rem 0;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .study-details {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.5rem;
        margin-top: 1rem;
    }
    
    .study-detail-item {
        color: #cbd5e1;
        font-size: 0.9rem;
        line-height: 1.6;
    }
    
    .study-detail-item strong {
        color: #f1f5f9;
    }
    
    .cost-highlight {
        background: rgba(20, 184, 166, 0.1);
        border: 1px solid rgba(20, 184, 166, 0.3);
        border-radius: 8px;
        padding: 0.75rem;
        text-align: center;
        margin-top: 1rem;
    }
    
    .cost-highlight .amount {
        color: #14b8a6;
        font-size: 1.3rem;
        font-weight: 700;
        margin: 0;
    }
    
    /* Input Styling */
    .stSelectbox > div > div {
        background-color: rgba(30, 41, 59, 0.8);
        border: 1px solid rgba(100, 116, 139, 0.3);
        border-radius: 8px;
        color: #f1f5f9;
    }
    
    .stNumberInput > div > div > input {
        background-color: rgba(30, 41, 59, 0.8);
        border: 1px solid rgba(100, 116, 139, 0.3);
        border-radius: 8px;
        color: #f1f5f9;
    }
    
    .stTextInput > div > div > input {
        background-color: rgba(30, 41, 59, 0.8);
        border: 1px solid rgba(100, 116, 139, 0.3);
        border-radius: 8px;
        color: #f1f5f9;
    }
    
    .stCheckbox > label {
        color: #cbd5e1;
        font-weight: 500;
    }
    
    .stSlider > div > div > div {
        color: #14b8a6;
    }
    
    /* Results Section */
    .results-container {
        background: rgba(15, 20, 25, 0.6);
        border: 1px solid rgba(20, 184, 166, 0.3);
        border-radius: 16px;
        padding: 2rem;
        margin: 2rem 0;
        backdrop-filter: blur(15px);
    }
    
    /* Custom Text Colors */
    .stMarkdown {
        color: #e2e8f0;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #f1f5f9;
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #14b8a6 0%, #06b6d4 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(20, 184, 166, 0.4);
    }
    
    /* Disclaimer Box */
    .disclaimer-box {
        background: rgba(245, 158, 11, 0.1);
        border: 1px solid rgba(245, 158, 11, 0.3);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 2rem 0;
        backdrop-filter: blur(10px);
    }
    
    .disclaimer-box h4 {
        color: #f59e0b;
        margin: 0 0 1rem 0;
    }
    
    .disclaimer-box p {
        color: #fbbf24;
        margin: 0.5rem 0;
        line-height: 1.6;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>⚡ Data Center Engineering Tools Suite</h1>
    <h2>Professional Bus Count Estimation & Cost Analysis Dashboard</h2>
    <p>Advanced Engineering Tools for Data Center Power System Design & Studies</p>
</div>
""", unsafe_allow_html=True)

# Developer Credit
st.markdown("""
<div class="developer-credit">
    🚀 Developed by <strong>Abhishek Diwanji</strong> | Power Systems Engineering Expert
</div>
""", unsafe_allow_html=True)

# Main Tabs Interface
tab1, tab2 = st.tabs(["🔌 Bus Count Estimator", "💰 Cost Estimation Tool"])

# =============================================================================
# TAB 1: BUS COUNT ESTIMATOR
# =============================================================================
with tab1:
    st.markdown("""
    <div class="disclaimer-box">
        <h4>🔌 Bus Count Estimation Tool</h4>
        <p><strong>Purpose:</strong> Estimate electrical bus requirements for data center power distribution systems based on load capacity, tier level, and design parameters.</p>
        <p><strong>Note:</strong> Results are estimates for preliminary design. Always validate with detailed electrical studies.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Bus Count Tool Interface
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="section-header">
            <h2>📊 Project Parameters</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Input type toggle
        input_type = st.radio(
            "Starting Point:",
            ["IT Load (MW)", "Total Facility Load (MW)"],
            help="Choose whether to start from critical IT load or total facility load",
            key="bus_input_type"
        )
        
        # Main load input
        if input_type == "IT Load (MW)":
            it_mw = st.number_input("IT Load (MW)", min_value=0.1, max_value=100.0, value=5.0, step=0.1, key="bus_it_load")
            total_mw = None
        else:
            total_mw = st.number_input("Total Facility Load (MW)", min_value=0.2, max_value=200.0, value=7.8, step=0.1, key="bus_total_load")
            it_mw = None
        
        # PUE input
        pue = st.slider("PUE (Power Usage Effectiveness)", min_value=1.1, max_value=2.0, value=1.56, step=0.01, key="bus_pue")
        
        # Data center type
        dc_type = st.selectbox("Data Center Type", ["Enterprise/Colo", "Hyperscale", "AI/HPC"], key="bus_dc_type")
        
        # Redundancy tier
        redundancy = st.selectbox("Redundancy Tier", ["N (Base)", "Tier III (N+1)", "Tier IV (2N)"], index=1, key="bus_redundancy")
        
        # Non-IT load split
        mech_fraction = st.slider("Mechanical (Cooling) Fraction", min_value=0.5, max_value=0.9, value=0.7, step=0.01, key="bus_mech_fraction")
    
    with col2:
        st.markdown("""
        <div class="section-header">
            <h2>🔧 Equipment Capacities</h2>
        </div>
        """, unsafe_allow_html=True)
        
        ups_lineup = st.slider("UPS Lineup (MW)", 0.5, 2.0, 1.5, 0.1, key="bus_ups")
        transformer_mva = st.slider("Transformer MV→LV (MVA)", 1.0, 5.0, 3.0, 0.1, key="bus_transformer")
        lv_bus_mw = st.slider("LV Switchboard Bus Section (MW)", 2.0, 4.5, 3.0, 0.1, key="bus_lv_bus")
        pdu_mva = st.slider("PDU Capacity (MVA)", 0.2, 0.6, 0.3, 0.05, key="bus_pdu")
        mv_base = st.slider("MV Buses Base (per system)", 1, 4, 2, 1, key="bus_mv_base")
        
        st.markdown("""
        <div class="section-header">
            <h2>⚙️ Additional Factors</h2>
        </div>
        """, unsafe_allow_html=True)
        
        voltage_levels = st.selectbox("Voltage Levels", [2, 3], index=0, key="bus_voltage_levels")
        backup_gens = st.slider("Backup Generators", 0, 10, 0, 1, key="bus_backup_gens")
        expansion_factor = st.slider("Future Expansion Factor", 1.0, 1.5, 1.0, 0.05, key="bus_expansion")
        power_factor = st.slider("Power Factor", 0.9, 1.0, 0.95, 0.01, key="bus_power_factor")
        bus_calibration_factor = st.slider("Bus Count Calibration Factor", 0.5, 2.0, 1.0, 0.1, key="bus_calibration_factor")
    
    # Bus Count Calculations
    def calculate_bus_counts():
        # Step 1: Load derivation
        if it_mw is not None:
            calc_total_mw = pue * it_mw
            calc_it_mw = it_mw
        else:
            calc_total_mw = total_mw
            calc_it_mw = total_mw / pue
        
        non_it_mw = calc_total_mw - calc_it_mw
        mech_mw = mech_fraction * non_it_mw
        house_mw = non_it_mw - mech_mw
        
        # Step 2: Base bus counts
        BUS_PER_MW = {"N (Base)": 1.5, "Tier III (N+1)": 2.0, "Tier IV (2N)": 2.3}
        estimated_buses = math.ceil(calc_total_mw * BUS_PER_MW[redundancy] * bus_calibration_factor)
        
        # Detailed component calculations
        lv_it_pcc = math.ceil(calc_it_mw / lv_bus_mw)
        lv_mech_mcc = math.ceil(mech_mw / lv_bus_mw)
        lv_house_pcc = math.ceil(house_mw / lv_bus_mw)
        lv_total = lv_it_pcc + lv_mech_mcc + lv_house_pcc
        
        ups_lineups = math.ceil(calc_it_mw / ups_lineup)
        pdus_total = math.ceil(calc_it_mw / pdu_mva)
        tx_count = math.ceil(calc_total_mw / (transformer_mva * power_factor))
        
        # Additional components
        voltage_additions = (voltage_levels - 2) * (tx_count + 1) if voltage_levels > 2 else 0
        generator_additions = backup_gens * 2
        
        # Apply expansion factor
        final_bus_count = math.ceil(estimated_buses * expansion_factor)
        
        return {
            'total_load': calc_total_mw,
            'it_load': calc_it_mw,
            'mechanical_load': mech_mw,
            'house_load': house_mw,
            'estimated_buses': final_bus_count,
            'lv_total': lv_total,
            'ups_lineups': ups_lineups,
            'pdus_total': pdus_total,
            'tx_count': tx_count,
            'mv_buses': mv_base,
            'voltage_additions': voltage_additions,
            'generator_additions': generator_additions
        }
    
    # Calculate and display results
    bus_results = calculate_bus_counts()
    
    # Results Display
    st.markdown("""
    <div class="section-header">
        <h2>📊 Bus Count Results</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Main metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Total Buses</h3>
            <p class="value">{bus_results['estimated_buses']:,}</p>
            <p class="subtitle">Calibrated estimate</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Total Load</h3>
            <p class="value">{bus_results['total_load']:.1f} MW</p>
            <p class="subtitle">PUE: {pue:.2f}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3>IT Load</h3>
            <p class="value">{bus_results['it_load']:.1f} MW</p>
            <p class="subtitle">Critical load</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Redundancy</h3>
            <p class="value">{redundancy.split('(')[0].strip()}</p>
            <p class="subtitle">{dc_type}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Component breakdown
    st.markdown("### 🔧 Component Breakdown")
    
    breakdown_data = {
        'Component': [
            'MV Buses', 'Transformers (MV→LV)', 'LV IT Buses (PCC)', 
            'LV Mechanical Buses (MCC)', 'LV House/Aux Buses', 'UPS Output Buses',
            'PDUs', 'Voltage Level Additions', 'Generator Transfer Switches'
        ],
        'Count': [
            bus_results['mv_buses'], bus_results['tx_count'], math.ceil(bus_results['it_load'] / lv_bus_mw),
            math.ceil(bus_results['mechanical_load'] / lv_bus_mw), math.ceil(bus_results['house_load'] / lv_bus_mw),
            bus_results['ups_lineups'], bus_results['pdus_total'], bus_results['voltage_additions'],
            bus_results['generator_additions']
        ],
        'Description': [
            f"Base {mv_base} buses", f"{bus_results['total_load']:.1f} MW ÷ {transformer_mva} MVA",
            f"{bus_results['it_load']:.1f} MW ÷ {lv_bus_mw} MW", f"{bus_results['mechanical_load']:.1f} MW ÷ {lv_bus_mw} MW",
            f"{bus_results['house_load']:.1f} MW ÷ {lv_bus_mw} MW", f"{bus_results['ups_lineups']} UPS lineups",
            f"{bus_results['it_load']:.1f} MW ÷ {pdu_mva} MVA", f"{voltage_levels-2} extra levels" if voltage_levels > 2 else "None",
            f"{backup_gens} generators × 2 ATS" if backup_gens > 0 else "None"
        ]
    }
    
    df_breakdown = pd.DataFrame(breakdown_data)
    st.dataframe(df_breakdown, use_container_width=True, hide_index=True)

# =============================================================================
# TAB 2: COST ESTIMATION TOOL
# =============================================================================
with tab2:
    st.markdown("""
    <div class="disclaimer-box">
        <h4>💰 Cost Estimation Tool</h4>
        <p><strong>Purpose:</strong> Estimate project costs for data center power system studies including Load Flow, Short Circuit, PDC, and Arc Flash analysis.</p>
        <p><strong>Note:</strong> Bus count calculations are handled by the separate Bus Count tool. This tool focuses on cost estimation only.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Project Information Section
    st.markdown("""
    <div class="section-header">
        <h2>📋 Project Information</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        project_name = st.text_input("Project Name", value="DC Power Studies", key="cost_project_name")
    with col2:
        it_capacity = st.number_input("IT Capacity (MW)", min_value=0.1, max_value=100.0, value=10.0, step=0.1, key="cost_it_capacity")
    with col3:
        mechanical_load = st.number_input("Mechanical Load (MW)", min_value=0.1, max_value=50.0, value=7.0, step=0.1, key="cost_mechanical")
    with col4:
        house_load = st.number_input("House/Auxiliary Load (MW)", min_value=0.1, max_value=20.0, value=3.0, step=0.1, key="cost_house")
    
    col5, col6, col7, col8 = st.columns(4)
    
    with col5:
        tier_level = st.selectbox("Tier Level", ["Tier I", "Tier II", "Tier III", "Tier IV"], index=3, key="cost_tier")
    with col6:
        delivery_type = st.selectbox("Type of Delivery", ["Standard", "Urgent"], key="cost_delivery")
    with col7:
        report_format = st.selectbox("Report Format", ["Basic PDF", "Detailed Report with Appendices", "Client-Branded Report"], index=1, key="cost_report")
    with col8:
        client_meetings = st.number_input("Number of Client Meetings", min_value=0, max_value=10, value=3, step=1, key="cost_meetings")
    
    col9, _ = st.columns([1, 3])
    with col9:
        custom_margin = st.number_input("Custom Margins (%)", min_value=0, max_value=30, value=15, step=1, key="cost_margin")
    
    # Calibration Controls (Expandable Section)
    with st.expander("🔧 Calibration Controls", expanded=False):
        cal_col1, cal_col2, cal_col3 = st.columns(3)
        
        with cal_col1:
            st.markdown("#### Hourly Rates (₹) - Updated Ranges")
            # FIXED: Updated default values to be within the new ranges
            senior_rate = st.number_input("Senior Engineer", min_value=500, max_value=4000, value=1200, step=50, key="cal_senior_rate")
            mid_rate = st.number_input("Mid-level Engineer", min_value=500, max_value=2500, value=650, step=25, key="cal_mid_rate")
            junior_rate = st.number_input("Junior Engineer", min_value=500, max_value=1500, value=500, step=25, key="cal_junior_rate")  # FIXED: Changed from 350 to 500
        
        with cal_col2:
            st.markdown("#### Study Complexity Factors")
            load_flow_factor = st.slider("Load Flow (base: 0.8h/bus)", 0.5, 2.0, 1.0, 0.1, key="cal_lf_factor")
            short_circuit_factor = st.slider("Short Circuit (base: 1.0h/bus)", 0.5, 2.0, 1.0, 0.1, key="cal_sc_factor")
            pdc_factor = st.slider("PDC (base: 1.5h/bus)", 0.5, 2.0, 1.0, 0.1, key="cal_pdc_factor")
            arc_flash_factor = st.slider("Arc Flash (base: 1.2h/bus)", 0.5, 2.0, 1.0, 0.1, key="cal_af_factor")
        
        with cal_col3:
            st.markdown("#### Other Factors")
            urgency_multiplier = st.slider("Urgent Delivery Multiplier", 1.1, 2.0, 1.3, 0.1, key="cal_urgency")
            meeting_cost = st.number_input("Cost per Meeting (₹)", min_value=3000, max_value=15000, value=8000, step=500, key="cal_meeting_cost")
            
            st.markdown("#### Resource Allocation (%)")
            senior_allocation = st.slider("Senior Engineer %", 10, 40, 20, 1, key="cal_senior_alloc") / 100
            mid_allocation = st.slider("Mid-level Engineer %", 20, 50, 30, 1, key="cal_mid_alloc") / 100
            junior_allocation = st.slider("Junior Engineer %", 30, 70, 50, 1, key="cal_junior_alloc") / 100
            
            # Normalize allocations
            total_allocation = senior_allocation + mid_allocation + junior_allocation
            if total_allocation != 1.0:
                senior_allocation = senior_allocation / total_allocation
                mid_allocation = mid_allocation / total_allocation
                junior_allocation = junior_allocation / total_allocation
        
        if st.button("Reset Calibration to Defaults", type="secondary", key="reset_calibration"):
            st.experimental_rerun()
    
    # Bus Count and Studies Section
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.markdown("""
        <div class="section-header">
            <h2>🔌 Bus Count Estimation</h2>
        </div>
        """, unsafe_allow_html=True)
        
        bus_calibration = st.slider("Bus Count Calibration Factor", 0.5, 2.0, 1.3, 0.1, key="cost_bus_cal")
        
        # Calculate basic info for cost tool
        total_load = it_capacity + mechanical_load + house_load
        tier_mapping = {"Tier I": 1.5, "Tier II": 1.7, "Tier III": 2.0, "Tier IV": 2.3}
        estimated_buses = math.ceil(total_load * tier_mapping[tier_level] * bus_calibration)
        
        st.markdown(f"""
        <div class="metric-card">
            <h3>Total Load:</h3>
            <p class="value">{total_load:.1f} MW</p>
        </div>
        
        <div class="metric-card">
            <h3>Estimated Buses:</h3>
            <p class="value">{estimated_buses} buses</p>
            <p class="subtitle">{tier_level} • {tier_mapping[tier_level]} buses/MW</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_right:
        st.markdown("""
        <div class="section-header">
            <h2>📋 Studies Required</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # FIXED: Removed Select All button to fix the bug
        studies_selected = {}
        
        col_s1, col_s2 = st.columns([1, 4])
        with col_s1:
            studies_selected['load_flow'] = st.checkbox("", value=True, key="study_lf")
        with col_s2:
            st.markdown("**Load Flow Study**<br><small>Steady-state voltage and power flow analysis</small>", unsafe_allow_html=True)
        
        col_s3, col_s4 = st.columns([1, 4])
        with col_s3:
            studies_selected['short_circuit'] = st.checkbox("", value=True, key="study_sc")
        with col_s4:
            st.markdown("**Short Circuit Study**<br><small>Fault current calculations and equipment verification</small>", unsafe_allow_html=True)
        
        col_s5, col_s6 = st.columns([1, 4])
        with col_s5:
            studies_selected['pdc'] = st.checkbox("", value=True, key="study_pdc")
        with col_s6:
            st.markdown("**Protective Device Coordination**<br><small>Relay coordination and protection settings</small>", unsafe_allow_html=True)
        
        col_s7, col_s8 = st.columns([1, 4])
        with col_s7:
            studies_selected['arc_flash'] = st.checkbox("", value=True, key="study_af")
        with col_s8:
            st.markdown("**Arc Flash Study**<br><small>Incident energy calculations and PPE requirements</small>", unsafe_allow_html=True)
    
    # Cost Calculations
    TIER_FACTORS = {"Tier I": 1.0, "Tier II": 1.2, "Tier III": 1.5, "Tier IV": 2.0}
    
    STUDIES_DATA = {
        'load_flow': {'name': 'Load Flow Study', 'base_hours_per_bus': 0.8, 'factor': load_flow_factor, 'emoji': '⚡'},
        'short_circuit': {'name': 'Short Circuit Study', 'base_hours_per_bus': 1.0, 'factor': short_circuit_factor, 'emoji': '⚡'},
        'pdc': {'name': 'Protective Device Coordination', 'base_hours_per_bus': 1.5, 'factor': pdc_factor, 'emoji': '🔧'},
        'arc_flash': {'name': 'Arc Flash Study', 'base_hours_per_bus': 1.2, 'factor': arc_flash_factor, 'emoji': '🔥'}
    }
    
    # Calculate costs
    tier_complexity = TIER_FACTORS[tier_level]
    total_study_hours = 0
    total_study_cost = 0
    study_results = {}
    
    for study_key, study_data in STUDIES_DATA.items():
        if studies_selected.get(study_key, False):
            study_hours = estimated_buses * study_data['base_hours_per_bus'] * study_data['factor'] * tier_complexity
            total_study_hours += study_hours
            
            senior_hours = study_hours * senior_allocation
            mid_hours = study_hours * mid_allocation
            junior_hours = study_hours * junior_allocation
            
            rate_multiplier = urgency_multiplier if delivery_type == "Urgent" else 1.0
            
            senior_cost = senior_hours * senior_rate * rate_multiplier
            mid_cost = mid_hours * mid_rate * rate_multiplier
            junior_cost = junior_hours * junior_rate * rate_multiplier
            
            study_total_cost = senior_cost + mid_cost + junior_cost
            total_study_cost += study_total_cost
            
            study_results[study_key] = {
                'name': study_data['name'],
                'emoji': study_data['emoji'],
                'hours': study_hours,
                'senior_hours': senior_hours,
                'mid_hours': mid_hours,
                'junior_hours': junior_hours,
                'senior_cost': senior_cost,
                'mid_cost': mid_cost,
                'junior_cost': junior_cost,
                'total_cost': study_total_cost
            }
    
    # Additional costs
    total_meeting_cost = client_meetings * meeting_cost
    REPORT_MULTIPLIERS = {"Basic PDF": 1.0, "Detailed Report with Appendices": 1.8, "Client-Branded Report": 2.2}
    report_cost = 15000 * REPORT_MULTIPLIERS[report_format]
    subtotal = total_study_cost + total_meeting_cost + report_cost
    total_cost = subtotal * (1 + custom_margin/100)
    
    # Results Section
    st.markdown("""
    <div class="section-header">
        <h2>📊 Cost Estimation Results</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Main metrics
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Project</h3>
            <p class="value">{project_name}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Total Load</h3>
            <p class="value">{total_load:.1f} MW</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Tier Level</h3>
            <p class="value">{tier_level}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Bus Count</h3>
            <p class="value">{estimated_buses} buses</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Total Hours</h3>
            <p class="value">{total_study_hours:.0f} hrs</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Study-wise Cost Breakdown
    if study_results:
        st.markdown("""
        <div class="section-header">
            <h2>📋 Study-wise Cost Breakdown</h2>
        </div>
        """, unsafe_allow_html=True)
        
        for study_key, study in study_results.items():
            st.markdown(f"""
            <div class="study-card">
                <h4>{study['emoji']} {study['name']}</h4>
                <p style="color: #64748b; margin: 0 0 1rem 0;">{study['hours']:.1f} hours total</p>
                <div class="study-details">
                    <div class="study-detail-item">
                        <strong>Senior:</strong> {study['senior_hours']:.1f}h (₹{study['senior_cost']:,.0f})<br>
                        <strong>Mid:</strong> {study['mid_hours']:.1f}h (₹{study['mid_cost']:,.0f})<br>
                        <strong>Junior:</strong> {study['junior_hours']:.1f}h (₹{study['junior_cost']:,.0f})
                    </div>
                    <div class="cost-highlight">
                        <p class="amount">₹{study['total_cost']:,.0f}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Simple chart using Streamlit
        st.markdown("### 📊 Cost Distribution")
        chart_data = pd.DataFrame({
            'Study': [study['name'] for study in study_results.values()],
            'Cost': [study['total_cost'] for study in study_results.values()]
        })
        st.bar_chart(chart_data.set_index('Study'))
        
        # Final cost summary
        st.markdown(f"""
        <div class="results-container">
            <h3 style="color: #14b8a6; text-align: center; margin-bottom: 2rem;">Total Project Cost Summary</h3>
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; text-align: center;">
                <div>
                    <h4 style="color: #06b6d4; margin: 0;">Studies Cost</h4>
                    <p style="color: #f1f5f9; font-size: 1.2rem; font-weight: 600; margin: 0.5rem 0;">₹{total_study_cost:,.0f}</p>
                </div>
                <div>
                    <h4 style="color: #06b6d4; margin: 0;">Meetings Cost</h4>
                    <p style="color: #f1f5f9; font-size: 1.2rem; font-weight: 600; margin: 0.5rem 0;">₹{total_meeting_cost:,.0f}</p>
                </div>
                <div>
                    <h4 style="color: #06b6d4; margin: 0;">Report Cost</h4>
                    <p style="color: #f1f5f9; font-size: 1.2rem; font-weight: 600; margin: 0.5rem 0;">₹{report_cost:,.0f}</p>
                </div>
                <div>
                    <h4 style="color: #06b6d4; margin: 0;">Margin ({custom_margin}%)</h4>
                    <p style="color: #f1f5f9; font-size: 1.2rem; font-weight: 600; margin: 0.5rem 0;">₹{total_cost - subtotal:,.0f}</p>
                </div>
            </div>
            <div style="text-align: center; margin-top: 2rem; padding: 2rem; background: rgba(20, 184, 166, 0.1); border-radius: 12px;">
                <h2 style="color: #14b8a6; margin: 0;">Total Project Cost</h2>
                <p style="color: #14b8a6; font-size: 3rem; font-weight: 700; margin: 1rem 0;">₹{total_cost:,.0f}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    else:
        st.warning("⚠️ No studies selected. Please select at least one study type to see cost estimates.")

# Footer
st.markdown("""
<div style="text-align: center; color: #64748b; padding: 2rem; margin-top: 3rem; border-top: 1px solid rgba(100, 116, 139, 0.2);">
    <p style="font-size: 1.1rem; font-weight: 600; color: #14b8a6; margin: 0;">⚡ Data Center Engineering Tools Suite</p>
    <p style="margin: 0.5rem 0;">🚀 Developed by <strong>Abhishek Diwanji</strong> | Power Systems Engineering Expert</p>
    <p style="margin: 0; font-size: 0.9rem;">Professional Suite v3.0 | Bus Count Estimator + Cost Analysis Tools</p>
</div>
""", unsafe_allow_html=True)
