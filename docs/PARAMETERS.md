# English parameter reference

All 770 real routes. Descriptions are based on captured device labels, not a complete manufacturer manual. Inferred and unknown functions are explicitly marked. Units and write permissions are not inferred from flags.

## Daily settings

Temperature targets, operating choices, schedules and user preferences.

| Parameter | English explanation | Confidence |
|---|---|---|
| Control Mode | Selects the controller's operating strategy. The numeric mode codes are not yet mapped. | label inferred |
| Cool Set Temp | Cooling temperature target. The displayed unit and scale have not yet been verified. | label inferred |
| Heat Set Temp | Heating temperature target. The displayed unit and scale have not yet been verified. | label inferred |
| DHW Set Temp | Domestic hot-water temperature target. The displayed unit and scale are unverified. | label inferred |
| Auto Set Temp | Temperature target used by automatic operation. The switching strategy is unverified. | label inferred |
| Power Mode | Selects a power or performance mode. The device's numeric choices are not yet mapped. | label inferred |
| Mode Silent | Configures silent operation, which can restrict operating speed. The choice codes are unverified. | label inferred |
| Silent Bgn Hour | Sets the start hour for silent operation. | label inferred |
| Silent Bgn Min | Sets the start minute for silent operation. | label inferred |
| Silent End Hour | Sets the end hour for silent operation. | label inferred |
| Silent End Min | Sets the end minute for silent operation. | label inferred |
| Duty Fun En | Configures the scheduled-operation function. The enable codes have not yet been mapped. | label inferred |
| Duty Set HT. | Heating target associated with scheduled operation. Its scale is unverified. | label inferred |
| Duty Set CL. | Cooling target associated with scheduled operation. Its scale is unverified. | label inferred |
| Duty On Hour | Sets the start hour for scheduled operation. | label inferred |
| Duty On Min. | Sets the start minute for scheduled operation. | label inferred |
| Duty Off Hour | Sets the end hour for scheduled operation. | label inferred |
| Duty Off Min. | Sets the end minute for scheduled operation. | label inferred |
| HT.2-WAY.INTLK | Configures the heating two-way-valve interlock. The input or output mapping is unverified. | label inferred |
| Lock Screen | Configures the controller's screen lock. The choice codes are unverified. | label inferred |
| Alarm Sound Set | Sets alarm sound behaviour. Sound On and Once 10sec are verified; Raw 0 and Raw 3 remain unmapped. | verified options |
| PUMP.MODE | Selects the circulation-pump operating strategy. The mode codes are not yet mapped. | label inferred |
| END.PUMP.EN | Configures the pump function named END.PUMP. Its exact operating condition is unverified. | label inferred |
| DHW Dual Mode | Configures a combined domestic-hot-water operating mode. The numeric choices are unverified. | label inferred |
| Max Run Time | Maximum operating-time setting. The timer unit and exact limiting behaviour are unverified. | label inferred |
| Cool Time Min | Minimum cooling-time setting. The timer unit and switching behaviour are unverified. | label inferred |
| Heat Time Min | Minimum heating-time setting. The timer unit and switching behaviour are unverified. | label inferred |
| DHW Time Max | Maximum domestic-hot-water run-time setting. The timer unit is unverified. | label inferred |
| H.Pump Set Temp | Temperature setting associated with the heat-pump function. The reference sensor is unverified. | label inferred |
| Defr_C.E.P | Manufacturer defrost setting named C.E.P. Its exact function has not been verified. | label inferred |
| Unit Number | Number-of-units setting for a multi-unit installation. The configuration format is unverified. | label inferred |
| 00#Unit | Assignment/configuration of unit 00 in a multi-unit system. The choice codes are unverified. | label inferred |
| 01#Unit | Assignment/configuration of unit 01 in a multi-unit system. The choice codes are unverified. | label inferred |
| 02#Unit | Assignment/configuration of unit 02 in a multi-unit system. The choice codes are unverified. | label inferred |
| 03#Unit | Assignment/configuration of unit 03 in a multi-unit system. The choice codes are unverified. | label inferred |
| 04#Unit | Assignment/configuration of unit 04 in a multi-unit system. The choice codes are unverified. | label inferred |
| 05#Unit | Assignment/configuration of unit 05 in a multi-unit system. The choice codes are unverified. | label inferred |
| 06#Unit | Assignment/configuration of unit 06 in a multi-unit system. The choice codes are unverified. | label inferred |
| 07#Unit | Assignment/configuration of unit 07 in a multi-unit system. The choice codes are unverified. | label inferred |
| All Comp Diff | Shared compressor-control difference setting. The reference signal and scale are unverified. | label inferred |
| Egy Ctrl Period | Update-period setting for energy/load control. Its timer scale is unverified. | label inferred |
| Steri. On Day | Sets the scheduled sterilization day. The weekday encoding is unverified. | label inferred |
| Steri. On Hour | Sets the start hour for sterilization. | label inferred |
| Steri. On Min | Sets the start minute for sterilization. | label inferred |
| Sterilization | Configures the hot-water sterilization function. The enable or mode codes are unverified. | label inferred |
| COOL_CURVE | Selects or configures cooling-curve control. The curve codes are not yet mapped. | label inferred |
| HEAT_CURVE | Selects or configures heating-curve control. The curve codes are not yet mapped. | label inferred |
| DO4_Selfdef | Input/output assignment for DO4_Selfdef. The numeric signal or function choices are unverified. | label inferred |

## System configuration

System identity, operating limits, control compensation and communication settings.

| Parameter | English explanation | Confidence |
|---|---|---|
| Unit Type | Equipment-type configuration. The numeric type codes have not been mapped. | label inferred |
| Refrige.Type | Refrigerant-type configuration. The numeric refrigerant codes have not been mapped. | label inferred |
| Four-way Valve | Configures the reversing valve. Output polarity and choice codes are unverified. | label inferred |
| Mac Model | Manufacturer model configuration. The numeric model codes are unverified. | label inferred |
| Remote Type | Selects the remote-controller or external-control type. The choice codes are unverified. | label inferred |
| Control Cyc. | System control update-period setting. The timer unit is unverified. | label inferred |
| Shutdown Rem | Configures remembered state after shutdown. The exact restart behaviour is unverified. | label inferred |
| Auto.Startup | Configures automatic startup. The trigger and numeric choice codes are unverified. | label inferred |
| DHW Diff | Domestic-hot-water control temperature difference, usually associated with restart hysteresis. | label inferred |
| Control Mode | Selects the controller's operating strategy. The numeric mode codes are not yet mapped. | label inferred |
| Cool Ctrl Cpst | Cooling-control compensation setting. Raw 1 is confirmed to display as 0.1; the compensation algorithm is unverified. | label inferred |
| FourV.OpenDly | Reversing-valve opening delay. The timer unit and switching sequence are unverified. | label inferred |
| FourV.OffDly | Reversing-valve shutdown delay. The timer unit and switching sequence are unverified. | label inferred |
| A Heater Env | Ambient-temperature criterion associated with an auxiliary heater. The exact trigger is unverified. | label inferred |
| O Liquid EXH | Liquid-related exhaust-temperature criterion. Its exact protection or valve logic is unverified. | label inferred |
| C Liquid EXH.D | Difference setting for the liquid/exhaust criterion. The reference signals are unverified. | label inferred |
| Crank ON Env | Ambient-temperature criterion for enabling the crankcase heater. Its scale is unverified. | label inferred |
| Crank OFF Env | Ambient-temperature criterion for disabling the crankcase heater. Its scale is unverified. | label inferred |
| Auto Heat Env | Ambient-temperature criterion associated with automatic heating selection. | label inferred |
| Auto Cold Env | Ambient-temperature criterion associated with automatic cooling selection. | label inferred |
| Heat Ctrl Cpst | Heating-control compensation setting. Its scale and compensation algorithm are unverified. | label inferred |
| Min PWD Time | Minimum time for the manufacturer function PWD. The function and timer unit are unverified. | label inferred |
| Max PWD Time | Maximum time for the manufacturer function PWD. The function and timer unit are unverified. | label inferred |
| Min Warm Tim | Minimum warm-operation timer. Its exact cycle and timer unit are unverified. | label inferred |
| Max Warm Tim | Maximum warm-operation timer. App writes of raw 998/999 were observed; the timer unit is unverified. | label inferred |
| DO3_Selfdef | Input/output assignment for DO3_Selfdef. The numeric signal or function choices are unverified. | label inferred |
| DO5_Selfdef | Input/output assignment for DO5_Selfdef. The numeric signal or function choices are unverified. | label inferred |
| DO7_Selfdef | Input/output assignment for DO7_Selfdef. The numeric signal or function choices are unverified. | label inferred |
| DO1_Selfdef | Input/output assignment for DO1_Selfdef. The numeric signal or function choices are unverified. | label inferred |
| RemoteOnoff | Configures external on/off control. The input polarity and choice codes are unverified. | label inferred |
| H.Eng Load D | Manufacturer setting H.Eng Load D in system configuration. Its exact function has not yet been verified. | unverified |
| H.Eng Unload D | Manufacturer setting H.Eng Unload D in system configuration. Its exact function has not yet been verified. | unverified |
| Trans Use | Configures the manufacturer function named Trans Use. Its exact purpose is unverified. | label inferred |
| Forbid LP ENV | Ambient criterion associated with low-pressure inhibition. Its exact protection logic is unverified. | label inferred |
| AntiIceHeatEnv | Ambient-temperature criterion associated with anti-ice heating. | label inferred |
| Cool Set Min | Lower allowed cooling-target setting. The displayed temperature scale is unverified. | label inferred |
| Cool Set Max | Upper allowed cooling-target setting. The displayed temperature scale is unverified. | label inferred |
| Heat Set Min | Lower allowed heating-target setting. The displayed temperature scale is unverified. | label inferred |
| Heat Set Max | Upper allowed heating-target setting. The displayed temperature scale is unverified. | label inferred |
| LoadCpstRange | Range associated with load compensation. The reference signal and scale are unverified. | label inferred |
| LoadCpstTime | Time associated with load compensation. The timer scale is unverified. | label inferred |
| BMS Format | Building-management communication format. The numeric protocol choices are unverified. | label inferred |
| BMS BaudRate | Building-management communication baud-rate choice. Numeric choices are not yet mapped. | label inferred |
| BMS Addr | Building-management communication address setting. | label inferred |
| C.Eng Load D | Manufacturer setting C.Eng Load D in system configuration. Its exact function has not yet been verified. | unverified |
| Device Type | Device-role or equipment-type configuration. The choice codes are unverified. | label inferred |
| Chassis Heater | Configures the chassis or base-pan heater function. The choice codes are unverified. | label inferred |
| C.Eng Unload D | Manufacturer setting C.Eng Unload D in system configuration. Its exact function has not yet been verified. | unverified |

## Compressor

Compressor speed limits, response settings, startup and oil-return parameters.

| Parameter | English explanation | Confidence |
|---|---|---|
| Motor Code | Compressor motor-profile code. The manufacturer's motor-code table is unavailable. | label inferred |
| Manual Mode | Selects compressor manual/service operation. The choice codes are unverified. | label inferred |
| Manual RPS | Manual compressor speed request. Despite the label, the displayed speed scale is unverified. | label inferred |
| Comp.Protect | Compressor protection configuration. The numeric choices are not yet mapped. | label inferred |
| FreqPreSub | Compressor frequency pre-adjustment/subtraction setting. The exact algorithm is unverified. | label inferred |
| Min RPS | Lower compressor speed setting. The raw-to-speed conversion has not been verified. | label inferred |
| Max RPS | Upper compressor speed setting. The raw-to-speed conversion has not been verified. | label inferred |
| C.Rated RPS | Rated compressor speed for cooling. The raw-to-speed conversion is unverified. | label inferred |
| H.Rated RPS | Rated compressor speed for heating. The raw-to-speed conversion is unverified. | label inferred |
| Hold Time | Time for holding a control state or speed. The exact condition and timer scale are unverified. | label inferred |
| Cold Min Speed | Lower compressor operating-speed setting for cooling. The speed scale is unverified. | label inferred |
| Cold Max Speed | Upper compressor operating-speed setting for cooling. The speed scale is unverified. | label inferred |
| Heat Min Speed | Lower compressor operating-speed setting for heating. The speed scale is unverified. | label inferred |
| Heat Max Speed | Upper compressor operating-speed setting for heating. The speed scale is unverified. | label inferred |
| Min RSP Time | Minimum-speed or RSP timing setting. The exact RSP meaning and timer scale are unverified. | label inferred |
| Reoil Time | Timing setting for compressor oil-return operation. The timer scale is unverified. | label inferred |
| AdviceAddr | Address setting named AdviceAddr. The communication target is unverified. | label inferred |
| DefrostFreq | Compressor frequency request associated with defrost. The speed scale is unverified. | label inferred |
| StartFreq | Compressor frequency request during startup. The speed scale is unverified. | label inferred |
| StartSpeed | Compressor startup speed setting. The raw-to-speed conversion is unverified. | label inferred |
| RunSpeed | Compressor running-speed setting. The raw-to-speed conversion is unverified. | label inferred |
| DefrostSpeed | Compressor speed setting during defrost. The raw-to-speed conversion is unverified. | label inferred |
| RpsStdAdjust | Adjustment factor for the speed mode named RpsStdAdjust. The scale and exact mode behaviour are unverified. | label inferred |
| StartPeriod | Compressor startup-period setting. The timer scale and startup sequence are unverified. | label inferred |
| Proportional | Proportional response factor for this control loop. The gain scale is unverified. | label inferred |
| Integral  Tm | Integral-response setting for this control loop; it adjusts accumulated-error response. The scale is unverified. | label inferred |
| DerivativeTm | Derivative-response setting for this control loop; it relates to error-change response. The scale is unverified. | label inferred |
| MotionPeriod | Control-loop update or adjustment interval. The timer scale is unverified. | label inferred |
| Calcu.Period | Control-loop update or adjustment interval. The timer scale is unverified. | label inferred |
| P Coef. | Proportional response factor for this control loop. The gain scale is unverified. | label inferred |
| Cold Cond Up | Manufacturer setting Cold Cond Up in compressor. Its exact function has not yet been verified. | unverified |
| Heat Cond Up | Manufacturer setting Heat Cond Up in compressor. Its exact function has not yet been verified. | unverified |
| RpsEcoAdjust | Adjustment factor for the speed mode named RpsEcoAdjust. The scale and exact mode behaviour are unverified. | label inferred |
| Heat Evap Down | Manufacturer setting Heat Evap Down in compressor. Its exact function has not yet been verified. | unverified |
| Freq.Max.Cur.Lmt | Manufacturer setting Freq.Max.Cur.Lmt in compressor. Its exact function has not yet been verified. | unverified |
| Freq.Max.Load.T | Manufacturer setting Freq.Max.Load.T in compressor. Its exact function has not yet been verified. | unverified |
| Freq.Blockage.T | Manufacturer setting Freq.Blockage.T in compressor. Its exact function has not yet been verified. | unverified |
| Exh Up Limit | Manufacturer setting Exh Up Limit in compressor. Its exact function has not yet been verified. | unverified |
| Reoil RSP | Compressor speed setting during oil-return operation. The speed scale is unverified. | label inferred |
| SpeedDownDly | Delay associated with SpeedDownDly. The timer unit and exact switching condition are unverified. | label inferred |
| RpsStrongAdjust | Adjustment factor for the speed mode named RpsStrongAdjust. The scale and exact mode behaviour are unverified. | label inferred |
| SilentFreqMax | Maximum compressor-frequency setting in silent operation. The speed scale is unverified. | label inferred |
| AvoidFreqRange | Width of compressor frequency-avoidance bands. The frequency scale is unverified. | label inferred |
| AvoidFreq1 | Compressor frequency-avoidance point 1. The frequency scale is unverified. | label inferred |
| AvoidFreq2 | Compressor frequency-avoidance point 2. The frequency scale is unverified. | label inferred |
| AvoidFreq3 | Compressor frequency-avoidance point 3. The frequency scale is unverified. | label inferred |
| AvoidFreq4 | Compressor frequency-avoidance point 4. The frequency scale is unverified. | label inferred |
| CM_MODEL_ID | Compressor model/profile identifier. The numeric model table is not yet mapped. | label inferred |

## Fan

Fan drive configuration, speed limits and temperature-dependent adjustments.

| Parameter | English explanation | Confidence |
|---|---|---|
| FreqFanSet | Frequency-controlled fan configuration. The choice codes are unverified. | label inferred |
| EC fan Code | Electronically commutated fan profile code. The model-code table is unverified. | label inferred |
| FanMaxCool | Maximum fan speed setting for cooling. The raw scale is unverified. | label inferred |
| FanMinCool | Minimum fan speed setting for cooling. The raw scale is unverified. | label inferred |
| FanEcoAdj | Adjustment factor for the speed mode named FanEcoAdj. The scale and exact mode behaviour are unverified. | label inferred |
| FreqSpeedCtrl | Fan speed-control strategy. The numeric strategy codes are unverified. | label inferred |
| Fan M.Speed | Fan speed setting labelled M.Speed. Its operating condition and scale are unverified. | label inferred |
| HighModule.T | Manufacturer setting HighModule.T in fan. Its exact function has not yet been verified. | unverified |
| Cold HF.Env | Temperature-related fan speed criterion named Cold HF.Env. The reference signal and scale are unverified. | label inferred |
| Cold LF.Env | Temperature-related fan speed criterion named Cold LF.Env. The reference signal and scale are unverified. | label inferred |
| Heat HF.Env | Temperature-related fan speed criterion named Heat HF.Env. The reference signal and scale are unverified. | label inferred |
| Heat LF.Env | Temperature-related fan speed criterion named Heat LF.Env. The reference signal and scale are unverified. | label inferred |
| Cold HF.cond | Temperature-related fan speed criterion named Cold HF.cond. The reference signal and scale are unverified. | label inferred |
| Cold LF.cond | Temperature-related fan speed criterion named Cold LF.cond. The reference signal and scale are unverified. | label inferred |
| Heat HF.evap | Temperature-related fan speed criterion named Heat HF.evap. The reference signal and scale are unverified. | label inferred |
| Heat LF.evap | Temperature-related fan speed criterion named Heat LF.evap. The reference signal and scale are unverified. | label inferred |
| FixFanSet | Fixed fan-speed configuration. The numeric choices are unverified. | label inferred |
| SpeedPeriod | Control-loop update or adjustment interval. The timer scale is unverified. | label inferred |
| SpeedPercent | Manufacturer setting SpeedPercent in fan. Its exact function has not yet been verified. | unverified |
| FanMaxHeat | Maximum fan speed setting for heating. The raw scale is unverified. | label inferred |
| FanMinHeat | Minimum fan speed setting for heating. The raw scale is unverified. | label inferred |
| PWM.Pulse.N | Pulse-count configuration for the PWM fan interface. The hardware mapping is unverified. | label inferred |
| FanStrongAdj | Adjustment factor for the speed mode named FanStrongAdj. The scale and exact mode behaviour are unverified. | label inferred |
| EcFanAddr | Communication address of the electronically commutated fan. | label inferred |
| EcMinSpeed | Minimum fan speed setting for fan. The raw scale is unverified. | label inferred |
| EcMaxSpeed | Maximum fan speed setting for fan. The raw scale is unverified. | label inferred |
| FreqFanNum | Number or assignment of frequency-controlled fans. The encoding is unverified. | label inferred |
| SilentSpeedMax | Maximum fan-speed setting for silent operation. The speed scale is unverified. | label inferred |
| Pwm_Init | Manufacturer setting Pwm_Init in fan. Its exact function has not yet been verified. | unverified |
| Pwm_Coef | Proportional response factor for this control loop. The gain scale is unverified. | label inferred |
| Pwm_Period | Control-loop update or adjustment interval. The timer scale is unverified. | label inferred |
| Pwm_Area | Manufacturer setting Pwm_Area in fan. Its exact function has not yet been verified. | unverified |
| FanStdAdj | Adjustment factor for the speed mode named FanStdAdj. The scale and exact mode behaviour are unverified. | label inferred |
| Avoid Cold.F | Manufacturer setting Avoid Cold.F in fan. Its exact function has not yet been verified. | unverified |
| Send.F Pause | Pause in fan frequency-command transmission. Its timer scale is unverified. | label inferred |
| Avoid Cold.T | Manufacturer setting Avoid Cold.T in fan. Its exact function has not yet been verified. | unverified |
| FreqCpstCoef | Manufacturer setting FreqCpstCoef in fan. Its exact function has not yet been verified. | unverified |
| MinCpstCoef | Minimum fan speed setting for fan. The raw scale is unverified. | label inferred |
| ColdFanEnv. Dif | Manufacturer setting ColdFanEnv. Dif in fan. Its exact function has not yet been verified. | unverified |
| ColdFanWing Dif | Manufacturer setting ColdFanWing Dif in fan. Its exact function has not yet been verified. | unverified |
| HeatFanEnv. Dif | Manufacturer setting HeatFanEnv. Dif in fan. Its exact function has not yet been verified. | unverified |
| HeatFanWing Dif | Manufacturer setting HeatFanWing Dif in fan. Its exact function has not yet been verified. | unverified |
| CoolFanSpeed adj | Manufacturer setting CoolFanSpeed adj in fan. Its exact function has not yet been verified. | unverified |
| FanMidCool | Intermediate fan speed setting for cooling. The raw scale is unverified. | label inferred |
| FanMidHeat | Intermediate fan speed setting for heating. The raw scale is unverified. | label inferred |
| FanMidTempCool | Intermediate temperature criterion setting for cooling. The raw scale is unverified. | label inferred |
| FanMidTempHeat | Intermediate temperature criterion setting for heating. The raw scale is unverified. | label inferred |

## Valve hardware

Expansion-valve hardware, manual positions, bypass and oil-return settings.

| Parameter | English explanation | Confidence |
|---|---|---|
| M.EEV Enable | Main expansion-valve enable/type configuration. The numeric choices are unverified. | label inferred |
| M.EEV StepMode | Main expansion-valve stepper-drive mode. The numeric drive codes are unverified. | label inferred |
| M.EEV StepRate | Main expansion-valve stepper actuation-rate setting. The rate scale is unverified. | label inferred |
| M.EEV Max step | Main expansion-valve maximum step-count setting. | label inferred |
| M.EEV ForceOD% | Main expansion-valve opening limit or request named M.EEV ForceOD%. The opening scale is unverified. | label inferred |
| M.EEV Max OD% | Main expansion-valve opening limit or request named M.EEV Max OD%. The opening scale is unverified. | label inferred |
| M.OH Exh Cpst | Main expansion-valve compensation setting named M.OH Exh Cpst. The exact reference signal is unverified. | label inferred |
| M.Manual Mode | Main expansion-valve manual/service-mode configuration. The choice codes are unverified. | label inferred |
| M.Manual Steps | Main expansion-valve position request in manual/service operation. | label inferred |
| EEV EVI JOINT | Configures coordination between the main expansion valve and vapor-injection valve. | label inferred |
| S.EEV Enable | Secondary expansion-valve enable/type configuration. The numeric choices are unverified. | label inferred |
| S.EEV StepMode | Secondary expansion-valve stepper-drive mode. The numeric drive codes are unverified. | label inferred |
| S.EEV StepRate | Secondary expansion-valve stepper actuation-rate setting. The rate scale is unverified. | label inferred |
| S.EEV Max Step | Secondary expansion-valve maximum step-count setting. | label inferred |
| S.EEV ForceOD% | Secondary expansion-valve opening limit or request named S.EEV ForceOD%. The opening scale is unverified. | label inferred |
| S.EEV Max OD% | Secondary expansion-valve opening limit or request named S.EEV Max OD%. The opening scale is unverified. | label inferred |
| S.EEV Min OD% | Secondary expansion-valve opening limit or request named S.EEV Min OD%. The opening scale is unverified. | label inferred |
| S.Manual Mode | Secondary expansion-valve manual/service-mode configuration. The choice codes are unverified. | label inferred |
| S.Manual Steps | Secondary expansion-valve position request in manual/service operation. | label inferred |
| Lehw.In | Manufacturer setting Lehw.In in valve hardware. Its exact function has not yet been verified. | unverified |
| Lehw.Env | Manufacturer setting Lehw.Env in valve hardware. Its exact function has not yet been verified. | unverified |
| Lehw.EEV | Manufacturer setting Lehw.EEV in valve hardware. Its exact function has not yet been verified. | unverified |
| M.OH Freq Cpst | Main expansion-valve compensation setting named M.OH Freq Cpst. The exact reference signal is unverified. | label inferred |
| Eev.Invt.Diff | Difference setting for expansion-valve/inverter coordination. The reference signal is unverified. | label inferred |
| Eev.Invt.Up | Expansion-valve/inverter coordination setting for increasing operation. | label inferred |
| Eev.Invt.Dn | Expansion-valve/inverter coordination setting for decreasing operation. | label inferred |
| M.EEV Exh Sub | Main expansion-valve compensation setting named M.EEV Exh Sub. The exact reference signal is unverified. | label inferred |
| ByV On Env   | Bypass-valve operating criterion named ByV On Env. The trigger, timing or scale is unverified. | label inferred |
| ByVon OD Coef. | Bypass-valve operating criterion named ByVon OD Coef.. The trigger, timing or scale is unverified. | label inferred |
| ByVoff OD Coef. | Bypass-valve operating criterion named ByVoff OD Coef.. The trigger, timing or scale is unverified. | label inferred |
| ByV Off Dly | Bypass-valve operating criterion named ByV Off Dly. The trigger, timing or scale is unverified. | label inferred |
| Cool ByV Off Dly | Bypass-valve operating criterion named Cool ByV Off Dly. The trigger, timing or scale is unverified. | label inferred |
| CmOn Reoil Keep | Compressor-on hold setting associated with oil return. The timer scale is unverified. | label inferred |
| Reoil CmOn Time | Manufacturer setting Reoil CmOn Time in valve hardware. Its exact function has not yet been verified. | unverified |
| ReoilOn Time | Oil-return activation timing setting. The timer scale is unverified. | label inferred |
| AV Var Freq Inc | Manufacturer setting AV Var Freq Inc in valve hardware. Its exact function has not yet been verified. | unverified |
| AV Freq Inc Coef | Manufacturer setting AV Freq Inc Coef in valve hardware. Its exact function has not yet been verified. | unverified |
| AV Freq Red Coef | Manufacturer setting AV Freq Red Coef in valve hardware. Its exact function has not yet been verified. | unverified |
| Freq Lim V Coef | Manufacturer setting Freq Lim V Coef in valve hardware. Its exact function has not yet been verified. | unverified |
| Open Freq Lim V Pv  | Manufacturer setting Open Freq Lim V Pv in valve hardware. Its exact function has not yet been verified. | unverified |
| M.OH ExhEX Cpst | Main expansion-valve compensation setting named M.OH ExhEX Cpst. The exact reference signal is unverified. | label inferred |
| EEV Reoil Step Start | Expansion-valve opening/step setting at the start of oil-return operation. | label inferred |
| Eev.Preopen.Arith | Selects an expansion-valve pre-opening calculation strategy. The choice codes are unverified. | label inferred |
| Heat Out M Min OD1 | Expansion-valve opening limit for the condition named Heat Out M Min OD1. The opening scale is unverified. | label inferred |
| Heat Out M Min OD2 | Expansion-valve opening limit for the condition named Heat Out M Min OD2. The opening scale is unverified. | label inferred |
| Heat Out M Min OD3 | Expansion-valve opening limit for the condition named Heat Out M Min OD3. The opening scale is unverified. | label inferred |
| Heat Out M Min OD4 | Expansion-valve opening limit for the condition named Heat Out M Min OD4. The opening scale is unverified. | label inferred |
| Heat Out M Min OD5 | Expansion-valve opening limit for the condition named Heat Out M Min OD5. The opening scale is unverified. | label inferred |

## Expansion valve

Main expansion-valve opening tables and controller response parameters.

| Parameter | English explanation | Confidence |
|---|---|---|
| Idle OD% | Expansion-valve opening associated with idle operation. The opening scale is unverified. | label inferred |
| Init. Holdtime | Time for holding the initial expansion-valve position. The timer scale is unverified. | label inferred |
| Cold Ampli. | Expansion-valve response or transition setting Cold Ampli.. The control scale is unverified. | label inferred |
| Heat Ampli.1 | Expansion-valve response or transition setting Heat Ampli.1. The control scale is unverified. | label inferred |
| Heat Ampli.2 | Expansion-valve response or transition setting Heat Ampli.2. The control scale is unverified. | label inferred |
| Heat Ampli.3 | Expansion-valve response or transition setting Heat Ampli.3. The control scale is unverified. | label inferred |
| Heat Change.1 | Expansion-valve response or transition setting Heat Change.1. The control scale is unverified. | label inferred |
| Heat Change.2 | Expansion-valve response or transition setting Heat Change.2. The control scale is unverified. | label inferred |
| Cold I.Min OD% | Expansion-valve opening limit for the condition named Cold I.Min OD%. The opening scale is unverified. | label inferred |
| Cold I.Max OD% | Expansion-valve opening limit for the condition named Cold I.Max OD%. The opening scale is unverified. | label inferred |
| Heat I.Min OD% | Expansion-valve opening limit for the condition named Heat I.Min OD%. The opening scale is unverified. | label inferred |
| Heat I.Max OD% | Expansion-valve opening limit for the condition named Heat I.Max OD%. The opening scale is unverified. | label inferred |
| Cold Min OD | Manufacturer setting Cold Min OD in expansion valve. Its exact function has not yet been verified. | unverified |
| Cool Sv1 | Expansion-valve target-table entry Cool Sv1. The exact target signal and scale are unverified. | label inferred |
| Cool Sv2 | Expansion-valve target-table entry Cool Sv2. The exact target signal and scale are unverified. | label inferred |
| Cool Sv3 | Expansion-valve target-table entry Cool Sv3. The exact target signal and scale are unverified. | label inferred |
| Cold Chg1 | Expansion-valve response or transition setting Cold Chg1. The control scale is unverified. | label inferred |
| Cold Chg2 | Expansion-valve response or transition setting Cold Chg2. The control scale is unverified. | label inferred |
| Heat Sv1 | Expansion-valve target-table entry Heat Sv1. The exact target signal and scale are unverified. | label inferred |
| Heat Sv2 | Expansion-valve target-table entry Heat Sv2. The exact target signal and scale are unverified. | label inferred |
| Heat Sv3 | Expansion-valve target-table entry Heat Sv3. The exact target signal and scale are unverified. | label inferred |
| Heat Sv4 | Expansion-valve target-table entry Heat Sv4. The exact target signal and scale are unverified. | label inferred |
| Heat Sv5 | Expansion-valve target-table entry Heat Sv5. The exact target signal and scale are unverified. | label inferred |
| Heat Sv6 | Expansion-valve target-table entry Heat Sv6. The exact target signal and scale are unverified. | label inferred |
| Heat Sv7 | Expansion-valve target-table entry Heat Sv7. The exact target signal and scale are unverified. | label inferred |
| Heat Sv8 | Expansion-valve target-table entry Heat Sv8. The exact target signal and scale are unverified. | label inferred |
| Heat Sv9 | Expansion-valve target-table entry Heat Sv9. The exact target signal and scale are unverified. | label inferred |
| Force.cl.Evap | Evaporator criterion associated with forced valve closure. The exact trigger is unverified. | label inferred |
| Defrost OD% | Expansion-valve opening used during defrost. The opening scale is unverified. | label inferred |
| LimitRange | Expansion-valve controller limiting range. The reference signal and scale are unverified. | label inferred |
| Proportional | Proportional response factor for this control loop. The gain scale is unverified. | label inferred |
| Integral  Tm | Integral-response setting for this control loop; it adjusts accumulated-error response. The scale is unverified. | label inferred |
| DerivativeTm | Derivative-response setting for this control loop; it relates to error-change response. The scale is unverified. | label inferred |
| MotionPeriod | Control-loop update or adjustment interval. The timer scale is unverified. | label inferred |
| Calcu.Period | Control-loop update or adjustment interval. The timer scale is unverified. | label inferred |
| P coef. | Proportional response factor for this control loop. The gain scale is unverified. | label inferred |
| Heat Min OD1 | Expansion-valve opening limit for the condition named Heat Min OD1. The opening scale is unverified. | label inferred |
| Heat Min OD2 | Expansion-valve opening limit for the condition named Heat Min OD2. The opening scale is unverified. | label inferred |
| Heat Min OD3 | Expansion-valve opening limit for the condition named Heat Min OD3. The opening scale is unverified. | label inferred |
| Heat Min OD4 | Expansion-valve opening limit for the condition named Heat Min OD4. The opening scale is unverified. | label inferred |
| Heat Min OD5 | Expansion-valve opening limit for the condition named Heat Min OD5. The opening scale is unverified. | label inferred |
| Heat Min OD6 | Expansion-valve opening limit for the condition named Heat Min OD6. The opening scale is unverified. | label inferred |
| Heat Min OD7 | Expansion-valve opening limit for the condition named Heat Min OD7. The opening scale is unverified. | label inferred |
| Heat Min OD8 | Expansion-valve opening limit for the condition named Heat Min OD8. The opening scale is unverified. | label inferred |
| Heat Min OD9 | Expansion-valve opening limit for the condition named Heat Min OD9. The opening scale is unverified. | label inferred |
| Off EVI Ampli | Expansion-valve adjustment when vapor injection switches off. The scale is unverified. | label inferred |
| HeatLimitWing | Heating limit associated with the Wing reference signal. The exact sensor is unverified. | label inferred |
| DefrInitOdCpst | Compensation applied to initial defrost valve opening. The adjustment scale is unverified. | label inferred |

## Vapor injection

EVI valve opening criteria, targets and response parameters.

| Parameter | English explanation | Confidence |
|---|---|---|
| EVI Heat Open | Configures vapor-injection opening during heating. The choice codes are unverified. | label inferred |
| EVI Cold Open | Configures vapor-injection opening during cooling. The choice codes are unverified. | label inferred |
| EVI Open Dly | Delay associated with EVI Open Dly. The timer unit and exact switching condition are unverified. | label inferred |
| EVI Open Env.Ht | Manufacturer setting EVI Open Env.Ht in vapor injection. Its exact function has not yet been verified. | unverified |
| EVI Open Exh | Manufacturer setting EVI Open Exh in vapor injection. Its exact function has not yet been verified. | unverified |
| EVI Open Env.Cl | Manufacturer setting EVI Open Env.Cl in vapor injection. Its exact function has not yet been verified. | unverified |
| EVI Degree Diff | Difference used by the vapor-injection degree controller. The reference signal is unverified. | label inferred |
| Cold I.Open OD% | Vapor-injection opening setting for Cold I.Open OD%. The opening scale and exact condition are unverified. | label inferred |
| Heat I.Open OD1% | Vapor-injection opening setting for Heat I.Open OD1%. The opening scale and exact condition are unverified. | label inferred |
| Heat I.Open OD2% | Vapor-injection opening setting for Heat I.Open OD2%. The opening scale and exact condition are unverified. | label inferred |
| Heat I.Open OD3% | Vapor-injection opening setting for Heat I.Open OD3%. The opening scale and exact condition are unverified. | label inferred |
| Heat I.Open OD4% | Vapor-injection opening setting for Heat I.Open OD4%. The opening scale and exact condition are unverified. | label inferred |
| Cold ExhOV Open | Vapor-injection opening setting for Cold ExhOV Open. The opening scale and exact condition are unverified. | label inferred |
| Heat ExhOV Open | Vapor-injection opening setting for Heat ExhOV Open. The opening scale and exact condition are unverified. | label inferred |
| Adjust Period | Control-loop update or adjustment interval. The timer scale is unverified. | label inferred |
| Proportional | Proportional response factor for this control loop. The gain scale is unverified. | label inferred |
| Integral  Tm | Integral-response setting for this control loop; it adjusts accumulated-error response. The scale is unverified. | label inferred |
| DerivativeTm | Derivative-response setting for this control loop; it relates to error-change response. The scale is unverified. | label inferred |
| MotionPeriod | Control-loop update or adjustment interval. The timer scale is unverified. | label inferred |
| Calcu.Period | Control-loop update or adjustment interval. The timer scale is unverified. | label inferred |
| P Coef. | Proportional response factor for this control loop. The gain scale is unverified. | label inferred |
| I Coef. | Integral-response setting for this control loop; it adjusts accumulated-error response. The scale is unverified. | label inferred |
| Line SetD 1 | Manufacturer setting Line SetD 1 in vapor injection. Its exact function has not yet been verified. | unverified |
| Line SetD 2 | Manufacturer setting Line SetD 2 in vapor injection. Its exact function has not yet been verified. | unverified |
| Setdegree 1 | Vapor-injection target setting named Setdegree 1. The temperature or degree scale is unverified. | label inferred |
| Setdegree 2 | Vapor-injection target setting named Setdegree 2. The temperature or degree scale is unverified. | label inferred |
| Exh SV Max | Vapor-injection target setting named Exh SV Max. The temperature or degree scale is unverified. | label inferred |
| Exh SV Cold | Vapor-injection target setting named Exh SV Cold. The temperature or degree scale is unverified. | label inferred |
| ExhSvTempCoef | Vapor-injection target setting named ExhSvTempCoef. The temperature or degree scale is unverified. | label inferred |
| Exh SV Heat1 | Vapor-injection target setting named Exh SV Heat1. The temperature or degree scale is unverified. | label inferred |
| Exh SV Heat2 | Vapor-injection target setting named Exh SV Heat2. The temperature or degree scale is unverified. | label inferred |
| Exh SV Heat3 | Vapor-injection target setting named Exh SV Heat3. The temperature or degree scale is unverified. | label inferred |
| Exh SV Heat4 | Vapor-injection target setting named Exh SV Heat4. The temperature or degree scale is unverified. | label inferred |
| Exh SV Heat5 | Vapor-injection target setting named Exh SV Heat5. The temperature or degree scale is unverified. | label inferred |
| EVI Open Rps | Compressor-speed criterion for opening vapor injection. The speed scale is unverified. | label inferred |
| EVI Close Rps | Compressor-speed criterion for closing vapor injection. The speed scale is unverified. | label inferred |
| ExhOV Open Diff | Vapor-injection opening setting for ExhOV Open Diff. The opening scale and exact condition are unverified. | label inferred |
| EVI Exh Diff | Exhaust-temperature difference setting in vapor-injection control. Its scale is unverified. | label inferred |
| Heat EVI A1 | Vapor-injection service-table value for Heat EVI A1. The named operating point is manufacturer-specific. | label inferred |
| Heat EVI B1 | Vapor-injection service-table value for Heat EVI B1. The named operating point is manufacturer-specific. | label inferred |
| Heat EVI E1 | Vapor-injection service-table value for Heat EVI E1. The named operating point is manufacturer-specific. | label inferred |
| Heat EVI G1 | Vapor-injection service-table value for Heat EVI G1. The named operating point is manufacturer-specific. | label inferred |
| Heat EVI C1 | Vapor-injection service-table value for Heat EVI C1. The named operating point is manufacturer-specific. | label inferred |
| Heat EVI D1 | Vapor-injection service-table value for Heat EVI D1. The named operating point is manufacturer-specific. | label inferred |
| Cool EVI | Vapor-injection service-table value for Cool EVI. The named operating point is manufacturer-specific. | label inferred |
| Exh SV Min | Vapor-injection target setting named Exh SV Min. The temperature or degree scale is unverified. | label inferred |
| Freq ExhSV Coef | Manufacturer setting Freq ExhSV Coef in vapor injection. Its exact function has not yet been verified. | unverified |
| EVI Open In.Cl | Inlet-related vapor-injection opening criterion in cooling. The reference sensor is unverified. | label inferred |

## Defrost

Defrost timing, temperature criteria, termination and drainage settings.

| Parameter | English explanation | Confidence |
|---|---|---|
| Dfr.Interval | Interval setting between defrost operations. The timer scale and eligibility rules are unverified. | label inferred |
| Dfr.Time | Defrost-duration setting. The timer scale and exact duration limit are unverified. | label inferred |
| Dfr.Time Cnt | Defrost timing/count setting. Its exact use and timer scale are unverified. | label inferred |
| Dfr. Env.T | Ambient-temperature criterion used by defrost control. The exact trigger is unverified. | label inferred |
| Dfr. Coil T | Coil-temperature criterion used by defrost control. The exact trigger is unverified. | label inferred |
| Dfr.Coil T | Coil-temperature criterion used by defrost control. The exact trigger is unverified. | label inferred |
| Dfr.Out T | Outlet-temperature criterion used by defrost control. The exact termination rule is unverified. | label inferred |
| EWD.SmartDfr | Configures the manufacturer's smart-defrost function. The numeric choices are unverified. | label inferred |
| Frost D1 | Defrost criterion or sequence setting named Frost D1. Its exact trigger, timer or scale is unverified. | label inferred |
| Frost D2 | Defrost criterion or sequence setting named Frost D2. Its exact trigger, timer or scale is unverified. | label inferred |
| T. Sure Time | Confirmation time for a defrost condition. The timer scale is unverified. | label inferred |
| Dfr.Env.T.1 | Defrost criterion or sequence setting named Dfr.Env.T.1. Its exact trigger, timer or scale is unverified. | label inferred |
| Dfr.Env.T.2 | Defrost criterion or sequence setting named Dfr.Env.T.2. Its exact trigger, timer or scale is unverified. | label inferred |
| Dfr.Env.T.3 | Defrost criterion or sequence setting named Dfr.Env.T.3. Its exact trigger, timer or scale is unverified. | label inferred |
| Dfr.Env.T.4 | Defrost criterion or sequence setting named Dfr.Env.T.4. Its exact trigger, timer or scale is unverified. | label inferred |
| Dfr.Inte. 1 | Defrost criterion or sequence setting named Dfr.Inte. 1. Its exact trigger, timer or scale is unverified. | label inferred |
| Dfr.Inte. 2 | Defrost criterion or sequence setting named Dfr.Inte. 2. Its exact trigger, timer or scale is unverified. | label inferred |
| Dfr.Inte. 3 | Defrost criterion or sequence setting named Dfr.Inte. 3. Its exact trigger, timer or scale is unverified. | label inferred |
| Dfr.Inte. 4 | Defrost criterion or sequence setting named Dfr.Inte. 4. Its exact trigger, timer or scale is unverified. | label inferred |
| Dfr.Inte. 5 | Defrost criterion or sequence setting named Dfr.Inte. 5. Its exact trigger, timer or scale is unverified. | label inferred |
| Dfr.T.Diff 1 | Defrost criterion or sequence setting named Dfr.T.Diff 1. Its exact trigger, timer or scale is unverified. | label inferred |
| Dfr.T.Diff 2 | Defrost criterion or sequence setting named Dfr.T.Diff 2. Its exact trigger, timer or scale is unverified. | label inferred |
| Dfr.T.Diff 3 | Defrost criterion or sequence setting named Dfr.T.Diff 3. Its exact trigger, timer or scale is unverified. | label inferred |
| Dfr.T.Diff 4 | Defrost criterion or sequence setting named Dfr.T.Diff 4. Its exact trigger, timer or scale is unverified. | label inferred |
| Dfr.T.Diff 5 | Defrost criterion or sequence setting named Dfr.T.Diff 5. Its exact trigger, timer or scale is unverified. | label inferred |
| LP.Dfr.Dect. | Low-pressure criterion associated with defrost detection. The exact rule is unverified. | label inferred |
| Dfr.Time Cnt | Defrost timing/count setting. Its exact use and timer scale are unverified. | label inferred |
| LP.Dfr.Cycle | Cycle setting for low-pressure-based defrost control. The timer scale is unverified. | label inferred |
| LP.Dfr.CoilT | Coil-temperature criterion for low-pressure-based defrost control. | label inferred |
| TimingDefrost | Configures timer-based defrost operation. The numeric choices are unverified. | label inferred |
| Emerg EWD | Emergency setting associated with the EWD defrost function. The choice codes are unverified. | label inferred |
| DfrStopCm. V | Defrost criterion or sequence setting named DfrStopCm. V. Its exact trigger, timer or scale is unverified. | label inferred |
| DfrStopCm.T1 | Defrost criterion or sequence setting named DfrStopCm.T1. Its exact trigger, timer or scale is unverified. | label inferred |
| DfrStopV.T1 | Defrost criterion or sequence setting named DfrStopV.T1. Its exact trigger, timer or scale is unverified. | label inferred |
| DfrStopCm.T2 | Defrost criterion or sequence setting named DfrStopCm.T2. Its exact trigger, timer or scale is unverified. | label inferred |
| DfrStopV.T2 | Defrost criterion or sequence setting named DfrStopV.T2. Its exact trigger, timer or scale is unverified. | label inferred |
| DfrStopFreq | Compressor frequency setting associated with defrost termination. The scale is unverified. | label inferred |
| DrippingTime | Drainage/dripping time associated with defrost completion. The timer scale is unverified. | label inferred |
| DFR.OP.AUXH.T | Auxiliary-heater temperature criterion during defrost operation. | label inferred |

## Frost & hydraulics

Frost prevention, water-pump response, fan-coil and sterilization settings.

| Parameter | English explanation | Confidence |
|---|---|---|
| Atfr.Inte. 1 | Antifreeze operating criterion named Atfr.Inte. 1. The reference signal, trigger or timer scale is unverified. | label inferred |
| Atfr.Inte. 2 | Antifreeze operating criterion named Atfr.Inte. 2. The reference signal, trigger or timer scale is unverified. | label inferred |
| Atfr.Pump T | Antifreeze operating criterion named Atfr.Pump T. The reference signal, trigger or timer scale is unverified. | label inferred |
| Atfr.Heat T | Antifreeze operating criterion named Atfr.Heat T. The reference signal, trigger or timer scale is unverified. | label inferred |
| Atfr.Comp.T | Antifreeze operating criterion named Atfr.Comp.T. The reference signal, trigger or timer scale is unverified. | label inferred |
| Atfr.Heat Out.T | Antifreeze operating criterion named Atfr.Heat Out.T. The reference signal, trigger or timer scale is unverified. | label inferred |
| Atfr.Comp Out.T | Antifreeze operating criterion named Atfr.Comp Out.T. The reference signal, trigger or timer scale is unverified. | label inferred |
| Atfr.Amb.T | Antifreeze operating criterion named Atfr.Amb.T. The reference signal, trigger or timer scale is unverified. | label inferred |
| Atfr.Enter.T | Antifreeze operating criterion named Atfr.Enter.T. The reference signal, trigger or timer scale is unverified. | label inferred |
| Atfr.AmbDiff | Antifreeze operating criterion named Atfr.AmbDiff. The reference signal, trigger or timer scale is unverified. | label inferred |
| Atfr.Enable | Configures antifreeze operation. The numeric enable or mode codes are unverified. | label inferred |
| ExitWarmEnv.Dif | Manufacturer setting ExitWarmEnv.Dif in frost & hydraulics. Its exact function has not yet been verified. | unverified |
| Sterilization Temp | Temperature target associated with hot-water sterilization. Its scale is unverified. | label inferred |
| Steril-maximum Cycle | Maximum interval/cycle setting for hot-water sterilization. The timer scale is unverified. | label inferred |
| Steril-high Temp Time | High-temperature hold time for hot-water sterilization. The timer scale is unverified. | label inferred |
| TBH On Dly | Delay associated with TBH On Dly. The timer unit and exact switching condition are unverified. | label inferred |
| PUMPF.Ctrl | Water-pump control strategy. The numeric strategy codes are unverified. | label inferred |
| PUMPF Model | Water-pump model or drive profile. The model-code table is unverified. | label inferred |
| PUMPF Set LH | Water-pump setting labelled LH. Its exact signal and scale are unverified. | label inferred |
| PMF.Set.Flow | Target flow setting for water-pump control. The flow unit and scale are unverified. | label inferred |
| Fcu.Num | Number-of-fan-coils configuration. The encoding is unverified. | label inferred |
| Fcu.Addr | Fan-coil communication address setting. | label inferred |
| M.Start.S | Manufacturer setting M.Start.S in frost & hydraulics. Its exact function has not yet been verified. | unverified |
| M.Close.S | Manufacturer setting M.Close.S in frost & hydraulics. Its exact function has not yet been verified. | unverified |
| S.Start.M | Manufacturer setting S.Start.M in frost & hydraulics. Its exact function has not yet been verified. | unverified |
| Fcu.Mode.Set | Fan-coil operating-mode configuration. The numeric mode codes are unverified. | label inferred |
| Fcu.Egy.Cpst | Manufacturer setting Fcu.Egy.Cpst in frost & hydraulics. Its exact function has not yet been verified. | unverified |
| Obj.Egy.Cpst | Manufacturer setting Obj.Egy.Cpst in frost & hydraulics. Its exact function has not yet been verified. | unverified |
| Fcu_Heat_Env | Manufacturer setting Fcu_Heat_Env in frost & hydraulics. Its exact function has not yet been verified. | unverified |
| Fcu_Cool_Env | Manufacturer setting Fcu_Cool_Env in frost & hydraulics. Its exact function has not yet been verified. | unverified |
| Pumpf Start Speed | Water-pump startup speed setting. The speed scale is unverified. | label inferred |
| Pumpf.Debug | Water-pump service/debug configuration. The numeric choices are unverified. | label inferred |
| PUMPF.SetRate | Water-pump drive-rate request. The raw-to-speed or duty conversion is unverified. | label inferred |
| PUMPF.MaxRate | Upper water-pump drive-rate setting. Its scale is unverified. | label inferred |
| PUMPF.Period | Water-pump control update-period setting. The timer scale is unverified. | label inferred |
| Pumpf.DebugRate | Water-pump drive rate in service/debug operation. Its scale is unverified. | label inferred |
| Exp.Tk.Ta | External-tank or auxiliary-heat criterion named Exp.Tk.Ta. The sensor assignment and scale are unverified. | label inferred |
| Exp.Tk.Ta.L | External-tank or auxiliary-heat criterion named Exp.Tk.Ta.L. The sensor assignment and scale are unverified. | label inferred |
| Exp.Tk.AHS.On | External-tank or auxiliary-heat criterion named Exp.Tk.AHS.On. The sensor assignment and scale are unverified. | label inferred |
| Exp.Tk.AHS.Off | External-tank or auxiliary-heat criterion named Exp.Tk.AHS.Off. The sensor assignment and scale are unverified. | label inferred |
| AC_HT_CM_TIME | Manufacturer setting AC_HT_CM_TIME in frost & hydraulics. Its exact function has not yet been verified. | unverified |
| Fac_Pass_Word_Set | Manufacturer service-password setting. Its encoding and application are unverified. | label inferred |
| Pumpf Temp Diff | Temperature difference associated with water-pump speed control. The scale is unverified. | label inferred |
| Pumpf Speed_Up Cycle | Water-pump adjustment interval when increasing speed. The raw scale is unverified. | label inferred |
| Pumpf Speed_Up Scale | Water-pump adjustment amount when increasing speed. The raw scale is unverified. | label inferred |
| Pumpf Speed_Down Cycle | Water-pump adjustment interval when decreasing speed. The raw scale is unverified. | label inferred |
| Pumpf Speed_Down Scale | Water-pump adjustment amount when decreasing speed. The raw scale is unverified. | label inferred |
| MIN Traffic Limit | Minimum-flow or traffic-limit setting. The physical quantity and scale are unverified. | label inferred |

## Protection

Alarm delays, temperature and current criteria, reset and interlock settings.

| Parameter | English explanation | Confidence |
|---|---|---|
| Error Dly | Delay before a fault condition is accepted. The timer scale and affected faults are unverified. | label inferred |
| Flow Err Dly | Delay before a water-flow fault is accepted. The timer scale is unverified. | label inferred |
| Auto.Reset | Automatic fault-reset configuration. The numeric choices are unverified. | label inferred |
| Auto.Re.Awed | Manufacturer automatic-reset allowance setting. The exact code meaning is unverified. | label inferred |
| LP.Alarm Dly | Delay associated with LP.Alarm Dly. The timer unit and exact switching condition are unverified. | label inferred |
| LP.Dly Defro | Delay associated with LP.Dly Defro. The timer unit and exact switching condition are unverified. | label inferred |
| Cool LP Dly. | Delay associated with Cool LP Dly.. The timer unit and exact switching condition are unverified. | label inferred |
| Heat LP Dly. | Delay associated with Heat LP Dly.. The timer unit and exact switching condition are unverified. | label inferred |
| Exit T. Diff | Temperature difference used for leaving a protection state. The reference sensor is unverified. | label inferred |
| Air Cool Low | Ambient-temperature operating/protection criterion named Air Cool Low. Its threshold direction and scale are unverified. | label inferred |
| Air Heat Hihg1 | Ambient-temperature operating/protection criterion named Air Heat Hihg1. Its threshold direction and scale are unverified. | label inferred |
| CantOnEnvCool | Ambient-temperature operating/protection criterion named CantOnEnvCool. Its threshold direction and scale are unverified. | label inferred |
| OutInDiffErr | Outlet/inlet temperature-difference protection criterion. The scale is unverified. | label inferred |
| GasInOutErr | Gas inlet/outlet difference protection criterion. The scale is unverified. | label inferred |
| Comp. Cu.Low | Manufacturer setting Comp. Cu.Low in protection. Its exact function has not yet been verified. | unverified |
| Cu.Dete. Dly | Delay associated with Cu.Dete. Dly. The timer unit and exact switching condition are unverified. | label inferred |
| Current Type | Current measurement or protection input type. The numeric choices are unverified. | label inferred |
| OutInDiffHigh | High outlet/inlet temperature-difference criterion. The exact action is unverified. | label inferred |
| CoolEvapLow | Low evaporating-temperature protection criterion during cooling. | label inferred |
| Exh Too High | High discharge/exhaust-temperature protection setting. The scale is unverified. | label inferred |
| Out Exh.H Diff | Manufacturer setting Out Exh.H Diff in protection. Its exact function has not yet been verified. | unverified |
| CoolGasInLow | Low inlet-gas temperature criterion during cooling. | label inferred |
| PwmSpeedTooLow | Manufacturer setting PwmSpeedTooLow in protection. Its exact function has not yet been verified. | unverified |
| PwmSpeedDly | Delay associated with PwmSpeedDly. The timer unit and exact switching condition are unverified. | label inferred |
| CmOffcheckLp | Low-pressure check associated with compressor-off operation. | label inferred |
| Air Heat High2 | Ambient-temperature operating/protection criterion named Air Heat High2. Its threshold direction and scale are unverified. | label inferred |
| Air Heat High3 | Ambient-temperature operating/protection criterion named Air Heat High3. Its threshold direction and scale are unverified. | label inferred |
| Air Heat High4 | Ambient-temperature operating/protection criterion named Air Heat High4. Its threshold direction and scale are unverified. | label inferred |
| Low Amb. 1 | Ambient-temperature operating/protection criterion named Low Amb. 1. Its threshold direction and scale are unverified. | label inferred |
| Low Amb. 2 | Ambient-temperature operating/protection criterion named Low Amb. 2. Its threshold direction and scale are unverified. | label inferred |
| Low Amb. 3 | Ambient-temperature operating/protection criterion named Low Amb. 3. Its threshold direction and scale are unverified. | label inferred |
| Low Amb.T1 | Ambient-temperature operating/protection criterion named Low Amb.T1. Its threshold direction and scale are unverified. | label inferred |
| Low Amb.T2 | Ambient-temperature operating/protection criterion named Low Amb.T2. Its threshold direction and scale are unverified. | label inferred |
| Low Amb.T3 | Ambient-temperature operating/protection criterion named Low Amb.T3. Its threshold direction and scale are unverified. | label inferred |
| Low Amb.T4 | Ambient-temperature operating/protection criterion named Low Amb.T4. Its threshold direction and scale are unverified. | label inferred |
| C#9_TA_C1 | Protection-curve entry C#9_TA_C1. The exact condition and raw scaling are unverified. | label inferred |
| C#9_TA_C2 | Protection-curve entry C#9_TA_C2. The exact condition and raw scaling are unverified. | label inferred |
| C#9_TWout2_C1 | Protection-curve entry C#9_TWout2_C1. The exact condition and raw scaling are unverified. | label inferred |
| C#9_TWout2_C2 | Protection-curve entry C#9_TWout2_C2. The exact condition and raw scaling are unverified. | label inferred |
| C#9_TA_H1 | Protection-curve entry C#9_TA_H1. The exact condition and raw scaling are unverified. | label inferred |
| C#9_TA_H2 | Protection-curve entry C#9_TA_H2. The exact condition and raw scaling are unverified. | label inferred |
| C#9_TWout2_H1 | Protection-curve entry C#9_TWout2_H1. The exact condition and raw scaling are unverified. | label inferred |
| C#9_TWout2_H2 | Protection-curve entry C#9_TWout2_H2. The exact condition and raw scaling are unverified. | label inferred |
| SMART_GRID_CFG | Smart-grid input/operating configuration. The numeric choices are unverified. | label inferred |
| SMART_GRID | Smart-grid operating setting. The numeric choices are unverified. | label inferred |
| ECO_RUN_TIME | Economy-mode run-time setting. The timer scale is unverified. | label inferred |
| Reote_Interlock_Delay | External interlock delay. The timer scale and input polarity are unverified. | label inferred |
| Refrigerant Gas Conc High | High refrigerant-gas concentration protection setting. The concentration scale is unverified. | label inferred |

## Inputs & sensors

Input assignments, temperature offsets, power estimates and sensor configuration.

| Parameter | English explanation | Confidence |
|---|---|---|
| Comp. LP | Configuration of the compressor low-pressure input. This is a setting, not a pressure measurement. | label inferred |
| Comp. HP | Configuration of the compressor high-pressure input. This is a setting, not a pressure measurement. | label inferred |
| Fan Overload | Configuration of the fan overload input. The input polarity is unverified. | label inferred |
| Water Flow | Configuration of the water-flow input. This is a setting, not a measured flow value. | label inferred |
| Power Err | Configuration of the electrical-supply fault input. Its polarity is unverified. | label inferred |
| TBH Over Load | Configuration of the tank/backup-heater overload input. Its polarity is unverified. | label inferred |
| Sub Freq | Configuration of the secondary frequency function. Its exact assignment is unverified. | label inferred |
| TmpInCpst | Compensation offset for inlet-water temperature. The calibration scale is unverified. | label inferred |
| TmpOutCpst | Compensation offset for outlet-water temperature. The calibration scale is unverified. | label inferred |
| TmpEnvCpst | Compensation offset for ambient temperature. The calibration scale is unverified. | label inferred |
| AntiIceCpst | Compensation offset for antifreeze temperature. The calibration scale is unverified. | label inferred |
| WingCpst | Compensation offset for the temperature signal named Wing. The calibration scale is unverified. | label inferred |
| GasOutCpst | Compensation offset for outlet-gas temperature. The calibration scale is unverified. | label inferred |
| GasInCpst | Compensation offset for inlet-gas temperature. The calibration scale is unverified. | label inferred |
| ValveCpst | Compensation offset for the valve-related temperature. The calibration scale is unverified. | label inferred |
| EcoOutCpst | Compensation offset for economizer outlet temperature. The calibration scale is unverified. | label inferred |
| EcoInCpst | Compensation offset for economizer inlet temperature. The calibration scale is unverified. | label inferred |
| CmTopCpst | Compensation offset for compressor-top temperature. The calibration scale is unverified. | label inferred |
| AntiIceSet | Antifreeze sensor/control configuration. The numeric choices are unverified. | label inferred |
| CompTopSet | Compressor-top sensor/control configuration. The numeric choices are unverified. | label inferred |
| EVI.TempDisp | Vapor-injection temperature display configuration. The choice codes are unverified. | label inferred |
| DHW.Cpst | Compensation offset for domestic-hot-water temperature. The calibration scale is unverified. | label inferred |
| TACtSet | Sensor/input configuration named TACtSet. The assignment is unverified. | label inferred |
| LDIevu_DI_TYPE | Input/output assignment for LDIevu_DI_TYPE. The numeric signal or function choices are unverified. | label inferred |
| LDIsg_DI_TYPE | Input/output assignment for LDIsg_DI_TYPE. The numeric signal or function choices are unverified. | label inferred |
| DI4_Selfdef | Input/output assignment for DI4_Selfdef. The numeric signal or function choices are unverified. | label inferred |
| DI6_Selfdef | Input/output assignment for DI6_Selfdef. The numeric signal or function choices are unverified. | label inferred |
| EAH OL | Manufacturer setting EAH OL in inputs & sensors. Its exact function has not yet been verified. | unverified |
| DISPLAY.LOGO | Controller display-logo configuration. The numeric choices are unverified. | label inferred |
| Idu_Odu_Function | Indoor/outdoor unit function assignment. The numeric choices are unverified. | label inferred |
| Out_DO1_Selfdef | Input/output assignment for Out_DO1_Selfdef. The numeric signal or function choices are unverified. | label inferred |
| FAN POWER | Configured power value for fan. This is a setting, not measured electrical power. | label inferred |
| PUMP POWER | Configured power value for pump. This is a setting, not measured electrical power. | label inferred |
| EAH1 POWER | Configured power value for eah1. This is a setting, not measured electrical power. | label inferred |
| IDLE POWER | Configured power value for idle. This is a setting, not measured electrical power. | label inferred |
| OTHER RUN POWER | Configured power value for other run. This is a setting, not measured electrical power. | label inferred |
| CAP_EVI_COEF | Capacity-estimation adjustment named CAP_EVI_COEF. Its coefficient or compensation scale is unverified. | label inferred |
| CAP_INTE_COEF | Capacity-estimation adjustment named CAP_INTE_COEF. Its coefficient or compensation scale is unverified. | label inferred |
| CAP_HIGH_CPST | Capacity-estimation adjustment named CAP_HIGH_CPST. Its coefficient or compensation scale is unverified. | label inferred |
| CAP_LOW_CPST | Capacity-estimation adjustment named CAP_LOW_CPST. Its coefficient or compensation scale is unverified. | label inferred |
| Power Down Dly | Shutdown delay associated with power-down operation. The timer scale is unverified. | label inferred |
| Language Option | Controller language selection. The numeric language codes have not been mapped. | label inferred |
| DO9_Selfdef | Input/output assignment for DO9_Selfdef. The numeric signal or function choices are unverified. | label inferred |
| PUMPret Enable | Return/recirculation-pump function configuration. The choice codes are unverified. | label inferred |
| PUMPret Run Time | Return/recirculation-pump operating time. The timer scale is unverified. | label inferred |
| PUMPret Disinfect | Return/recirculation-pump behaviour during disinfection. The choice codes are unverified. | label inferred |
| PUMPret Timer | Return/recirculation-pump timer configuration. The encoding is unverified. | label inferred |
| TWout2_SENSOR | Configuration of the second outlet-water temperature sensor. The choice codes are unverified. | label inferred |

## Service tables 1

Manufacturer service and test-point table entries. They are settings, not live measurements.

| Parameter | English explanation | Confidence |
|---|---|---|
| Debug Set. | Manufacturer service/debug mode configuration. The numeric choices are unverified. | label inferred |
| Heat Comp A1 | Heating service-table entry Comp A1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Fan A1 | Heating service-table entry Fan A1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat EEV A1 | Heating service-table entry EEV A1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Comp B1 | Heating service-table entry Comp B1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Fan B1 | Heating service-table entry Fan B1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat EEV B1 | Heating service-table entry EEV B1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Comp E1 | Heating service-table entry Comp E1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Fan E1 | Heating service-table entry Fan E1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat EEV E1 | Heating service-table entry EEV E1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Comp G1 | Heating service-table entry Comp G1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Fan G1 | Heating service-table entry Fan G1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat EEV G1 | Heating service-table entry EEV G1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Comp C1 | Heating service-table entry Comp C1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Fan C1 | Heating service-table entry Fan C1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat EEV C1 | Heating service-table entry EEV C1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Comp D1 | Heating service-table entry Comp D1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Fan D1 | Heating service-table entry Fan D1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat EEV D1 | Heating service-table entry EEV D1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Cool Comp | Cooling service-table entry for comp. The operating point and scale are unverified. | label inferred |
| Cool Fan | Cooling service-table entry for fan. The operating point and scale are unverified. | label inferred |
| Cool EEV | Cooling service-table entry for eev. The operating point and scale are unverified. | label inferred |
| Heat EWD1 A1 | Heating service-table entry EWD1 A1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Itvl A1 | Heating service-table entry Itvl A1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Step A1 | Heating service-table entry Step A1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Freq A1 | Heating service-table entry Freq A1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Wing A1 | Heating service-table entry Wing A1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Time A1 | Heating service-table entry Time A1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat EWD1 B1 | Heating service-table entry EWD1 B1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Itvl B1 | Heating service-table entry Itvl B1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Step B1 | Heating service-table entry Step B1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Freq B1 | Heating service-table entry Freq B1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Wing B1 | Heating service-table entry Wing B1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Time B1 | Heating service-table entry Time B1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat EWD1 E1 | Heating service-table entry EWD1 E1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Itvl E1 | Heating service-table entry Itvl E1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Step E1 | Heating service-table entry Step E1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Freq E1 | Heating service-table entry Freq E1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Wing E1 | Heating service-table entry Wing E1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Time E1 | Heating service-table entry Time E1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat EWD1 G1 | Heating service-table entry EWD1 G1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Itvl G1 | Heating service-table entry Itvl G1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Step G1 | Heating service-table entry Step G1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Freq G1 | Heating service-table entry Freq G1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Wing G1 | Heating service-table entry Wing G1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Time G1 | Heating service-table entry Time G1. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Pumpf_Sv_X1 | Water-pump service/setpoint table entry X1. The raw scale is unverified. | label inferred |
| Pumpf_Sv_X2 | Water-pump service/setpoint table entry X2. The raw scale is unverified. | label inferred |

## Service tables 2

The second service table, including heating and EVI test-point settings.

| Parameter | English explanation | Confidence |
|---|---|---|
| Heat Comp A2 | Heating service-table entry Comp A2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Fan A2 | Heating service-table entry Fan A2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat EEV A2 | Heating service-table entry EEV A2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Comp B2 | Heating service-table entry Comp B2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Fan B2 | Heating service-table entry Fan B2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat EEV B2 | Heating service-table entry EEV B2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Comp E2 | Heating service-table entry Comp E2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Fan E2 | Heating service-table entry Fan E2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat EEV E2 | Heating service-table entry EEV E2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Comp G2 | Heating service-table entry Comp G2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Fan G2 | Heating service-table entry Fan G2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat EEV G2 | Heating service-table entry EEV G2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Comp C2 | Heating service-table entry Comp C2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Fan C2 | Heating service-table entry Fan C2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat EEV C2 | Heating service-table entry EEV C2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Comp D2 | Heating service-table entry Comp D2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Fan D2 | Heating service-table entry Fan D2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat EEV D2 | Heating service-table entry EEV D2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat EWD1 A2 | Heating service-table entry EWD1 A2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Itvl A2 | Heating service-table entry Itvl A2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Step A2 | Heating service-table entry Step A2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Freq A2 | Heating service-table entry Freq A2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Wing A2 | Heating service-table entry Wing A2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Time A2 | Heating service-table entry Time A2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat EWD1 B2 | Heating service-table entry EWD1 B2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Itvl B2 | Heating service-table entry Itvl B2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Step B2 | Heating service-table entry Step B2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Freq B2 | Heating service-table entry Freq B2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Wing B2 | Heating service-table entry Wing B2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Time B2 | Heating service-table entry Time B2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat EWD1 E2 | Heating service-table entry EWD1 E2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Itvl E2 | Heating service-table entry Itvl E2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Step E2 | Heating service-table entry Step E2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Freq E2 | Heating service-table entry Freq E2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Wing E2 | Heating service-table entry Wing E2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Time E2 | Heating service-table entry Time E2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat EWD1 G2 | Heating service-table entry EWD1 G2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Itvl G2 | Heating service-table entry Itvl G2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Step G2 | Heating service-table entry Step G2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Freq G2 | Heating service-table entry Freq G2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Wing G2 | Heating service-table entry Wing G2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat Time G2 | Heating service-table entry Time G2. The manufacturer-specific operating point and scale are unverified. | label inferred |
| Heat EVI A2 | Vapor-injection service-table value for Heat EVI A2. The named operating point is manufacturer-specific. | label inferred |
| Heat EVI B2 | Vapor-injection service-table value for Heat EVI B2. The named operating point is manufacturer-specific. | label inferred |
| Heat EVI E2 | Vapor-injection service-table value for Heat EVI E2. The named operating point is manufacturer-specific. | label inferred |
| Heat EVI G2 | Vapor-injection service-table value for Heat EVI G2. The named operating point is manufacturer-specific. | label inferred |
| Heat EVI C2 | Vapor-injection service-table value for Heat EVI C2. The named operating point is manufacturer-specific. | label inferred |
| Heat EVI D2 | Vapor-injection service-table value for Heat EVI D2. The named operating point is manufacturer-specific. | label inferred |

## Pressure & pump drive

Pressure/flow sensor calibration and pump motor or inverter configuration.

| Parameter | English explanation | Confidence |
|---|---|---|
| LP Sensor Type | Low-pressure sensor model/type configuration. The numeric sensor codes are unverified. | label inferred |
| HP Sensor Type | High-pressure sensor model/type configuration. The numeric sensor codes are unverified. | label inferred |
| LP Range Min. | Low-pressure sensor calibration-range lower endpoint. The raw-to-physical conversion is unverified. | label inferred |
| LP Range Max. | Low-pressure sensor calibration-range upper endpoint. The raw-to-physical conversion is unverified. | label inferred |
| HP Range Min. | High-pressure sensor calibration-range lower endpoint. The raw-to-physical conversion is unverified. | label inferred |
| HP Range Max. | High-pressure sensor calibration-range upper endpoint. The raw-to-physical conversion is unverified. | label inferred |
| Cool LP Set | Pressure-control threshold or difference named Cool LP Set. The pressure scale and exact action are unverified. | label inferred |
| Heat LP Set | Pressure-control threshold or difference named Heat LP Set. The pressure scale and exact action are unverified. | label inferred |
| Cool HP Set | Pressure-control threshold or difference named Cool HP Set. The pressure scale and exact action are unverified. | label inferred |
| Heat HP Set | Pressure-control threshold or difference named Heat HP Set. The pressure scale and exact action are unverified. | label inferred |
| LP Reset Diff | Pressure-control threshold or difference named LP Reset Diff. The pressure scale and exact action are unverified. | label inferred |
| HP Reset Diff | Pressure-control threshold or difference named HP Reset Diff. The pressure scale and exact action are unverified. | label inferred |
| HP Adjust Diff | Pressure-control threshold or difference named HP Adjust Diff. The pressure scale and exact action are unverified. | label inferred |
| HP LimAdd Diff | Pressure-control threshold or difference named HP LimAdd Diff. The pressure scale and exact action are unverified. | label inferred |
| HP ForSub Diff | Pressure-control threshold or difference named HP ForSub Diff. The pressure scale and exact action are unverified. | label inferred |
| LP Adjust Diff | Pressure-control threshold or difference named LP Adjust Diff. The pressure scale and exact action are unverified. | label inferred |
| LP LimAdd Diff | Pressure-control threshold or difference named LP LimAdd Diff. The pressure scale and exact action are unverified. | label inferred |
| LP ForSub Diff | Pressure-control threshold or difference named LP ForSub Diff. The pressure scale and exact action are unverified. | label inferred |
| Flow Sensor Type | Flow-sensor model/type configuration. The numeric sensor codes are unverified. | label inferred |
| Flow Sensor Range Min | Flow sensor calibration-range lower endpoint. The raw-to-physical conversion is unverified. | label inferred |
| Flow Sensor Range Max | Flow sensor calibration-range upper endpoint. The raw-to-physical conversion is unverified. | label inferred |
| Ref Leakage Sensor Code | Refrigerant-leak sensor model/profile code. The numeric code table is unverified. | label inferred |
| Ref Leakage Sensor Base Addr | Base communication address of the refrigerant-leak sensor. | label inferred |
| Smart Ele Meter Code | Electrical meter model/profile code. The numeric code table is unverified. | label inferred |
| Smart Ele Meter Addr | Electrical meter communication address setting. | label inferred |
| FreqPmfSet | Frequency-controlled water-pump configuration. The numeric choices are unverified. | label inferred |
| FreqPmfAddr | Communication address of the frequency-controlled water pump. | label inferred |
| PM Max Freq | Manufacturer setting PM Max Freq in pressure & pump drive. Its exact function has not yet been verified. | unverified |
| PM Min Freq | Manufacturer setting PM Min Freq in pressure & pump drive. Its exact function has not yet been verified. | unverified |
| PWM Pm Type | PWM water-pump interface type. The numeric choices are unverified. | label inferred |
| Volt Pump Type | Voltage-controlled water-pump interface type. The numeric choices are unverified. | label inferred |
| PM Init Speed | Initial water-pump speed request. The drive-rate scale is unverified. | label inferred |
| PM Init Hold | Time for holding the initial water-pump speed. The timer scale is unverified. | label inferred |
| PM Run Min | Minimum running water-pump drive rate. The scale is unverified. | label inferred |
| Motor Power(KW) | Pump/inverter motor rated-power configuration. The label names kW but the raw scale is unverified. | label inferred |
| Motor Poles | Motor pole-count configuration for the drive profile. | label inferred |
| Motor Rate Cur | Motor rated-current configuration. The current scale is unverified. | label inferred |
| Motor Rate Freq | Motor rated-frequency configuration. The frequency scale is unverified. | label inferred |
| Motor Rate Spee | Motor rated-speed configuration. The speed scale is unverified. | label inferred |
| Motor Rate Volt | Motor rated-voltage configuration. The voltage scale is unverified. | label inferred |
| Invt Up T1 | Inverter response/transition setting named Invt Up T1. The transition condition and raw scale are unverified. | label inferred |
| Invt Dn T1 | Inverter response/transition setting named Invt Dn T1. The transition condition and raw scale are unverified. | label inferred |
| Invt Up T8 | Inverter response/transition setting named Invt Up T8. The transition condition and raw scale are unverified. | label inferred |
| Invt Dn T8 | Inverter response/transition setting named Invt Dn T8. The transition condition and raw scale are unverified. | label inferred |
| Invt Turn F | Inverter response/transition setting named Invt Turn F. The transition condition and raw scale are unverified. | label inferred |
| Invt VF Curve | Inverter voltage/frequency curve configuration. The curve codes are unverified. | label inferred |
| PWM Fb Reserve | PWM feedback polarity/reserved configuration. The numeric choices are unverified. | label inferred |
| PWM Reserve Out | PWM output polarity/reserved configuration. The numeric choices are unverified. | label inferred |

## Working frequency

All 46 cooling and heating frequency-table entries, arranged by named operating condition.

| Parameter | English explanation | Confidence |
|---|---|---|
| ClUpEnv50In12 | Cooling upper frequency-table entry labelled Env 50, In 12. The condition thresholds and speed units are unverified. | label inferred |
| ClUpEnv43In12 | Cooling upper frequency-table entry labelled Env 43, In 12. The condition thresholds and speed units are unverified. | label inferred |
| ClUpEnv35In12 | Cooling upper frequency-table entry labelled Env 35, In 12. The condition thresholds and speed units are unverified. | label inferred |
| ClUpEnv20In12 | Cooling upper frequency-table entry labelled Env 20, In 12. The condition thresholds and speed units are unverified. | label inferred |
| ClUpEnv50In20 | Cooling upper frequency-table entry labelled Env 50, In 20. The condition thresholds and speed units are unverified. | label inferred |
| ClUpEnv43In20 | Cooling upper frequency-table entry labelled Env 43, In 20. The condition thresholds and speed units are unverified. | label inferred |
| ClUpEnv35In20 | Cooling upper frequency-table entry labelled Env 35, In 20. The condition thresholds and speed units are unverified. | label inferred |
| ClUpEnv20In20 | Cooling upper frequency-table entry labelled Env 20, In 20. The condition thresholds and speed units are unverified. | label inferred |
| ClUpEnv50In35 | Cooling upper frequency-table entry labelled Env 50, In 35. The condition thresholds and speed units are unverified. | label inferred |
| ClUpEnv43In35 | Cooling upper frequency-table entry labelled Env 43, In 35. The condition thresholds and speed units are unverified. | label inferred |
| ClUpEnv35In35 | Cooling upper frequency-table entry labelled Env 35, In 35. The condition thresholds and speed units are unverified. | label inferred |
| ClUpEnv20In35 | Cooling upper frequency-table entry labelled Env 20, In 35. The condition thresholds and speed units are unverified. | label inferred |
| ClDnEnv50 | Cooling lower frequency-table entry labelled Env 50. The condition thresholds and speed units are unverified. | label inferred |
| ClDnEnv43 | Cooling lower frequency-table entry labelled Env 43. The condition thresholds and speed units are unverified. | label inferred |
| ClDnEnv35 | Cooling lower frequency-table entry labelled Env 35. The condition thresholds and speed units are unverified. | label inferred |
| ClDnEnv20 | Cooling lower frequency-table entry labelled Env 20. The condition thresholds and speed units are unverified. | label inferred |
| HtUpEnv28In20(50) | Heating upper frequency-table entry labelled Env 28, In 20(50). The condition thresholds and speed units are unverified. | label inferred |
| HtUpEnv07In20(50) | Heating upper frequency-table entry labelled Env 7, In 20(50). The condition thresholds and speed units are unverified. | label inferred |
| HtUpEnv00In20(50) | Heating upper frequency-table entry labelled Env 0, In 20(50). The condition thresholds and speed units are unverified. | label inferred |
| HtUpEnv-06In20(50) | Heating upper frequency-table entry labelled Env -6, In 20(50). The condition thresholds and speed units are unverified. | label inferred |
| HtUpEnv-12In20(50) | Heating upper frequency-table entry labelled Env -12, In 20(50). The condition thresholds and speed units are unverified. | label inferred |
| HtUpEnv-21In20(50) | Heating upper frequency-table entry labelled Env -21, In 20(50). The condition thresholds and speed units are unverified. | label inferred |
| HtUpEnv28In36(62) | Heating upper frequency-table entry labelled Env 28, In 36(62). The condition thresholds and speed units are unverified. | label inferred |
| HtUpEnv07In36(62) | Heating upper frequency-table entry labelled Env 7, In 36(62). The condition thresholds and speed units are unverified. | label inferred |
| HtUpEnv00In36(62) | Heating upper frequency-table entry labelled Env 0, In 36(62). The condition thresholds and speed units are unverified. | label inferred |
| HtUpEnv-06In36(62) | Heating upper frequency-table entry labelled Env -6, In 36(62). The condition thresholds and speed units are unverified. | label inferred |
| HtUpEnv-12In36(62) | Heating upper frequency-table entry labelled Env -12, In 36(62). The condition thresholds and speed units are unverified. | label inferred |
| HtUpEnv-21In36(62) | Heating upper frequency-table entry labelled Env -21, In 36(62). The condition thresholds and speed units are unverified. | label inferred |
| HtUpEnv28In50(75) | Heating upper frequency-table entry labelled Env 28, In 50(75). The condition thresholds and speed units are unverified. | label inferred |
| HtUpEnv07In50(75) | Heating upper frequency-table entry labelled Env 7, In 50(75). The condition thresholds and speed units are unverified. | label inferred |
| HtUpEnv00In50(75) | Heating upper frequency-table entry labelled Env 0, In 50(75). The condition thresholds and speed units are unverified. | label inferred |
| HtUpEnv-06In50(75) | Heating upper frequency-table entry labelled Env -6, In 50(75). The condition thresholds and speed units are unverified. | label inferred |
| HtUpEnv-12In50(75) | Heating upper frequency-table entry labelled Env -12, In 50(75). The condition thresholds and speed units are unverified. | label inferred |
| HtUpEnv-21In50(75) | Heating upper frequency-table entry labelled Env -21, In 50(75). The condition thresholds and speed units are unverified. | label inferred |
| HtDnEnv28In20(50) | Heating lower frequency-table entry labelled Env 28, In 20(50). The condition thresholds and speed units are unverified. | label inferred |
| HtDnEnv00In20(50) | Heating lower frequency-table entry labelled Env 0, In 20(50). The condition thresholds and speed units are unverified. | label inferred |
| HtDnEnv-12In20(50) | Heating lower frequency-table entry labelled Env -12, In 20(50). The condition thresholds and speed units are unverified. | label inferred |
| HtDnEnv-21In20(50) | Heating lower frequency-table entry labelled Env -21, In 20(50). The condition thresholds and speed units are unverified. | label inferred |
| HtDnEnv28In36(62) | Heating lower frequency-table entry labelled Env 28, In 36(62). The condition thresholds and speed units are unverified. | label inferred |
| HtDnEnv00In36(62) | Heating lower frequency-table entry labelled Env 0, In 36(62). The condition thresholds and speed units are unverified. | label inferred |
| HtDnEnv-12In36(62) | Heating lower frequency-table entry labelled Env -12, In 36(62). The condition thresholds and speed units are unverified. | label inferred |
| HtDnEnv-21In36(62) | Heating lower frequency-table entry labelled Env -21, In 36(62). The condition thresholds and speed units are unverified. | label inferred |
| HtDnEnv28In50(75) | Heating lower frequency-table entry labelled Env 28, In 50(75). The condition thresholds and speed units are unverified. | label inferred |
| HtDnEnv00In50(75) | Heating lower frequency-table entry labelled Env 0, In 50(75). The condition thresholds and speed units are unverified. | label inferred |
| HtDnEnv-12In50(75) | Heating lower frequency-table entry labelled Env -12, In 50(75). The condition thresholds and speed units are unverified. | label inferred |
| HtDnEnv-21In50(75) | Heating lower frequency-table entry labelled Env -21, In 50(75). The condition thresholds and speed units are unverified. | label inferred |

## Protection & auxiliary

Additional operating limits, auxiliary heaters, circulation and smart-grid settings.

| Parameter | English explanation | Confidence |
|---|---|---|
| Low Amb. 0 | Ambient-temperature operating/protection criterion named Low Amb. 0. Its threshold direction and scale are unverified. | label inferred |
| Air Heat High0 | Ambient-temperature operating/protection criterion named Air Heat High0. Its threshold direction and scale are unverified. | label inferred |
| Low Amb.T0 | Ambient-temperature operating/protection criterion named Low Amb.T0. Its threshold direction and scale are unverified. | label inferred |
| ERR_AC_FLUX_SET | Air-conditioning water-flow protection setting. The flow scale is unverified. | label inferred |
| CLOSE_AT_HEAT_DELAY | Delay for the close/stop action associated with heating. The exact action is unverified. | label inferred |
| LED Logo En | Configures the illuminated logo. The numeric enable codes are unverified. | label inferred |
| Logo On Hour | Sets the start hour for logo lighting. | label inferred |
| Logo On Min. | Sets the start minute for logo lighting. | label inferred |
| Logo Off Hour | Sets the end hour for logo lighting. | label inferred |
| Logo Off Min. | Sets the end minute for logo lighting. | label inferred |
| EAH2 En | Configures the second auxiliary electric-heater stage. The choice codes are unverified. | label inferred |
| EAH_ON_HI_DT | Upper temperature-difference criterion for auxiliary electric heating. | label inferred |
| EAH_ON_LO_DT | Lower temperature-difference criterion for auxiliary electric heating. | label inferred |
| EAH_GEAR | Auxiliary electric-heater stage/level configuration. The choice codes are unverified. | label inferred |
| AHS | Auxiliary heat-source configuration. The numeric choices are unverified. | label inferred |
| EXH Open Dly. | Delay associated with EXH Open Dly.. The timer unit and exact switching condition are unverified. | label inferred |
| EXH Open Diff | Manufacturer setting EXH Open Diff in protection & auxiliary. Its exact function has not yet been verified. | unverified |
| EXH Close Diff | Manufacturer setting EXH Close Diff in protection & auxiliary. Its exact function has not yet been verified. | unverified |
| EXH Open Env. | Manufacturer setting EXH Open Env. in protection & auxiliary. Its exact function has not yet been verified. | unverified |
| TWout2 High | High-temperature criterion for the second outlet-water sensor. | label inferred |
| SYS_PUMPF | System water-pump configuration. The numeric choices are unverified. | label inferred |
| Idu_Odu_Type | Indoor/outdoor unit type assignment. The numeric choices are unverified. | label inferred |
| R290_Climate_Temp_Diff | R290 climate-control temperature difference. Its reference sensor and scale are unverified. | label inferred |
| PUMP_INTER_ON_TIME | On-time for intermittent pump operation. The timer scale is unverified. | label inferred |
| PUMP_INTER_OFF_TIME | Off-time for intermittent pump operation. The timer scale is unverified. | label inferred |
| Dhw Set Max | Upper allowed domestic-hot-water target. The temperature scale is unverified. | label inferred |
| Ac Pump Dly | Air-conditioning circulation-pump delay. The timer scale is unverified. | label inferred |
| Invt Base Freq | Base frequency of the inverter profile. The frequency scale is unverified. | label inferred |
| Invt Max Out.V | Upper inverter output-voltage setting. The voltage scale is unverified. | label inferred |
| Ele.Grid Cur. Max | Upper electrical-supply current setting. The current scale is unverified. | label inferred |
| Mac Open Cur. Min  | Minimum current criterion associated with machine activation. The exact rule is unverified. | label inferred |
| Cur. Limit Diff | Difference used in current limiting. The current scale is unverified. | label inferred |
| Cur. Force Diff | Difference used by forced current adjustment. The exact action is unverified. | label inferred |
| Ext Equipment Cur. | External-equipment current allowance or setting. The scale is unverified. | label inferred |
| PV Mppt Code | Photovoltaic MPPT device/profile code. The numeric code table is unverified. | label inferred |
| PV Mppt Base Address | Base communication address of the photovoltaic MPPT controller. | label inferred |
| PV Mppt Num | Number/assignment of photovoltaic MPPT controllers. The encoding is unverified. | label inferred |
| DI7_Selfdef | Input/output assignment for DI7_Selfdef. The numeric signal or function choices are unverified. | label inferred |
| Cool Run Max Env.T | Upper ambient-temperature operating criterion for cooling. | label inferred |
| Cool Run Max Wat.T | Upper water-temperature operating criterion for cooling. | label inferred |
| PUMPf Set Flow 1 | Water-pump flow target 1. The physical flow unit and raw scale are unverified. | label inferred |
| PUMPf Set Flow 2 | Water-pump flow target 2. The physical flow unit and raw scale are unverified. | label inferred |
| Cpst Begin Temp | Temperature criterion for starting compensation. The reference signal is unverified. | label inferred |
| Temp Cpst Value | Temperature compensation amount. The reference signal and scale are unverified. | label inferred |
| SMART_GRID_LOCK_TIME_MAX | Maximum hold/lock time for smart-grid control. The timer scale is unverified. | label inferred |
| Pv Cpst | Photovoltaic-related compensation setting. The reference signal and scale are unverified. | label inferred |
| DO7_Selfdef | Input/output assignment for DO7_Selfdef. The numeric signal or function choices are unverified. | label inferred |
| DO8_Selfdef | Input/output assignment for DO8_Selfdef. The numeric signal or function choices are unverified. | label inferred |

## Solar & thermostat

Solar-loop, thermostat and additional heating operating-limit settings.

| Parameter | English explanation | Confidence |
|---|---|---|
| TSL_SENSOR | Sensor configuration named TSL. Its physical sensor location and choice codes are unverified. | label inferred |
| SOLAR | Solar-loop control configuration. The numeric choices are unverified. | label inferred |
| PUMPsl_ON_THWt_TEMP | Solar-loop pump activation criterion THWt_TEMP. The sensor reference and temperature scale are unverified. | label inferred |
| PUMPsl_ON_THWt_DT | Solar-loop pump activation criterion THWt_DT. The sensor reference and temperature scale are unverified. | label inferred |
| PUMPsl_ON_WATER_TEMP | Solar-loop pump activation criterion WATER_TEMP. The sensor reference and temperature scale are unverified. | label inferred |
| PUMPsl_ON_WATER_DT | Solar-loop pump activation criterion WATER_DT. The sensor reference and temperature scale are unverified. | label inferred |
| PUMPsl_ANTIFREEZE | Solar-loop pump antifreeze configuration. The numeric choices are unverified. | label inferred |
| Heat Run Max Env.T | Upper ambient-temperature operating criterion for heating. | label inferred |
| Heat Run Low Env.T | Lower ambient-temperature operating criterion for heating. | label inferred |
| Heat Run Max Wat.T | Upper water-temperature operating criterion for heating. | label inferred |
| Exit Cm Limit Diff | Difference used for leaving a compressor-limit state. The reference signal is unverified. | label inferred |
| Thermostat Sw | External thermostat switch configuration. The input polarity and choice codes are unverified. | label inferred |
| Thermostat Mode | External thermostat operating-mode configuration. The numeric choices are unverified. | label inferred |
| Pump Pv Flow Cpst | Photovoltaic-related water-pump flow compensation. The adjustment scale is unverified. | label inferred |
