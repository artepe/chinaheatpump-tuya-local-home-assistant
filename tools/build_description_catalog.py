#!/usr/bin/env python3
"""Build English help from captured labels; never infer units or permissions."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMPONENT = ROOT / "custom_components" / "mango_tuya_local"

GROUPS = [
    (
        "Daily settings",
        "mdi:tune-variant",
        "Temperature targets, operating choices, schedules and user preferences.",
    ),
    (
        "System configuration",
        "mdi:cog-outline",
        "System identity, operating limits, control compensation and communication settings.",
    ),
    (
        "Compressor",
        "mdi:engine-outline",
        "Compressor speed limits, response settings, startup and oil-return parameters.",
    ),
    ("Fan", "mdi:fan", "Fan drive configuration, speed limits and temperature-dependent adjustments."),
    (
        "Valve hardware",
        "mdi:valve",
        "Expansion-valve hardware, manual positions, bypass and oil-return settings.",
    ),
    (
        "Expansion valve",
        "mdi:valve-open",
        "Main expansion-valve opening tables and controller response parameters.",
    ),
    ("Vapor injection", "mdi:pipe-valve", "EVI valve opening criteria, targets and response parameters."),
    (
        "Defrost",
        "mdi:snowflake-melt",
        "Defrost timing, temperature criteria, termination and drainage settings.",
    ),
    (
        "Frost & hydraulics",
        "mdi:water-pump",
        "Frost prevention, water-pump response, fan-coil and sterilization settings.",
    ),
    (
        "Protection",
        "mdi:shield-check-outline",
        "Alarm delays, temperature and current criteria, reset and interlock settings.",
    ),
    (
        "Inputs & sensors",
        "mdi:access-point",
        "Input assignments, temperature offsets, power estimates and sensor configuration.",
    ),
    (
        "Service tables 1",
        "mdi:flask-outline",
        "Manufacturer service and test-point table entries. They are settings, not live measurements.",
    ),
    (
        "Service tables 2",
        "mdi:flask-round-bottom-outline",
        "The second service table, including heating and EVI test-point settings.",
    ),
    (
        "Pressure & pump drive",
        "mdi:gauge",
        "Pressure/flow sensor calibration and pump motor or inverter configuration.",
    ),
    (
        "Working frequency",
        "mdi:chart-bell-curve",
        "All 46 cooling and heating frequency-table entries, arranged by named operating condition.",
    ),
    (
        "Protection & auxiliary",
        "mdi:shield-alert-outline",
        "Additional operating limits, auxiliary heaters, circulation and smart-grid settings.",
    ),
    (
        "Solar & thermostat",
        "mdi:solar-power-variant-outline",
        "Solar-loop, thermostat and additional heating operating-limit settings.",
    ),
]

# These descriptions explain labels, not experimentally validated algorithms.
HELP = {
    "Control Mode": "Selects the controller's operating strategy. The numeric mode codes are not yet mapped.",
    "Cool Set Temp": "Cooling temperature target. The displayed unit and scale have not yet been verified.",
    "Heat Set Temp": "Heating temperature target. The displayed unit and scale have not yet been verified.",
    "DHW Set Temp": "Domestic hot-water temperature target. The displayed unit and scale are unverified.",
    "Auto Set Temp": "Temperature target used by automatic operation. The switching strategy is unverified.",
    "Power Mode": "Selects a power or performance mode. The device's numeric choices are not yet mapped.",
    "Mode Silent": "Configures silent operation, which can restrict operating speed. The choice codes are unverified.",
    "Duty Fun En": "Configures the scheduled-operation function. The enable codes have not yet been mapped.",
    "Duty Set HT.": "Heating target associated with scheduled operation. Its scale is unverified.",
    "Duty Set CL.": "Cooling target associated with scheduled operation. Its scale is unverified.",
    "HT.2-WAY.INTLK": "Configures the heating two-way-valve interlock. The input or output mapping is unverified.",
    "Lock Screen": "Configures the controller's screen lock. The choice codes are unverified.",
    "PUMP.MODE": "Selects the circulation-pump operating strategy. The mode codes are not yet mapped.",
    "END.PUMP.EN": "Configures the pump function named END.PUMP. Its exact operating condition is unverified.",
    "DHW Dual Mode": "Configures a combined domestic-hot-water operating mode. The numeric choices are unverified.",
    "Max Run Time": "Maximum operating-time setting. The timer unit and exact limiting behaviour are unverified.",
    "Cool Time Min": "Minimum cooling-time setting. The timer unit and switching behaviour are unverified.",
    "Heat Time Min": "Minimum heating-time setting. The timer unit and switching behaviour are unverified.",
    "DHW Time Max": "Maximum domestic-hot-water run-time setting. The timer unit is unverified.",
    "H.Pump Set Temp": "Temperature setting associated with the heat-pump function. The reference sensor is unverified.",
    "Defr_C.E.P": "Manufacturer defrost setting named C.E.P. Its exact function has not been verified.",
    "Unit Number": "Number-of-units setting for a multi-unit installation. The configuration format is unverified.",
    "All Comp Diff": "Shared compressor-control difference setting. The reference signal and scale are unverified.",
    "Egy Ctrl Period": "Update-period setting for energy/load control. Its timer scale is unverified.",
    "Sterilization": "Configures the hot-water sterilization function. The enable or mode codes are unverified.",
    "COOL_CURVE": "Selects or configures cooling-curve control. The curve codes are not yet mapped.",
    "HEAT_CURVE": "Selects or configures heating-curve control. The curve codes are not yet mapped.",
    "Unit Type": "Equipment-type configuration. The numeric type codes have not been mapped.",
    "Refrige.Type": "Refrigerant-type configuration. The numeric refrigerant codes have not been mapped.",
    "Four-way Valve": "Configures the reversing valve. Output polarity and choice codes are unverified.",
    "Mac Model": "Manufacturer model configuration. The numeric model codes are unverified.",
    "Remote Type": "Selects the remote-controller or external-control type. The choice codes are unverified.",
    "Control Cyc.": "System control update-period setting. The timer unit is unverified.",
    "Shutdown Rem": "Configures remembered state after shutdown. The exact restart behaviour is unverified.",
    "Auto.Startup": "Configures automatic startup. The trigger and numeric choice codes are unverified.",
    "DHW Diff": "Domestic-hot-water control temperature difference, usually associated with restart hysteresis.",
    "Cool Ctrl Cpst": "Cooling-control compensation setting. Raw 1 is confirmed to display as 0.1; the compensation algorithm is unverified.",
    "Heat Ctrl Cpst": "Heating-control compensation setting. Its scale and compensation algorithm are unverified.",
    "FourV.OpenDly": "Reversing-valve opening delay. The timer unit and switching sequence are unverified.",
    "FourV.OffDly": "Reversing-valve shutdown delay. The timer unit and switching sequence are unverified.",
    "A Heater Env": "Ambient-temperature criterion associated with an auxiliary heater. The exact trigger is unverified.",
    "O Liquid EXH": "Liquid-related exhaust-temperature criterion. Its exact protection or valve logic is unverified.",
    "C Liquid EXH.D": "Difference setting for the liquid/exhaust criterion. The reference signals are unverified.",
    "Crank ON Env": "Ambient-temperature criterion for enabling the crankcase heater. Its scale is unverified.",
    "Crank OFF Env": "Ambient-temperature criterion for disabling the crankcase heater. Its scale is unverified.",
    "Auto Heat Env": "Ambient-temperature criterion associated with automatic heating selection.",
    "Auto Cold Env": "Ambient-temperature criterion associated with automatic cooling selection.",
    "Min PWD Time": "Minimum time for the manufacturer function PWD. The function and timer unit are unverified.",
    "Max PWD Time": "Maximum time for the manufacturer function PWD. The function and timer unit are unverified.",
    "Min Warm Tim": "Minimum warm-operation timer. Its exact cycle and timer unit are unverified.",
    "Max Warm Tim": "Maximum warm-operation timer. App writes of raw 998/999 were observed; the timer unit is unverified.",
    "RemoteOnoff": "Configures external on/off control. The input polarity and choice codes are unverified.",
    "Trans Use": "Configures the manufacturer function named Trans Use. Its exact purpose is unverified.",
    "Forbid LP ENV": "Ambient criterion associated with low-pressure inhibition. Its exact protection logic is unverified.",
    "AntiIceHeatEnv": "Ambient-temperature criterion associated with anti-ice heating.",
    "Cool Set Min": "Lower allowed cooling-target setting. The displayed temperature scale is unverified.",
    "Cool Set Max": "Upper allowed cooling-target setting. The displayed temperature scale is unverified.",
    "Heat Set Min": "Lower allowed heating-target setting. The displayed temperature scale is unverified.",
    "Heat Set Max": "Upper allowed heating-target setting. The displayed temperature scale is unverified.",
    "LoadCpstRange": "Range associated with load compensation. The reference signal and scale are unverified.",
    "LoadCpstTime": "Time associated with load compensation. The timer scale is unverified.",
    "BMS Format": "Building-management communication format. The numeric protocol choices are unverified.",
    "BMS BaudRate": "Building-management communication baud-rate choice. Numeric choices are not yet mapped.",
    "BMS Addr": "Building-management communication address setting.",
    "Device Type": "Device-role or equipment-type configuration. The choice codes are unverified.",
    "Chassis Heater": "Configures the chassis or base-pan heater function. The choice codes are unverified.",
    "Motor Code": "Compressor motor-profile code. The manufacturer's motor-code table is unavailable.",
    "Manual Mode": "Selects compressor manual/service operation. The choice codes are unverified.",
    "Manual RPS": "Manual compressor speed request. Despite the label, the displayed speed scale is unverified.",
    "Comp.Protect": "Compressor protection configuration. The numeric choices are not yet mapped.",
    "FreqPreSub": "Compressor frequency pre-adjustment/subtraction setting. The exact algorithm is unverified.",
    "Min RPS": "Lower compressor speed setting. The raw-to-speed conversion has not been verified.",
    "Max RPS": "Upper compressor speed setting. The raw-to-speed conversion has not been verified.",
    "C.Rated RPS": "Rated compressor speed for cooling. The raw-to-speed conversion is unverified.",
    "H.Rated RPS": "Rated compressor speed for heating. The raw-to-speed conversion is unverified.",
    "Cold Min Speed": "Lower compressor operating-speed setting for cooling. The speed scale is unverified.",
    "Cold Max Speed": "Upper compressor operating-speed setting for cooling. The speed scale is unverified.",
    "Heat Min Speed": "Lower compressor operating-speed setting for heating. The speed scale is unverified.",
    "Heat Max Speed": "Upper compressor operating-speed setting for heating. The speed scale is unverified.",
    "Min RSP Time": "Minimum-speed or RSP timing setting. The exact RSP meaning and timer scale are unverified.",
    "Reoil Time": "Timing setting for compressor oil-return operation. The timer scale is unverified.",
    "Reoil RSP": "Compressor speed setting during oil-return operation. The speed scale is unverified.",
    "AdviceAddr": "Address setting named AdviceAddr. The communication target is unverified.",
    "DefrostFreq": "Compressor frequency request associated with defrost. The speed scale is unverified.",
    "StartFreq": "Compressor frequency request during startup. The speed scale is unverified.",
    "StartSpeed": "Compressor startup speed setting. The raw-to-speed conversion is unverified.",
    "RunSpeed": "Compressor running-speed setting. The raw-to-speed conversion is unverified.",
    "DefrostSpeed": "Compressor speed setting during defrost. The raw-to-speed conversion is unverified.",
    "StartPeriod": "Compressor startup-period setting. The timer scale and startup sequence are unverified.",
    "Hold Time": "Time for holding a control state or speed. The exact condition and timer scale are unverified.",
    "SilentFreqMax": "Maximum compressor-frequency setting in silent operation. The speed scale is unverified.",
    "AvoidFreqRange": "Width of compressor frequency-avoidance bands. The frequency scale is unverified.",
    "CM_MODEL_ID": "Compressor model/profile identifier. The numeric model table is not yet mapped.",
    "FreqFanSet": "Frequency-controlled fan configuration. The choice codes are unverified.",
    "EC fan Code": "Electronically commutated fan profile code. The model-code table is unverified.",
    "FreqSpeedCtrl": "Fan speed-control strategy. The numeric strategy codes are unverified.",
    "Fan M.Speed": "Fan speed setting labelled M.Speed. Its operating condition and scale are unverified.",
    "FixFanSet": "Fixed fan-speed configuration. The numeric choices are unverified.",
    "PWM.Pulse.N": "Pulse-count configuration for the PWM fan interface. The hardware mapping is unverified.",
    "EcFanAddr": "Communication address of the electronically commutated fan.",
    "FreqFanNum": "Number or assignment of frequency-controlled fans. The encoding is unverified.",
    "SilentSpeedMax": "Maximum fan-speed setting for silent operation. The speed scale is unverified.",
    "Send.F Pause": "Pause in fan frequency-command transmission. Its timer scale is unverified.",
    "EEV EVI JOINT": "Configures coordination between the main expansion valve and vapor-injection valve.",
    "Eev.Invt.Diff": "Difference setting for expansion-valve/inverter coordination. The reference signal is unverified.",
    "Eev.Invt.Up": "Expansion-valve/inverter coordination setting for increasing operation.",
    "Eev.Invt.Dn": "Expansion-valve/inverter coordination setting for decreasing operation.",
    "CmOn Reoil Keep": "Compressor-on hold setting associated with oil return. The timer scale is unverified.",
    "CmOn Reoil Time": "Compressor-on timing setting for oil-return operation. The timer scale is unverified.",
    "ReoilOn Time": "Oil-return activation timing setting. The timer scale is unverified.",
    "EEV Reoil Step Start": "Expansion-valve opening/step setting at the start of oil-return operation.",
    "Eev.Preopen.Arith": "Selects an expansion-valve pre-opening calculation strategy. The choice codes are unverified.",
    "Idle OD%": "Expansion-valve opening associated with idle operation. The opening scale is unverified.",
    "Init. Holdtime": "Time for holding the initial expansion-valve position. The timer scale is unverified.",
    "Defrost OD%": "Expansion-valve opening used during defrost. The opening scale is unverified.",
    "LimitRange": "Expansion-valve controller limiting range. The reference signal and scale are unverified.",
    "Force.cl.Evap": "Evaporator criterion associated with forced valve closure. The exact trigger is unverified.",
    "Off EVI Ampli": "Expansion-valve adjustment when vapor injection switches off. The scale is unverified.",
    "HeatLimitWing": "Heating limit associated with the Wing reference signal. The exact sensor is unverified.",
    "DefrInitOdCpst": "Compensation applied to initial defrost valve opening. The adjustment scale is unverified.",
    "EVI Heat Open": "Configures vapor-injection opening during heating. The choice codes are unverified.",
    "EVI Cold Open": "Configures vapor-injection opening during cooling. The choice codes are unverified.",
    "EVI Degree Diff": "Difference used by the vapor-injection degree controller. The reference signal is unverified.",
    "EVI Open Rps": "Compressor-speed criterion for opening vapor injection. The speed scale is unverified.",
    "EVI Close Rps": "Compressor-speed criterion for closing vapor injection. The speed scale is unverified.",
    "EVI Exh Diff": "Exhaust-temperature difference setting in vapor-injection control. Its scale is unverified.",
    "EVI Open In.Cl": "Inlet-related vapor-injection opening criterion in cooling. The reference sensor is unverified.",
    "Dfr.Interval": "Interval setting between defrost operations. The timer scale and eligibility rules are unverified.",
    "Dfr.Time": "Defrost-duration setting. The timer scale and exact duration limit are unverified.",
    "Dfr.Time Cnt": "Defrost timing/count setting. Its exact use and timer scale are unverified.",
    "Dfr. Env.T": "Ambient-temperature criterion used by defrost control. The exact trigger is unverified.",
    "Dfr. Coil T": "Coil-temperature criterion used by defrost control. The exact trigger is unverified.",
    "Dfr.Coil T": "Coil-temperature criterion used by defrost control. The exact trigger is unverified.",
    "Dfr.Out T": "Outlet-temperature criterion used by defrost control. The exact termination rule is unverified.",
    "EWD.SmartDfr": "Configures the manufacturer's smart-defrost function. The numeric choices are unverified.",
    "T. Sure Time": "Confirmation time for a defrost condition. The timer scale is unverified.",
    "LP.Dfr.Dect.": "Low-pressure criterion associated with defrost detection. The exact rule is unverified.",
    "LP.Dfr.Cycle": "Cycle setting for low-pressure-based defrost control. The timer scale is unverified.",
    "LP.Dfr.CoilT": "Coil-temperature criterion for low-pressure-based defrost control.",
    "TimingDefrost": "Configures timer-based defrost operation. The numeric choices are unverified.",
    "Emerg EWD": "Emergency setting associated with the EWD defrost function. The choice codes are unverified.",
    "DfrStopFreq": "Compressor frequency setting associated with defrost termination. The scale is unverified.",
    "DrippingTime": "Drainage/dripping time associated with defrost completion. The timer scale is unverified.",
    "DFR.OP.AUXH.T": "Auxiliary-heater temperature criterion during defrost operation.",
    "Atfr.Enable": "Configures antifreeze operation. The numeric enable or mode codes are unverified.",
    "Sterilization Temp": "Temperature target associated with hot-water sterilization. Its scale is unverified.",
    "Steril-maximum Cycle": "Maximum interval/cycle setting for hot-water sterilization. The timer scale is unverified.",
    "Steril-high Temp Time": "High-temperature hold time for hot-water sterilization. The timer scale is unverified.",
    "PUMPF.Ctrl": "Water-pump control strategy. The numeric strategy codes are unverified.",
    "PUMPF Model": "Water-pump model or drive profile. The model-code table is unverified.",
    "PUMPF Set LH": "Water-pump setting labelled LH. Its exact signal and scale are unverified.",
    "PMF.Set.Flow": "Target flow setting for water-pump control. The flow unit and scale are unverified.",
    "Fcu.Num": "Number-of-fan-coils configuration. The encoding is unverified.",
    "Fcu.Addr": "Fan-coil communication address setting.",
    "Fcu.Mode.Set": "Fan-coil operating-mode configuration. The numeric mode codes are unverified.",
    "Pumpf Start Speed": "Water-pump startup speed setting. The speed scale is unverified.",
    "Pumpf.Debug": "Water-pump service/debug configuration. The numeric choices are unverified.",
    "PUMPF.SetRate": "Water-pump drive-rate request. The raw-to-speed or duty conversion is unverified.",
    "PUMPF.MaxRate": "Upper water-pump drive-rate setting. Its scale is unverified.",
    "PUMPF.Period": "Water-pump control update-period setting. The timer scale is unverified.",
    "Pumpf.DebugRate": "Water-pump drive rate in service/debug operation. Its scale is unverified.",
    "Fac_Pass_Word_Set": "Manufacturer service-password setting. Its encoding and application are unverified.",
    "Pumpf Temp Diff": "Temperature difference associated with water-pump speed control. The scale is unverified.",
    "MIN Traffic Limit": "Minimum-flow or traffic-limit setting. The physical quantity and scale are unverified.",
    "Error Dly": "Delay before a fault condition is accepted. The timer scale and affected faults are unverified.",
    "Flow Err Dly": "Delay before a water-flow fault is accepted. The timer scale is unverified.",
    "Auto.Reset": "Automatic fault-reset configuration. The numeric choices are unverified.",
    "Auto.Re.Awed": "Manufacturer automatic-reset allowance setting. The exact code meaning is unverified.",
    "Exit T. Diff": "Temperature difference used for leaving a protection state. The reference sensor is unverified.",
    "Current Type": "Current measurement or protection input type. The numeric choices are unverified.",
    "OutInDiffErr": "Outlet/inlet temperature-difference protection criterion. The scale is unverified.",
    "OutInDiffHigh": "High outlet/inlet temperature-difference criterion. The exact action is unverified.",
    "GasInOutErr": "Gas inlet/outlet difference protection criterion. The scale is unverified.",
    "Exh Too High": "High discharge/exhaust-temperature protection setting. The scale is unverified.",
    "CoolEvapLow": "Low evaporating-temperature protection criterion during cooling.",
    "CoolGasInLow": "Low inlet-gas temperature criterion during cooling.",
    "CmOffcheckLp": "Low-pressure check associated with compressor-off operation.",
    "SMART_GRID_CFG": "Smart-grid input/operating configuration. The numeric choices are unverified.",
    "SMART_GRID": "Smart-grid operating setting. The numeric choices are unverified.",
    "ECO_RUN_TIME": "Economy-mode run-time setting. The timer scale is unverified.",
    "Reote_Interlock_Delay": "External interlock delay. The timer scale and input polarity are unverified.",
    "Refrigerant Gas Conc High": "High refrigerant-gas concentration protection setting. The concentration scale is unverified.",
    "Comp. LP": "Configuration of the compressor low-pressure input. This is a setting, not a pressure measurement.",
    "Comp. HP": "Configuration of the compressor high-pressure input. This is a setting, not a pressure measurement.",
    "Fan Overload": "Configuration of the fan overload input. The input polarity is unverified.",
    "Water Flow": "Configuration of the water-flow input. This is a setting, not a measured flow value.",
    "Power Err": "Configuration of the electrical-supply fault input. Its polarity is unverified.",
    "TBH Over Load": "Configuration of the tank/backup-heater overload input. Its polarity is unverified.",
    "Sub Freq": "Configuration of the secondary frequency function. Its exact assignment is unverified.",
    "AntiIceSet": "Antifreeze sensor/control configuration. The numeric choices are unverified.",
    "CompTopSet": "Compressor-top sensor/control configuration. The numeric choices are unverified.",
    "EVI.TempDisp": "Vapor-injection temperature display configuration. The choice codes are unverified.",
    "TACtSet": "Sensor/input configuration named TACtSet. The assignment is unverified.",
    "DISPLAY.LOGO": "Controller display-logo configuration. The numeric choices are unverified.",
    "Idu_Odu_Function": "Indoor/outdoor unit function assignment. The numeric choices are unverified.",
    "Power Down Dly": "Shutdown delay associated with power-down operation. The timer scale is unverified.",
    "Language Option": "Controller language selection. The numeric language codes have not been mapped.",
    "PUMPret Enable": "Return/recirculation-pump function configuration. The choice codes are unverified.",
    "PUMPret Run Time": "Return/recirculation-pump operating time. The timer scale is unverified.",
    "PUMPret Disinfect": "Return/recirculation-pump behaviour during disinfection. The choice codes are unverified.",
    "PUMPret Timer": "Return/recirculation-pump timer configuration. The encoding is unverified.",
    "TWout2_SENSOR": "Configuration of the second outlet-water temperature sensor. The choice codes are unverified.",
    "Debug Set.": "Manufacturer service/debug mode configuration. The numeric choices are unverified.",
    "LP Sensor Type": "Low-pressure sensor model/type configuration. The numeric sensor codes are unverified.",
    "HP Sensor Type": "High-pressure sensor model/type configuration. The numeric sensor codes are unverified.",
    "Flow Sensor Type": "Flow-sensor model/type configuration. The numeric sensor codes are unverified.",
    "Ref Leakage Sensor Code": "Refrigerant-leak sensor model/profile code. The numeric code table is unverified.",
    "Ref Leakage Sensor Base Addr": "Base communication address of the refrigerant-leak sensor.",
    "Smart Ele Meter Code": "Electrical meter model/profile code. The numeric code table is unverified.",
    "Smart Ele Meter Addr": "Electrical meter communication address setting.",
    "FreqPmfSet": "Frequency-controlled water-pump configuration. The numeric choices are unverified.",
    "FreqPmfAddr": "Communication address of the frequency-controlled water pump.",
    "PWM Pm Type": "PWM water-pump interface type. The numeric choices are unverified.",
    "Volt Pump Type": "Voltage-controlled water-pump interface type. The numeric choices are unverified.",
    "PM Init Speed": "Initial water-pump speed request. The drive-rate scale is unverified.",
    "PM Init Hold": "Time for holding the initial water-pump speed. The timer scale is unverified.",
    "PM Run Min": "Minimum running water-pump drive rate. The scale is unverified.",
    "Motor Power(KW)": "Pump/inverter motor rated-power configuration. The label names kW but the raw scale is unverified.",
    "Motor Poles": "Motor pole-count configuration for the drive profile.",
    "Motor Rate Cur": "Motor rated-current configuration. The current scale is unverified.",
    "Motor Rate Freq": "Motor rated-frequency configuration. The frequency scale is unverified.",
    "Motor Rate Spee": "Motor rated-speed configuration. The speed scale is unverified.",
    "Motor Rate Volt": "Motor rated-voltage configuration. The voltage scale is unverified.",
    "Invt VF Curve": "Inverter voltage/frequency curve configuration. The curve codes are unverified.",
    "PWM Fb Reserve": "PWM feedback polarity/reserved configuration. The numeric choices are unverified.",
    "PWM Reserve Out": "PWM output polarity/reserved configuration. The numeric choices are unverified.",
    "ERR_AC_FLUX_SET": "Air-conditioning water-flow protection setting. The flow scale is unverified.",
    "CLOSE_AT_HEAT_DELAY": "Delay for the close/stop action associated with heating. The exact action is unverified.",
    "LED Logo En": "Configures the illuminated logo. The numeric enable codes are unverified.",
    "EAH2 En": "Configures the second auxiliary electric-heater stage. The choice codes are unverified.",
    "EAH_ON_HI_DT": "Upper temperature-difference criterion for auxiliary electric heating.",
    "EAH_ON_LO_DT": "Lower temperature-difference criterion for auxiliary electric heating.",
    "EAH_GEAR": "Auxiliary electric-heater stage/level configuration. The choice codes are unverified.",
    "AHS": "Auxiliary heat-source configuration. The numeric choices are unverified.",
    "TWout2 High": "High-temperature criterion for the second outlet-water sensor.",
    "SYS_PUMPF": "System water-pump configuration. The numeric choices are unverified.",
    "Idu_Odu_Type": "Indoor/outdoor unit type assignment. The numeric choices are unverified.",
    "R290_Climate_Temp_Diff": "R290 climate-control temperature difference. Its reference sensor and scale are unverified.",
    "PUMP_INTER_ON_TIME": "On-time for intermittent pump operation. The timer scale is unverified.",
    "PUMP_INTER_OFF_TIME": "Off-time for intermittent pump operation. The timer scale is unverified.",
    "Dhw Set Max": "Upper allowed domestic-hot-water target. The temperature scale is unverified.",
    "Ac Pump Dly": "Air-conditioning circulation-pump delay. The timer scale is unverified.",
    "Invt Base Freq": "Base frequency of the inverter profile. The frequency scale is unverified.",
    "Invt Max Out.V": "Upper inverter output-voltage setting. The voltage scale is unverified.",
    "Ele.Grid Cur. Max": "Upper electrical-supply current setting. The current scale is unverified.",
    "Mac Open Cur. Min": "Minimum current criterion associated with machine activation. The exact rule is unverified.",
    "Cur. Limit Diff": "Difference used in current limiting. The current scale is unverified.",
    "Cur. Force Diff": "Difference used by forced current adjustment. The exact action is unverified.",
    "Ext Equipment Cur.": "External-equipment current allowance or setting. The scale is unverified.",
    "PV Mppt Code": "Photovoltaic MPPT device/profile code. The numeric code table is unverified.",
    "PV Mppt Base Address": "Base communication address of the photovoltaic MPPT controller.",
    "PV Mppt Num": "Number/assignment of photovoltaic MPPT controllers. The encoding is unverified.",
    "Cool Run Max Env.T": "Upper ambient-temperature operating criterion for cooling.",
    "Cool Run Max Wat.T": "Upper water-temperature operating criterion for cooling.",
    "Cpst Begin Temp": "Temperature criterion for starting compensation. The reference signal is unverified.",
    "Temp Cpst Value": "Temperature compensation amount. The reference signal and scale are unverified.",
    "SMART_GRID_LOCK_TIME_MAX": "Maximum hold/lock time for smart-grid control. The timer scale is unverified.",
    "Pv Cpst": "Photovoltaic-related compensation setting. The reference signal and scale are unverified.",
    "TSL_SENSOR": "Sensor configuration named TSL. Its physical sensor location and choice codes are unverified.",
    "SOLAR": "Solar-loop control configuration. The numeric choices are unverified.",
    "PUMPsl_ANTIFREEZE": "Solar-loop pump antifreeze configuration. The numeric choices are unverified.",
    "Heat Run Max Env.T": "Upper ambient-temperature operating criterion for heating.",
    "Heat Run Low Env.T": "Lower ambient-temperature operating criterion for heating.",
    "Heat Run Max Wat.T": "Upper water-temperature operating criterion for heating.",
    "Exit Cm Limit Diff": "Difference used for leaving a compressor-limit state. The reference signal is unverified.",
    "Thermostat Sw": "External thermostat switch configuration. The input polarity and choice codes are unverified.",
    "Thermostat Mode": "External thermostat operating-mode configuration. The numeric choices are unverified.",
    "Pump Pv Flow Cpst": "Photovoltaic-related water-pump flow compensation. The adjustment scale is unverified.",
}

SENSOR_OFFSETS = {
    "TmpInCpst": "inlet-water temperature",
    "TmpOutCpst": "outlet-water temperature",
    "TmpEnvCpst": "ambient temperature",
    "AntiIceCpst": "antifreeze temperature",
    "WingCpst": "the temperature signal named Wing",
    "GasOutCpst": "outlet-gas temperature",
    "GasInCpst": "inlet-gas temperature",
    "ValveCpst": "the valve-related temperature",
    "EcoOutCpst": "economizer outlet temperature",
    "EcoInCpst": "economizer inlet temperature",
    "CmTopCpst": "compressor-top temperature",
    "DHW.Cpst": "domestic-hot-water temperature",
}


def describe(row):
    group, name = row["group"], row["name"].strip()
    confidence = "label_inferred"
    family = ""
    if (group, row["slot"]) == (0, 20):
        return {
            "description": "Sets alarm sound behaviour. Sound On and Once 10sec are verified; Raw 0 and Raw 3 remain unmapped.",
            "confidence": "verified_options",
            "family": "",
        }
    if name in HELP:
        text = HELP[name]
    elif group == 14:
        match = re.fullmatch(r"(Cl|Ht)(Up|Dn)Env(-?\d+)(?:In(.+))?", name)
        if not match:
            raise ValueError("Unknown working-frequency label")
        mode, band, env, inlet = match.groups()
        mode = "Heating" if mode == "Ht" else "Cooling"
        band = "upper" if band == "Up" else "lower"
        family = f"{mode} / {band} table"
        condition = f"Env {int(env)}" + (f", In {inlet}" if inlet else "")
        text = f"{mode} {band} frequency-table entry labelled {condition}. The condition thresholds and speed units are unverified."
    elif name in SENSOR_OFFSETS:
        text = f"Compensation offset for {SENSOR_OFFSETS[name]}. The calibration scale is unverified."
    elif re.fullmatch(r"\d{2}#Unit", name):
        text = f"Assignment/configuration of unit {name[:2]} in a multi-unit system. The choice codes are unverified."
    elif match := re.fullmatch(r"(Silent|Duty|Steri\.|Logo)\s*(Bgn|End|On|Off)?\s*(Hour|Min\.?)", name):
        function = {
            "Silent": "silent operation",
            "Duty": "scheduled operation",
            "Steri.": "sterilization",
            "Logo": "logo lighting",
        }[match[1]]
        part = "hour" if match[3] == "Hour" else "minute"
        action = {"Bgn": "start", "End": "end", "On": "start", "Off": "end", None: "scheduled"}[match[2]]
        text = f"Sets the {action} {part} for {function}."
    elif name == "Steri. On Day":
        text = "Sets the scheduled sterilization day. The weekday encoding is unverified."
    elif name in ("Proportional", "P Coef.", "P coef.", "P Coef", "Pwm_Coef"):
        text = "Proportional response factor for this control loop. The gain scale is unverified."
    elif "Integral" in name or name == "I Coef.":
        text = "Integral-response setting for this control loop; it adjusts accumulated-error response. The scale is unverified."
    elif name == "DerivativeTm":
        text = "Derivative-response setting for this control loop; it relates to error-change response. The scale is unverified."
    elif name in ("MotionPeriod", "Calcu.Period", "Adjust Period", "SpeedPeriod", "Pwm_Period"):
        text = "Control-loop update or adjustment interval. The timer scale is unverified."
    elif name.startswith("AvoidFreq"):
        text = f"Compressor frequency-avoidance point {name[-1]}. The frequency scale is unverified."
    elif re.search(r"Rps(?:Std|Eco|Strong)Adjust|Fan(?:Std|Eco|Strong)Adj", name):
        text = f"Adjustment factor for the speed mode named {name}. The scale and exact mode behaviour are unverified."
    elif group == 3 and ("Max" in name or "Min" in name or "Mid" in name):
        bound = "maximum" if "Max" in name else "minimum" if "Min" in name else "intermediate"
        mode = "cooling" if "Cool" in name else "heating" if "Heat" in name else "fan"
        quantity = "temperature criterion" if "Temp" in name else "fan speed"
        text = f"{bound.capitalize()} {quantity} setting for {mode}. The raw scale is unverified."
    elif group == 3 and re.search(r"\b[CH]old [HL]F|Heat [HL]F", name):
        text = f"Temperature-related fan speed criterion named {name}. The reference signal and scale are unverified."
    elif match := re.match(r"([MS])\.(?:EEV|Manual|OH)", name):
        valve = "Main" if match[1] == "M" else "Secondary"
        if "Enable" in name:
            text = f"{valve} expansion-valve enable/type configuration. The numeric choices are unverified."
        elif "Manual Mode" in name:
            text = (
                f"{valve} expansion-valve manual/service-mode configuration. The choice codes are unverified."
            )
        elif "StepMode" in name:
            text = f"{valve} expansion-valve stepper-drive mode. The numeric drive codes are unverified."
        elif "StepRate" in name:
            text = f"{valve} expansion-valve stepper actuation-rate setting. The rate scale is unverified."
        elif "Max step" in name or "Max Step" in name:
            text = f"{valve} expansion-valve maximum step-count setting."
        elif "Manual Steps" in name:
            text = f"{valve} expansion-valve position request in manual/service operation."
        elif "OD" in name:
            text = f"{valve} expansion-valve opening limit or request named {name}. The opening scale is unverified."
        else:
            text = f"{valve} expansion-valve compensation setting named {name}. The exact reference signal is unverified."
    elif group in (4, 5) and re.search(r"Heat (?:Out M )?Min OD\d|(?:Cold|Heat) I\.(?:Min|Max) OD", name):
        text = (
            f"Expansion-valve opening limit for the condition named {name}. The opening scale is unverified."
        )
    elif group == 5 and re.fullmatch(r"(?:Heat|Cool) Sv\d", name):
        text = f"Expansion-valve target-table entry {name}. The exact target signal and scale are unverified."
    elif group == 5 and ("Ampli" in name or "Change" in name or "Chg" in name):
        text = f"Expansion-valve response or transition setting {name}. The control scale is unverified."
    elif name.startswith("ByV") or "ByV" in name:
        text = f"Bypass-valve operating criterion named {name}. The trigger, timing or scale is unverified."
    elif group == 6 and ("Exh SV" in name or name.startswith("ExhSv") or name.startswith("Setdegree")):
        text = f"Vapor-injection target setting named {name}. The temperature or degree scale is unverified."
    elif group == 6 and re.search(r"I\.Open OD|ExhOV Open", name):
        text = f"Vapor-injection opening setting for {name}. The opening scale and exact condition are unverified."
    elif re.fullmatch(r"(?:Heat|Cool) EVI(?: [A-Z]\d)?", name):
        text = f"Vapor-injection service-table value for {name}. The named operating point is manufacturer-specific."
    elif group == 7:
        text = f"Defrost criterion or sequence setting named {name}. Its exact trigger, timer or scale is unverified."
    elif name.startswith("Atfr."):
        text = f"Antifreeze operating criterion named {name}. The reference signal, trigger or timer scale is unverified."
    elif name.startswith("Pumpf Speed_"):
        direction = "increasing" if "Up" in name else "decreasing"
        quantity = "adjustment interval" if "Cycle" in name else "adjustment amount"
        text = f"Water-pump {quantity} when {direction} speed. The raw scale is unverified."
    elif name.startswith("Exp.Tk."):
        text = f"External-tank or auxiliary-heat criterion named {name}. The sensor assignment and scale are unverified."
    elif group == 9 and name.startswith("C#9_"):
        text = f"Protection-curve entry {name}. The exact condition and raw scaling are unverified."
    elif re.search(r"Low Amb|Air Heat Hi|Air Cool Low|CantOnEnvCool", name):
        text = f"Ambient-temperature operating/protection criterion named {name}. Its threshold direction and scale are unverified."
    elif "Dly" in name or "Delay" in name:
        text = f"Delay associated with {name}. The timer unit and exact switching condition are unverified."
    elif "Selfdef" in name or name.startswith("LDI"):
        text = f"Input/output assignment for {name}. The numeric signal or function choices are unverified."
    elif name.endswith("POWER"):
        text = f"Configured power value for {name[:-5].strip().lower()}. This is a setting, not measured electrical power."
    elif name.startswith("CAP_"):
        text = f"Capacity-estimation adjustment named {name}. Its coefficient or compensation scale is unverified."
    elif group in (11, 12) and name.startswith("Heat "):
        text = f"Heating service-table entry {name[5:]}. The manufacturer-specific operating point and scale are unverified."
    elif group == 11 and name.startswith("Cool "):
        text = f"Cooling service-table entry for {name[5:].lower()}. The operating point and scale are unverified."
    elif name.startswith("Pumpf_Sv_"):
        text = f"Water-pump service/setpoint table entry {name[-2:]}. The raw scale is unverified."
    elif group == 13 and "Range" in name:
        signal = (
            "Low-pressure" if name.startswith("LP") else "High-pressure" if name.startswith("HP") else "Flow"
        )
        end = "lower" if "Min" in name else "upper"
        text = (
            f"{signal} sensor calibration-range {end} endpoint. The raw-to-physical conversion is unverified."
        )
    elif group == 13 and name.startswith(("LP", "HP", "Cool LP", "Heat LP", "Cool HP", "Heat HP")):
        text = f"Pressure-control threshold or difference named {name}. The pressure scale and exact action are unverified."
    elif group == 13 and name.startswith("Invt"):
        text = f"Inverter response/transition setting named {name}. The transition condition and raw scale are unverified."
    elif name.startswith("PUMPf Set Flow"):
        text = f"Water-pump flow target {name[-1]}. The physical flow unit and raw scale are unverified."
    elif name.startswith("PUMPsl_ON_"):
        text = f"Solar-loop pump activation criterion {name[10:]}. The sensor reference and temperature scale are unverified."
    else:
        text = f"Manufacturer setting {name} in {GROUPS[group][0].lower()}. Its exact function has not yet been verified."
        confidence = "unverified"
    return {"description": text, "confidence": confidence, "family": family}


def build(profile):
    groups = [
        {
            "group": s["group"],
            "name": s["name"],
            "title": GROUPS[s["group"]][0],
            "icon": GROUPS[s["group"]][1],
            "description": GROUPS[s["group"]][2],
        }
        for s in profile["sections"]
    ]
    return {
        "format": "mango_dashboard_catalog_v1",
        "groups": groups,
        "parameters": {f"{r['group']}:{r['slot']}": describe(r) for r in profile["routes"]},
    }


if __name__ == "__main__":
    data = build(json.loads((COMPONENT / "profile.json").read_text()))
    (COMPONENT / "descriptions.json").write_text(json.dumps(data, indent=2, ensure_ascii=True) + "\n")
    print("English descriptions:", len(data["parameters"]))
    print("Unverified functions:", sum(p["confidence"] == "unverified" for p in data["parameters"].values()))
