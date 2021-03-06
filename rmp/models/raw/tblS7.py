"""Models for RMP source files with `tblS7...` prefix."""
from django.db import models
from rmp.fields import (
    CopyFromBigIntegerField,
    CopyFromBooleanField,
    CopyFromCharField,
    CopyFromDateTimeField,
    CopyFromDecimalField,
    CopyFromForeignKey,
    CopyFromIntegerField,
    CopyFromTextField,
)
from rmp.models.base import BaseRMPModel


class tblS7PreventionProgramChemicals(BaseRMPModel):
    primarykey = CopyFromIntegerField(
        primary_key=True,
        source_column='PrimaryKey',
        verbose_name='Primary Key',
        help_text='Unique identifier for the Prevention Program 3 chemicals '
                  'record destination table. Generated by RMP*Submit and 3rd-'
                  'party programs.',
    )
    preventionprogram3id = CopyFromForeignKey(
        'Tbls7PreventionProgram3',
        source_column='PreventionProgram3ID',
        verbose_name='Prevention Program 3 ID',
        on_delete=models.PROTECT,
        help_text='A unique number used to identify each prevention program '
                  'within a NAICS code within a process. Generated by '
                  'RMP*Submit and 3rd-party programs.',
    )
    processchemicalid = CopyFromForeignKey(
        'tbls1ProcessChemicals',
        on_delete=models.PROTECT,
        source_column='ProcessChemicalID',
        verbose_name='Process Chemical ID',
        help_text='A number used to identify each chemical within a single RMP'
                  'from Section 1 Chemicals in Covered Process. Generated by '
                  'RMP*Submit and 3rd-party programs.'
    )

    source_file = 'tblS7_Prevention_Program_Chemicals'

    class Meta:
        verbose_name = 'Prevention Program: Program Level 3 Chemical'
        verbose_name_plural = 'Prevention Program: Program Level 3 Chemical'


class tblS7PreventionProgramChemicalsChangeHistory(BaseRMPModel):
    pp3chemchangehistoryid = CopyFromIntegerField(
        primary_key=True,
        source_column='PP3ChemChangeHistoryID',
        verbose_name='PP3 Chemical Change History ID',
    )
    facilitychangehistoryid = CopyFromIntegerField(
        source_column='FacilityChangeHistoryID',
        verbose_name='Facility Change History ID',
    )
    cdxcorrectioncode = CopyFromCharField(
        max_length=1,
        source_column='CDXCorrectionCode',
        verbose_name='CDX Correction Code',
    )
    pp3chemid = CopyFromForeignKey(
        'tblS7PreventionProgramChemicals',
        on_delete=models.PROTECT,
        source_column='PP3ChemID',
        verbose_name='Prevention Program Chemical ID',
    )
    preventionprogram3id = CopyFromForeignKey(
        'tblS7PreventionProgram3',
        on_delete=models.PROTECT,
        source_column='PreventionProgram3ID',
        verbose_name='Prevention Program3 ID',
    )
    processchemicalid = CopyFromForeignKey(
        'tblS1ProcessChemicals',
        on_delete=models.PROTECT,
        source_column='ProcessChemicalID',
        verbose_name='Process Chemical ID',
    )
    process_naics_id = CopyFromForeignKey(
        'tblS1ProcessNAICS',
        on_delete=models.PROTECT,
        source_column='Process_NAICS_ID',
        verbose_name='',
    )
    naicscode = CopyFromForeignKey(
        'tlkpNAICS',
        on_delete=models.PROTECT,
        source_column='NAICSCode',
        verbose_name='NAICS Code',
    )

    source_file = 'tblS7_Prevention_Program_Chemicals_ChangeHistory'


class tblS7PreventionProgram3(BaseRMPModel):
    preventionprogram3id = CopyFromIntegerField(
        primary_key=True,
        source_column='PreventionProgram3ID',
    )
    process_naics_id = CopyFromForeignKey(
        'tblS1ProcessNAICS',
        on_delete=models.PROTECT,
        source_column='Process_NAICS_ID',
    )
    safetyreviewdate = CopyFromDateTimeField(
        source_column='SafetyReviewDate',
        null=True,
    )
    pha_date = CopyFromDateTimeField(
        source_column='PHA_Date',
        null=True,
    )
    pha_whatif = CopyFromBooleanField(
        source_column='PHA_WhatIf',
    )
    pha_checklist = CopyFromBooleanField(
        source_column='PHA_Checklist',
    )
    pha_whatifchecklist = CopyFromBooleanField(
        source_column='PHA_WhatIfChecklist',
    )
    pha_hazop = CopyFromBooleanField(
        source_column='PHA_HAZOP',
    )
    pha_fmea = CopyFromBooleanField(
        source_column='PHA_FMEA',
    )
    pha_fta = CopyFromBooleanField(
        source_column='PHA_FTA',
    )
    pha_othertechnique = CopyFromCharField(
        source_column='PHA_OtherTechnique',
        max_length=200,
        blank=True,
    )
    phacompletiondate = CopyFromDateTimeField(
        source_column='PHACompletionDate',
        null=True,
    )
    mh_toxicrelease = CopyFromBooleanField(
        source_column='MH_ToxicRelease',
    )
    mh_fire = CopyFromBooleanField(
        source_column='MH_Fire',
    )
    mh_explosion = CopyFromBooleanField(
        source_column='MH_Explosion',
    )
    mh_runawayreaction = CopyFromBooleanField(
        source_column='MH_RunawayReaction',
    )
    mh_polymerization = CopyFromBooleanField(
        source_column='MH_Polymerization',
    )
    mh_overpressurization = CopyFromBooleanField(
        source_column='MH_Overpressurization',
    )
    mh_corrosion = CopyFromBooleanField(
        source_column='MH_Corrosion',
    )
    mh_overfilling = CopyFromBooleanField(
        source_column='MH_Overfilling',
    )
    mh_contamination = CopyFromBooleanField(
        source_column='MH_Contamination',
    )
    mh_equipmentfailure = CopyFromBooleanField(
        source_column='MH_EquipmentFailure',
    )
    mh_coolingloss = CopyFromBooleanField(
        source_column='MH_CoolingLoss',
    )
    mh_earthquake = CopyFromBooleanField(
        source_column='MH_Earthquake',
    )
    mh_floods = CopyFromBooleanField(
        source_column='MH_Floods',
    )
    mh_tornado = CopyFromBooleanField(
        source_column='MH_Tornado',
    )
    mh_hurricanes = CopyFromBooleanField(
        source_column='MH_Hurricanes',
    )
    mh_othertype = CopyFromCharField(
        source_column='MH_OtherType',
        max_length=200,
        blank=True,
    )
    pc_vents = CopyFromBooleanField(
        source_column='PC_Vents',
    )
    pc_reliefvalves = CopyFromBooleanField(
        source_column='PC_ReliefValves',
    )
    pc_checkvalves = CopyFromBooleanField(
        source_column='PC_CheckValves',
    )
    pc_scrubbers = CopyFromBooleanField(
        source_column='PC_Scrubbers',
    )
    pc_flares = CopyFromBooleanField(
        source_column='PC_Flares',
    )
    pc_manualshutoffs = CopyFromBooleanField(
        source_column='PC_ManualShutoffs',
    )
    pc_automaticshutoffs = CopyFromBooleanField(
        source_column='PC_AutomaticShutoffs',
    )
    pc_interlocks = CopyFromBooleanField(
        source_column='PC_Interlocks',
    )
    pc_alarms = CopyFromBooleanField(
        source_column='PC_Alarms',
    )
    pc_keyedbypass = CopyFromBooleanField(
        source_column='PC_KeyedBypass',
    )
    pc_emergencyairsupply = CopyFromBooleanField(
        source_column='PC_EmergencyAirSupply',
    )
    pc_emergencypower = CopyFromBooleanField(
        source_column='PC_EmergencyPower',
    )
    pc_backuppump = CopyFromBooleanField(
        source_column='PC_BackupPump',
    )
    pc_groundingequipment = CopyFromBooleanField(
        source_column='PC_GroundingEquipment',
    )
    pc_inhibitoraddition = CopyFromBooleanField(
        source_column='PC_InhibitorAddition',
    )
    pc_rupturedisks = CopyFromBooleanField(
        source_column='PC_RuptureDisks',
    )
    pc_excessflowdevice = CopyFromBooleanField(
        source_column='PC_ExcessFlowDevice',
    )
    pc_quenchsystem = CopyFromBooleanField(
        source_column='PC_QuenchSystem',
    )
    pc_purgesystem = CopyFromBooleanField(
        source_column='PC_PurgeSystem',
    )
    pc_none = CopyFromBooleanField(
        source_column='PC_None',
    )
    pc_othertype = CopyFromCharField(
        source_column='PC_OtherType',
        max_length=200,
        blank=True,
    )
    ms_sprinklersystem = CopyFromBooleanField(
        source_column='MS_SprinklerSystem',
    )
    ms_dikes = CopyFromBooleanField(
        source_column='MS_Dikes',
    )
    ms_firewalls = CopyFromBooleanField(
        source_column='MS_FireWalls',
    )
    ms_blastwalls = CopyFromBooleanField(
        source_column='MS_BlastWalls',
    )
    ms_delugesystem = CopyFromBooleanField(
        source_column='MS_DelugeSystem',
    )
    ms_watercurtain = CopyFromBooleanField(
        source_column='MS_WaterCurtain',
    )
    ms_enclosure = CopyFromBooleanField(
        source_column='MS_Enclosure',
    )
    ms_neutralization = CopyFromBooleanField(
        source_column='MS_Neutralization',
    )
    ms_none = CopyFromBooleanField(
        source_column='MS_None',
    )
    ms_othertype = CopyFromCharField(
        source_column='MS_OtherType',
        max_length=200,
        blank=True,
    )
    md_processareadetectors = CopyFromBooleanField(
        source_column='MD_ProcessAreaDetectors',
    )
    md_perimetermonitors = CopyFromBooleanField(
        source_column='MD_PerimeterMonitors',
    )
    md_none = CopyFromBooleanField(
        source_column='MD_None',
    )
    md_othertype = CopyFromCharField(
        source_column='MD_OtherType',
        max_length=200,
        blank=True,
    )
    ch_chemicalreduction = CopyFromBooleanField(
        source_column='CH_ChemicalReduction',
    )
    ch_chemicalincrease = CopyFromBooleanField(
        source_column='CH_ChemicalIncrease',
    )
    ch_changeprocessparameters = CopyFromBooleanField(
        source_column='CH_ChangeProcessParameters',
    )
    ch_installprocesscontrols = CopyFromBooleanField(
        source_column='CH_InstallProcessControls',
    )
    ch_installprocessdetection = CopyFromBooleanField(
        source_column='CH_InstallProcessDetection',
    )
    ch_installperimetermonitoring = CopyFromBooleanField(
        source_column='CH_InstallPerimeterMonitoring',
    )
    ch_installmitigationsystems = CopyFromBooleanField(
        source_column='CH_InstallMitigationSystems',
    )
    ch_nonerequired = CopyFromBooleanField(
        source_column='CH_NoneRequired',
    )
    ch_none = CopyFromBooleanField(
        source_column='CH_None',
    )
    ch_otherchanges = CopyFromCharField(
        source_column='CH_OtherChanges',
        max_length=200,
        blank=True,
    )
    opproceduresreviewdate = CopyFromDateTimeField(
        source_column='OpProceduresReviewDate',
        null=True,
    )
    trainingreviewdate = CopyFromDateTimeField(
        source_column='TrainingReviewDate',
        null=True,
    )
    tr_classroom = CopyFromBooleanField(
        source_column='TR_Classroom',
    )
    tr_onthejob = CopyFromBooleanField(
        source_column='TR_OnTheJob',
    )
    tr_othertype = CopyFromCharField(
        source_column='TR_OtherType',
        max_length=200,
        blank=True,
    )
    ct_writtentest = CopyFromBooleanField(
        source_column='CT_WrittenTest',
    )
    ct_oraltest  = CopyFromBooleanField(
        source_column='CT_OralTest',
    )
    ct_demonstration = CopyFromBooleanField(
        source_column='CT_Demonstration',
    )
    ct_observation = CopyFromBooleanField(
        source_column='CT_Observation',
    )
    ct_othertype = CopyFromCharField(
        source_column='CT_OtherType',
        max_length=200, blank=True)
    maintenancereviewdate = CopyFromDateTimeField(
        source_column='MaintenanceReviewDate',
        null=True,
    )
    equipmentinspectiondate = CopyFromDateTimeField(
        source_column='EquipmentInspectionDate',
        null=True,
    )
    equipmenttested = CopyFromCharField(
        source_column='EquipmentTested',
        max_length=200,
        blank=True,
    )
    changemgmtdate = CopyFromDateTimeField(
        source_column='ChangeMgmtDate',
        null=True,
    )
    changemgmtreviewdate = CopyFromDateTimeField(
        source_column='ChangeMgmtReviewDate',
        null=True,
    )
    prestartupreviewdate = CopyFromDateTimeField(
        source_column='PreStartupReviewDate',
        null=True,
    )
    complianceauditdate = CopyFromDateTimeField(
        source_column='ComplianceAuditDate',
        null=True,
    )
    auditcompletiondate = CopyFromDateTimeField(
        source_column='AuditCompletionDate',
        null=True,
    )
    incidentinvestigationdate = CopyFromDateTimeField(
        source_column='IncidentInvestigationDate',
        null=True,
    )
    investigationchangedate = CopyFromDateTimeField(
        source_column='InvestigationChangeDate',
        null=True,
    )
    participationplansreviewdate = CopyFromDateTimeField(
        source_column='ParticipationPlansReviewDate',
        null=True,
    )
    hotworkpermitreviewdate = CopyFromDateTimeField(
        source_column='HotWorkPermitReviewDate',
        null=True,
    )
    contractorsafetyreviewdate = CopyFromDateTimeField(
        source_column='ContractorSafetyReviewDate',
        null=True,
    )
    contractorsafetyevaldate = CopyFromDateTimeField(
        source_column='ContractorSafetyEvalDate',
        null=True,
    )
    cbi_flag = CopyFromBooleanField(
        source_column='CBI_Flag',
    )
    description = CopyFromTextField(
        source_column='Description',
        blank=True,
    ) # TODO to rmp_prev3text with prevention programID

    class Meta:
        verbose_name = 'Prevention Program: Program Level 3'
        verbose_name_plural = 'Prevention Programs: Program Level 3'


class tblS7PreventionProgram3Description_ChangeHistory(BaseRMPModel):
    preventionprogram3descchangehistoryid = CopyFromIntegerField(
        primary_key=True,
        source_column='PreventionProgram3DescChangeHistoryID',
    )
    facilitychangehistoryid = CopyFromIntegerField(
        source_column='FacilityChangeHistoryID',
    )
    cdxcorrectioncode = CopyFromCharField(
        max_length=1,
        source_column='CDXCorrectionCode',
    )
    preventionprogram3id = CopyFromForeignKey(
        'tblS7PreventionProgram3',
        on_delete=models.PROTECT,
        source_column='PreventionProgram3ID',
    )
    description = CopyFromTextField(
        source_column='Description',
        blank=True,
    )
    olddescription = CopyFromTextField(
        source_column='OldDescription',
        blank=True,
    )
    seqnum = CopyFromIntegerField(
        source_column='SeqNum',
    )


# class tblS7PreventionProgram3_ChangeHistory(BaseRMPModel):
    # preventionprogram3changehistoryid = (
    #     source_column='PreventionProgram3ChangeHistoryID',
    # )
    # facilitychangehistoryid = (
    #     source_column='FacilityChangeHistoryID',
    # )
    # cdxcorrectioncode = (
    #     source_column='CDXCorrectionCode',
    # )
    # preventionprogram3id = (
    #     source_column='PreventionProgram3ID',
    # )
    # naicscode = (
    #     source_column='NAICSCode',
    # )
    # process_naics_id = (
    #     source_column='Process_NAICS_ID',
    # )
    # processid = (
    #     source_column='ProcessID',
    # )
    # safetyreviewdate = (
    #     source_column='SafetyReviewDate',
    # )
    # oldsafetyreviewdate = (
    #     source_column='OldSafetyReviewDate',
    # )
    # pha_date = (
    #     source_column='PHA_Date',
    # )
    # oldpha_date = (
    #     source_column='OldPHA_Date',
    # )
    # pha_whatif = (
    #     source_column='PHA_WhatIf',
    # )
    # oldpha_whatif = (
    #     source_column='OldPHA_WhatIf',
    # )
    # pha_checklist = (
    #     source_column='PHA_Checklist',
    # )
    # oldpha_checklist = (
    #     source_column='OldPHA_Checklist',
    # )
    # pha_whatifchecklist = (
    #     source_column='PHA_WhatIfChecklist',
    # )
    # oldpha_whatifchecklist = (
    #     source_column='OldPHA_WhatIfChecklist',
    # )
    # pha_hazop = (
    #     source_column='PHA_HAZOP',
    # )
    # oldpha_hazop = (
    #     source_column='OldPHA_HAZOP',
    # )
    # pha_fmea = (
    #     source_column='PHA_FMEA',
    # )
    # oldpha_fmea = (
    #     source_column='OldPHA_FMEA',
    # )
    # pha_fta = (
    #     source_column='PHA_FTA',
    # )
    # oldpha_fta = (
    #     source_column='OldPHA_FTA',
    # )
    # pha_othertechnique = (
    #     source_column='PHA_OtherTechnique',
    # )
    # oldpha_othertechnique = (
    #     source_column='OldPHA_OtherTechnique',
    # )
    # phacompletiondate = (
    #     source_column='PHACompletionDate',
    # )
    # oldphacompletiondate = (
    #     source_column='OldPHACompletionDate',
    # )
    # mh_toxicrelease = (
    #     source_column='MH_ToxicRelease',
    # )
    # oldmh_toxicrelease = (
    #     source_column='OldMH_ToxicRelease',
    # )
    # mh_fire = (
    #     source_column='MH_Fire',
    # )
    # oldmh_fire = (
    #     source_column='OldMH_Fire',
    # )
    # mh_explosion = (
    #     source_column='MH_Explosion',
    # )
    # oldmh_explosion = (
    #     source_column='OldMH_Explosion',
    # )
    # mh_runawayreaction = (
    #     source_column='MH_RunawayReaction',
    # )
    # oldmh_runawayreaction = (
    #     source_column='OldMH_RunawayReaction',
    # )
    # mh_polymerization = (
    #     source_column='MH_Polymerization',
    # )
    # oldmh_polymerization = (
    #     source_column='OldMH_Polymerization',
    # )
    # mh_overpressurization = (
    #     source_column='MH_Overpressurization',
    # )
    # oldmh_overpressurization = (
    #     source_column='OldMH_Overpressurization',
    # )
    # mh_corrosion = (
    #     source_column='MH_Corrosion',
    # )
    # oldmh_corrosion = (
    #     source_column='OldMH_Corrosion',
    # )
    # mh_overfilling = (
    #     source_column='MH_Overfilling',
    # )
    # oldmh_overfilling = (
    #     source_column='OldMH_Overfilling',
    # )
    # mh_contamination = (
    #     source_column='MH_Contamination',
    # )
    # oldmh_contamination = (
    #     source_column='OldMH_Contamination',
    # )
    # mh_equipmentfailure = (
    #     source_column='MH_EquipmentFailure',
    # )
    # oldmh_equipmentfailure = (
    #     source_column='OldMH_EquipmentFailure',
    # )
    # mh_coolingloss = (
    #     source_column='MH_CoolingLoss',
    # )
    # oldmh_coolingloss = (
    #     source_column='OldMH_CoolingLoss',
    # )
    # mh_earthquake = (
    #     source_column='MH_Earthquake',
    # )
    # oldmh_earthquake = (
    #     source_column='OldMH_Earthquake',
    # )
    # mh_floods = (
    #     source_column='MH_Floods',
    # )
    # oldmh_floods = (
    #     source_column='OldMH_Floods',
    # )
    # mh_tornado = (
    #     source_column='MH_Tornado',
    # )
    # oldmh_tornado = (
    #     source_column='OldMH_Tornado',
    # )
    # mh_hurricanes = (
    #     source_column='MH_Hurricanes',
    # )
    # oldmh_hurricanes = (
    #     source_column='OldMH_Hurricanes',
    # )
    # mh_othertype = (
    #     source_column='MH_OtherType',
    # )
    # oldmh_othertype = (
    #     source_column='OldMH_OtherType',
    # )
    # pc_vents = (
    #     source_column='PC_Vents',
    # )
    # oldpc_vents = (
    #     source_column='OldPC_Vents',
    # )
    # pc_reliefvalves = (
    #     source_column='PC_ReliefValves',
    # )
    # oldpc_reliefvalves = (
    #     source_column='OldPC_ReliefValves',
    # )
    # pc_checkvalves = (
    #     source_column='PC_CheckValves',
    # )
    # oldpc_checkvalves = (
    #     source_column='OldPC_CheckValves',
    # )
    # pc_scrubbers = (
    #     source_column='PC_Scrubbers',
    # )
    # oldpc_scrubbers = (
    #     source_column='OldPC_Scrubbers',
    # )
    # pc_flares = (
    #     source_column='PC_Flares',
    # )
    # oldpc_flares = (
    #     source_column='OldPC_Flares',
    # )
    # pc_manualshutoffs = (
    #     source_column='PC_ManualShutoffs',
    # )
    # oldpc_manualshutoffs = (
    #     source_column='OldPC_ManualShutoffs',
    # )
    # pc_automaticshutoffs = (
    #     source_column='PC_AutomaticShutoffs',
    # )
    # oldpc_automaticshutoffs = (
    #     source_column='OldPC_AutomaticShutoffs',
    # )
    # pc_interlocks = (
    #     source_column='PC_Interlocks',
    # )
    # oldpc_interlocks = (
    #     source_column='OldPC_Interlocks',
    # )
    # pc_alarms = (
    #     source_column='PC_Alarms',
    # )
    # oldpc_alarms = (
    #     source_column='OldPC_Alarms',
    # )
    # pc_keyedbypass = (
    #     source_column='PC_KeyedBypass',
    # )
    # oldpc_keyedbypass = (
    #     source_column='OldPC_KeyedBypass',
    # )
    # pc_emergencyairsupply = (
    #     source_column='PC_EmergencyAirSupply',
    # )
    # oldpc_emergencyairsupply = (
    #     source_column='OldPC_EmergencyAirSupply',
    # )
    # pc_emergencypower = (
    #     source_column='PC_EmergencyPower',
    # )
    # oldpc_emergencypower = (
    #     source_column='OldPC_EmergencyPower',
    # )
    # pc_backuppump = (
    #     source_column='PC_BackupPump',
    # )
    # oldpc_backuppump = (
    #     source_column='OldPC_BackupPump',
    # )
    # pc_groundingequipment = (
    #     source_column='PC_GroundingEquipment',
    # )
    # oldpc_groundingequipment = (
    #     source_column='OldPC_GroundingEquipment',
    # )
    # pc_inhibitoraddition = (
    #     source_column='PC_InhibitorAddition',
    # )
    # oldpc_inhibitoraddition = (
    #     source_column='OldPC_InhibitorAddition',
    # )
    # pc_rupturedisks = (
    #     source_column='PC_RuptureDisks',
    # )
    # oldpc_rupturedisks = (
    #     source_column='OldPC_RuptureDisks',
    # )
    # pc_excessflowdevice = (
    #     source_column='PC_ExcessFlowDevice',
    # )
    # oldpc_excessflowdevice = (
    #     source_column='OldPC_ExcessFlowDevice',
    # )
    # pc_quenchsystem = (
    #     source_column='PC_QuenchSystem',
    # )
    # oldpc_quenchsystem = (
    #     source_column='OldPC_QuenchSystem',
    # )
    # pc_purgesystem = (
    #     source_column='PC_PurgeSystem',
    # )
    # oldpc_purgesystem = (
    #     source_column='OldPC_PurgeSystem',
    # )
    # pc_none = (
    #     source_column='PC_None',
    # )
    # oldpc_none = (
    #     source_column='OldPC_None',
    # )
    # pc_othertype = (
    #     source_column='PC_OtherType',
    # )
    # oldpc_othertype = (
    #     source_column='OldPC_OtherType',
    # )
    # ms_sprinklersystem = (
    #     source_column='MS_SprinklerSystem',
    # )
    # oldms_sprinklersystem = (
    #     source_column='OldMS_SprinklerSystem',
    # )
    # ms_dikes = (
    #     source_column='MS_Dikes',
    # )
    # oldms_dikes = (
    #     source_column='OldMS_Dikes',
    # )
    # ms_firewalls = (
    #     source_column='MS_FireWalls',
    # )
    # oldms_firewalls = (
    #     source_column='OldMS_FireWalls',
    # )
    # ms_blastwalls = (
    #     source_column='MS_BlastWalls',
    # )
    # oldms_blastwalls = (
    #     source_column='OldMS_BlastWalls',
    # )
    # ms_delugesystem = (
    #     source_column='MS_DelugeSystem',
    # )
    # oldms_delugesystem = (
    #     source_column='OldMS_DelugeSystem',
    # )
    # ms_watercurtain = (
    #     source_column='MS_WaterCurtain',
    # )
    # oldms_watercurtain = (
    #     source_column='OldMS_WaterCurtain',
    # )
    # ms_enclosure = (
    #     source_column='MS_Enclosure',
    # )
    # oldms_enclosure = (
    #     source_column='OldMS_Enclosure',
    # )
    # ms_neutralization = (
    #     source_column='MS_Neutralization',
    # )
    # oldms_neutralization = (
    #     source_column='OldMS_Neutralization',
    # )
    # ms_none = (
    #     source_column='MS_None',
    # )
    # oldms_none = (
    #     source_column='OldMS_None',
    # )
    # ms_othertype = (
    #     source_column='MS_OtherType',
    # )
    # oldms_othertype = (
    #     source_column='OldMS_OtherType',
    # )
    # md_processareadetectors = (
    #     source_column='MD_ProcessAreaDetectors',
    # )
    # oldmd_processareadetectors = (
    #     source_column='OldMD_ProcessAreaDetectors',
    # )
    # md_perimetermonitors = (
    #     source_column='MD_PerimeterMonitors',
    # )
    # oldmd_perimetermonitors = (
    #     source_column='OldMD_PerimeterMonitors',
    # )
    # md_none = (
    #     source_column='MD_None',
    # )
    # oldmd_none = (
    #     source_column='OldMD_None',
    # )
    # md_othertype = (
    #     source_column='MD_OtherType',
    # )
    # oldmd_othertype = (
    #     source_column='OldMD_OtherType',
    # )
    # ch_chemicalreduction = (
    #     source_column='CH_ChemicalReduction',
    # )
    # oldch_chemicalreduction = (
    #     source_column='OldCH_ChemicalReduction',
    # )
    # ch_chemicalincrease = (
    #     source_column='CH_ChemicalIncrease',
    # )
    # oldch_chemicalincrease = (
    #     source_column='OldCH_ChemicalIncrease',
    # )
    # ch_changeprocessparameters = (
    #     source_column='CH_ChangeProcessParameters',
    # )
    # oldch_changeprocessparameters = (
    #     source_column='OldCH_ChangeProcessParameters',
    # )
    # ch_installprocesscontrols = (
    #     source_column='CH_InstallProcessControls',
    # )
    # oldch_installprocesscontrols = (
    #     source_column='OldCH_InstallProcessControls',
    # )
    # ch_installprocessdetection = (
    #     source_column='CH_InstallProcessDetection',
    # )
    # oldch_installprocessdetection = (
    #     source_column='OldCH_InstallProcessDetection',
    # )
    # ch_installperimetermonitoring = (
    #     source_column='CH_InstallPerimeterMonitoring',
    # )
    # oldch_installperimetermonitoring = (
    #     source_column='OldCH_InstallPerimeterMonitoring',
    # )
    # ch_installmitigationsystems = (
    #     source_column='CH_InstallMitigationSystems',
    # )
    # oldch_installmitigationsystems = (
    #     source_column='OldCH_InstallMitigationSystems',
    # )
    # ch_nonerequired = (
    #     source_column='CH_NoneRequired',
    # )
    # oldch_nonerequired = (
    #     source_column='OldCH_NoneRequired',
    # )
    # ch_none = (
    #     source_column='CH_None',
    # )
    # oldch_none = (
    #     source_column='OldCH_None',
    # )
    # ch_otherchanges = (
    #     source_column='CH_OtherChanges',
    # )
    # oldch_otherchanges = (
    #     source_column='OldCH_OtherChanges',
    # )
    # opproceduresreviewdate = (
    #     source_column='OpProceduresReviewDate',
    # )
    # oldopproceduresreviewdate = (
    #     source_column='OldOpProceduresReviewDate',
    # )
    # trainingreviewdate = (
    #     source_column='TrainingReviewDate',
    # )
    # oldtrainingreviewdate = (
    #     source_column='OldTrainingReviewDate',
    # )
    # tr_classroom = (
    #     source_column='TR_Classroom',
    # )
    # oldtr_classroom = (
    #     source_column='OldTR_Classroom',
    # )
    # tr_onthejob = (
    #     source_column='TR_OnTheJob',
    # )
    # oldtr_onthejob = (
    #     source_column='OldTR_OnTheJob',
    # )
    # tr_othertype = (
    #     source_column='TR_OtherType',
    # )
    # oldtr_othertype = (
    #     source_column='OldTR_OtherType',
    # )
    # ct_writtentest = (
    #     source_column='CT_WrittenTest',
    # )
    # oldct_writtentest = (
    #     source_column='OldCT_WrittenTest',
    # )
    # ct_oraltest = (
    #     source_column='CT_OralTest',
    # )
    # oldct_oraltest = (
    #     source_column='OldCT_OralTest',
    # )
    # ct_demonstration = (
    #     source_column='CT_Demonstration',
    # )
    # oldct_demonstration = (
    #     source_column='OldCT_Demonstration',
    # )
    # ct_observation = (
    #     source_column='CT_Observation',
    # )
    # oldct_observation = (
    #     source_column='OldCT_Observation',
    # )
    # ct_othertype = (
    #     source_column='CT_OtherType',
    # )
    # oldct_othertype = (
    #     source_column='OldCT_OtherType',
    # )
    # maintenancereviewdate = (
    #     source_column='MaintenanceReviewDate',
    # )
    # oldmaintenancereviewdate = (
    #     source_column='OldMaintenanceReviewDate',
    # )
    # equipmentinspectiondate = (
    #     source_column='EquipmentInspectionDate',
    # )
    # oldequipmentinspectiondate = (
    #     source_column='OldEquipmentInspectionDate',
    # )
    # equipmenttested = (
    #     source_column='EquipmentTested',
    # )
    # oldequipmenttested = (
    #     source_column='OldEquipmentTested',
    # )
    # changemgmtdate = (
    #     source_column='ChangeMgmtDate',
    # )
    # oldchangemgmtdate = (
    #     source_column='OldChangeMgmtDate',
    # )
    # changemgmtreviewdate = (
    #     source_column='ChangeMgmtReviewDate',
    # )
    # oldchangemgmtreviewdate = (
    #     source_column='OldChangeMgmtReviewDate',
    # )
    # prestartupreviewdate = (
    #     source_column='PreStartupReviewDate',
    # )
    # oldprestartupreviewdate = (
    #     source_column='OldPreStartupReviewDate',
    # )
    # complianceauditdate = (
    #     source_column='ComplianceAuditDate',
    # )
    # oldcomplianceauditdate = (
    #     source_column='OldComplianceAuditDate',
    # )
    # auditcompletiondate = (
    #     source_column='AuditCompletionDate',
    # )
    # oldauditcompletiondate = (
    #     source_column='OldAuditCompletionDate',
    # )
    # incidentinvestigationdate = (
    #     source_column='IncidentInvestigationDate',
    # )
    # oldincidentinvestigationdate = (
    #     source_column='OldIncidentInvestigationDate',
    # )
    # investigationchangedate = (
    #     source_column='InvestigationChangeDate',
    # )
    # oldinvestigationchangedate = (
    #     source_column='OldInvestigationChangeDate',
    # )
    # participationplansreviewdate = (
    #     source_column='ParticipationPlansReviewDate',
    # )
    # oldparticipationplansreviewdate = (
    #     source_column='OldParticipationPlansReviewDate',
    # )
    # hotworkpermitreviewdate = (
    #     source_column='HotWorkPermitReviewDate',
    # )
    # oldhotworkpermitreviewdate = (
    #     source_column='OldHotWorkPermitReviewDate',
    # )
    # contractorsafetyreviewdate = (
    #     source_column='ContractorSafetyReviewDate',
    # )
    # oldcontractorsafetyreviewdate = (
    #     source_column='OldContractorSafetyReviewDate',
    # )
    # contractorsafetyevaldate = (
    #     source_column='ContractorSafetyEvalDate',
    # )
    # oldcontractorsafetyevaldate = (
    #     source_column='OldContractorSafetyEvalDate',
    # )

    # class Meta:
    #     verbose_name=''
    #     verbose_name_plural=''
