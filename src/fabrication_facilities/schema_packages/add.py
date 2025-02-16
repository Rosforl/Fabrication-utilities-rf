from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.datamodel.data import (
    ArchiveSection,
)
from nomad.datamodel.metainfo.eln import Chemical
from nomad.metainfo import (
    Package,
    Quantity,
    Section,
    SubSection,
)

from fabrication_facilities.schema_packages.fabrication_steps import (
    FabricationProcessStep,
)
from fabrication_facilities.schema_packages.utils import Massflow_controller

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='Add processes schema')


class ICP_CVD(FabricationProcessStep, Chemical, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
            ],
            'properties': {
                'order': [
                    'name',
                    'job_progressive_id',
                    'start_time',
                    'ending_date',
                    'fabricationProcessStepDefinition',
                    'fabricationEquipmentRecipeName',
                    'thickness_from_recipe',
                    'duration_from_recipe',
                    'deposition_rate_from_recipe',
                    'short_name',
                    'chemical_formula',
                    'thickness_target',
                    'chamber_pressure',
                    'chuck_temperature',
                    'power',
                    'bias',
                    'thickness_obtained',
                    'duration_effective',
                    'deposition_rate_obtained',
                    'notes',
                ]
            },
        },
    )
    thickness_from_recipe = Quantity(
        type=np.float64,
        description='Total material deposited under conditions described in the recipe',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'um'},
        unit='um',
    )
    duration_from_recipe = Quantity(
        type=np.float64,
        description='Time prescribed by the recipe',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )
    deposition_rate_from_recipe = Quantity(
        type=np.float64,
        description='Deposition rate provided in the recipe',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'um/minute'},
        unit='um/minute',
    )
    short_name = Quantity(
        type=str,
        description='Material to be deposited',
        a_eln={'component': 'StringEditQuantity', 'label': 'target material'},
    )
    chemical_formula = Quantity(
        type=str,
        description='Inserted only if known',
        a_eln={'component': 'StringEditQuantity'},
    )
    thickness_target = Quantity(
        type=np.float64,
        description='Amount of material to be deposited',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'um'},
        unit='um',
    )
    chamber_pressure = Quantity(
        type=np.float64,
        description='Pressure in the chamber',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mbar'},
        unit='mbar',
    )
    chuck_temperature = Quantity(
        type=np.float64,
        description='Temperature of the chuck',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
        unit='celsius',
    )
    power = Quantity(
        type=np.float64,
        description='Power erogated',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'watt'},
        unit='watt',
    )
    bias = Quantity(
        type=np.float64,
        description='Bias voltage in the chamber',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'volt'},
        unit='volt',
    )
    thickness_obtained = Quantity(
        type=np.float64,
        description='Amount of material deposited efefctively in the process',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'um'},
        unit='um',
    )
    duration_effective = Quantity(
        type=np.float64,
        description='Real time employed',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )
    deposition_rate_obtained = Quantity(
        type=np.float64,
        description='Deposition rate as output',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'um/minute'},
        unit='um/minute',
    )
    fluximeters = SubSection(
        section_def=Massflow_controller,
        repeats=True,
    )
    #    output_measures= SubSection(
    #        section_def= Link,
    #        repeats= False,
    #    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `Step` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class Spin_Coating(FabricationProcessStep, Chemical, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
            ],
            'properties': {
                'order': [
                    'name',
                    'job_progressive_id',
                    'start_time',
                    'ending_date',
                    'fabricationProcessStepDefinition',
                    'fabricationEquipmentRecipeName',
                    'thickness_from_recipe',
                    'duration_from_recipe',
                    'short_name',
                    'chemical_formula',
                    'thickness_target',
                    'hdms_required',
                    'exposure_required',
                    'exposure_duration',
                    'peb_required',
                    'peb_duration',
                    'peb_temperature',
                    'dewetting_duration',
                    'dewetting_temperature',
                    'spin_dispensed_volume',
                    'spin_frequency',
                    'spin_angular_acceleration',
                    'spin_duration',
                    'baking_duration',
                    'baking_temperature',
                    'thickness_obtained',
                    'notes',
                ]
            },
        },
    )
    thickness_from_recipe = Quantity(
        type=np.float64,
        description='Amount of material deposited under standard conditions described in the recipe',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'um'},
        unit='um',
    )
    duration_from_recipe = Quantity(
        type=np.float64,
        description='Time prescribed by the recipe',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )
    short_name = Quantity(
        type=str,
        description='Material to be deposited',
        a_eln={'component': 'StringEditQuantity', 'label': 'photoresist name'},
    )
    chemical_formula = Quantity(
        type=str,
        description='Inserted only if known',
        a_eln={
            'component': 'StringEditQuantity',
        },
    )
    thickness_target = Quantity(
        type=np.float64,
        description='Amount of material to be deposited',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'um'},
        unit='um',
    )
    hdms_required = Quantity(
        type=bool,
        description='The recipe use the hdms?',
        a_eln={
            'component': 'BoolEditQuantity',
        },
    )
    exposure_required = Quantity(
        type=bool,
        description='The recipe use exposure?',
        a_eln={
            'component': 'BoolEditQuantity',
        },
    )
    exposure_duration = None
    # Quantity(type=any,description='The duration of the exposure',a_eln={'component': None,'defaultDisplayUnit': None,},unit=None,)
    peb_required = Quantity(
        type=bool,
        description='The recipe use exposure?',
        a_eln={
            'component': 'BoolEditQuantity',
        },
    )
    peb_duration = None
    # Quantity(type=,description='The duration of the exposure',a_eln={'component': None,'defaultDisplayUnit': None,},unit=None,)
    peb_temperature = None

    # Quantity(type=any,description='The duration of the exposure',a_eln={'component': None,'defaultDisplayUnit': None,},unit=None,)
    dewetting_duration = Quantity(
        type=np.float64,
        description='The duration of the dewetting',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'minute',
        },
        unit='minute',
    )
    dewetting_temperature = Quantity(
        type=np.float64,
        description='The temperaure of the dewetting',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )
    spin_dispensed_volume = Quantity(
        type=np.float64,
        description='Solution dispensed',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'milliliter',
        },
        unit='milliliter',
    )
    spin_frequency = Quantity(
        type=np.float64,
        description='Velocity of the spinner',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDispalyUnit': 'revolutions_per_minute',
        },
        unit='revolutions_per_minute',
    )
    spin_angular_acceleration = Quantity(
        type=np.float64,
        description='Acceleration of the spinner',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDispalyUnit': 'revolutions_per_minute/second',
        },
        unit='rpm/second',
    )
    spin_duration = Quantity(
        type=np.float64,
        description='Acceleration of the spinner',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDispalyUnit': 'second',
        },
        unit='second',
    )
    baking_duration = Quantity(
        type=np.float64,
        description='The duration of the dewetting',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'minute',
        },
        unit='minute',
    )
    baking_temperature = Quantity(
        type=np.float64,
        description='The temperaure of the dewetting',
        a_eln={
            'component': 'NumberEditQuantity',
            'defaultDisplayUnit': 'celsius',
        },
        unit='celsius',
    )
    thickness_obtained = Quantity(
        type=np.float64,
        description='Amount of material deposited under standard conditions described in the recipe',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'um'},
        unit='um',
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
        if self.exposure_required:
            self.exposure_duration = Quantity(
                type=np.float64,
                description='The duration of the exposure',
                a_eln={
                    'component': 'NumberEditQuantity',
                    'defaultDisplayUnit': 'minute',
                },
                unit='minute',
            )


m_package.__init_metainfo__()
