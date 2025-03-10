#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.datamodel.data import (
    ArchiveSection,
    EntryData,
)
from nomad.datamodel.metainfo.basesections import (
    ProcessStep,
    Entity,
    ElementalComposition,
)
from nomad.datamodel.metainfo.eln import Instrument
from nomad.datamodel.metainfo.workflow import Link
from nomad.metainfo import (
    Datetime,
    MEnum,
    Package,
    Quantity,
    Section,
    SubSection,
)
from nomad.datamodel.metainfo.eln import Chemical
from fabrication_facilities.schema_packages.Items import ItemPropertyDefinition, Item
from fabrication_facilities.schema_packages.utils import parse_chemical_formula

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='FABLIMS Equipment Schema')


class TechniqueSubCategory(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={'properties': {'order': ['name', 'id', 'description']}},
    )
    name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    id = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    description = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `techniqueSubCategory` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class TechniqueMainCategory(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={'properties': {'order': ['name', 'id', 'description']}},
    )
    name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    id = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    description = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )
    technique_sub_categories = SubSection(
        section_def=TechniqueSubCategory,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `techniqueMainCategory` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class TechniqueGeneralCategory(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={'properties': {'order': ['name', 'id', 'description']}},
    )
    name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    id = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    description = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )
    technique_main_categories = SubSection(
        section_def=TechniqueMainCategory,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `finaltechnique` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class TechniqueCategories(EntryData, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={'properties': {'order': ['name', 'description']}},
    )
    description = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )
    name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    technique_general_categories = SubSection(
        section_def=TechniqueGeneralCategory,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `TechniqueCategories` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class EquipmentTechnique(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={
            'properties': {
                'order': [
                    'name',
                    'id',
                    'description',
                    'techniqueMainCategory',
                    'techniqueSubCategory',
                    'genericEquipmentName',
                    'referencingcategorization',
                ]
            }
        },
    )
    name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    id = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    description = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )
    genericEquipmentName = Quantity(
        type=str,
        description='Generic equipment that does the activity, f.e. etcher for etching',
        a_eln={'component': 'StringEditQuantity'},
    )
    techniqueMainCategory = Quantity(
        type=MEnum(
            [
                'synthesis',
                'integration',
                'doping',
                'dicing',
                'thermal processing',
                'lithography',
                'etching',
            ]
        ),
        a_eln={'component': 'EnumEditQuantity'},
    )
    techniqueSubCategory = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    referencingcategorization = Quantity(
        type=TechniqueSubCategory,
        description='Reference to the taxonomy adopted',
        a_eln={'component': 'ReferenceEditQuantity'},
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `EquipmentTechnique` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class ItemPermittedPropertyDefinition(ItemPropertyDefinition, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={
            'hide': ['value'],
            'properties': {
                'order': [
                    'name',
                    'id',
                    'description',
                    'unit',
                    'value_min',
                    'value_max',
                ]
            },
        }
    )

    value_max = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )
    value_min = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `ItemPermittedPropertyDefinition` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class EquipmentHasPermittedItemPropertyData(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={'properties': {'order': ['id', 'ItemShapeType']}},
    )
    id = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    itemShapeType = Quantity(
        type=MEnum(
            [
                'Wafer with flat standard',
                'Wafer with flat JEIDA',
                'Rectangle shape',
                '1/2 wafer',
                '1/4 wafer',
                'Fragment',
                'Square shape',
                'Powder',
                'Wafer with Notch standard',
            ]
        ),
        a_eln={'component': 'EnumEditQuantity'},
    )
    properties = SubSection(
        section_def=ItemPermittedPropertyDefinition,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `EquipmentHasPermittedItemPropertyData` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class EquipmentParameterData(ItemPermittedPropertyDefinition, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={
            'hide': ['value'],
            'properties': {
                'order': [
                    'name',
                    'id',
                    'description',
                    'unit',
                    'value_min',
                    'value_max',
                ]
            },
        }
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `EquipmentParameterData` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class FabricationProductType(EntryData, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={'properties': {'order': ['name', 'description', 'id']}},
    )
    id = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    description = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )


class ListofProductType(EntryData, ArchiveSection):
    m_def = Section()

    name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    description = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )
    available_products = SubSection(
        section_def=FabricationProductType,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `FabricationProcessProductType` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class FabricationProcessStepBase(ProcessStep, EntryData, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={
            'hide': [
                'comment',
                'duration',
                'start_time',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'affiliation',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'recipe_name',
                    'recipe_file',
                    'notes',
                ],
            },
        },
    )
    job_number = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    description = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )
    affiliation = Quantity(
        type=MEnum('NFFA-DI', 'iENTRANCE@ENL'), a_eln={'component': 'EnumEditQuantity'}
    )
    operator = Quantity(type=str, a_eln={'component': 'StringEditQuantity'})
    location = Quantity(type=str, a_eln={'component': 'StringEditQuantity'})
    room = Quantity(type=str, a_eln={'component': 'StringEditQuantity'})
    starting_date = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity'},
    )
    ending_date = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity'},
    )
    step_type = Quantity(type=str, a_eln={'component': 'StringEditQuantity'})
    id_item_processed = Quantity(type=str, a_eln={'component': 'StringEditQuantity'})
    definition_of_process_step = Quantity(
        type=EquipmentTechnique,
        a_eln={'component': 'ReferenceEditQuantity'},
    )
    recipe_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    recipe_file = Quantity(
        type=str,
        a_eln={'component': 'FileEditQuantity'},
    )
    notes = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `FabricationProcessStep` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class Jobdone(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={
            'properties': {
                'order': [
                    'name',
                    'job_number',
                    'notes',
                    'starting_date',
                    'ending_date',
                    'id_item_processed',
                    'referenced_activity',
                ]
            }
        },
    )
    name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    job_number = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    notes = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    starting_date = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity'},
    )
    ending_date = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity'},
    )
    id_items_processed = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
        shape=['*'],
    )
    referenced_activities = Quantity(
        type=FabricationProcessStepBase,
        shape=['*'],
        a_eln={'component': 'ReferenceEditQuantity'},
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `Jobdone` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class Equipment(Instrument, EntryData, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={
            'hide': [
                'lab_id',
                'datetime',
            ],
            'properties': {
                'order': [
                    'name',
                    'inventary_code',
                    'affiliation',
                    'product_model',
                    'institution',
                    'manufacturer_name',
                    'is_bookable',
                    'automatic_loading',
                    'description',
                ],
            },
        }
    )
    inventary_code = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    affiliation = Quantity(
        type=MEnum('NFFA-DI', 'iENTRANCE@ENL'),
        a_eln={'component': 'EnumEditQuantity'},
    )
    institution = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    manufacturer_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    product_model = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    automatic_loading = Quantity(
        type=bool,
        a_eln={'component': 'BoolEditQuantity'},
    )
    is_bookable = Quantity(
        type=bool,
        a_eln={'component': 'BoolEditQuantity'},
    )
    capabilities = SubSection(section_def=EquipmentParameterData, repeats=True)
    equipmentTechniques = SubSection(
        section_def=EquipmentTechnique,
        repeats=True,
    )
    permittedItems = SubSection(
        section_def=EquipmentHasPermittedItemPropertyData,
        repeats=True,
    )
    equipmentLogBook = SubSection(
        section_def=Jobdone,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `Equipment` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class EquipmentReference(Link, ArchiveSection):
    m_def = Section()

    id = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    notes = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )

    section = Quantity(
        type=Instrument,
        a_eln={'component': 'ReferenceEditQuantity'},
    )


class FabricationProcessStep(FabricationProcessStepBase, EntryData):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={
            'hide': [
                'comment',
                'duration',
                'start_time',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'affiliation',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'recipe_name',
                    'recipe_file',
                    'notes',
                ],
            },
        },
    )
    # job_number = Quantity(
    #     type=int,
    #     a_eln={'component': 'NumberEditQuantity'},
    # )
    # name = Quantity(
    #     type=str,
    #     a_eln={'component': 'StringEditQuantity'},
    # )
    # description = Quantity(
    #     type=str,
    #     a_eln={'component': 'RichTextEditQuantity'},
    # )
    # affiliation = Quantity(
    #     type=MEnum('NFFA-DI', 'iENTRANCE@ENL'), a_eln={'component': 'EnumEditQuantity'}
    # )
    # operator = Quantity(type=str, a_eln={'component': 'StringEditQuantity'})
    # location = Quantity(type=str, a_eln={'component': 'StringEditQuantity'})
    # room = Quantity(type=str, a_eln={'component': 'StringEditQuantity'})
    # id_item_processed = Quantity(type=str, a_eln={'component': 'StringEditQuantity'})
    # starting_date = Quantity(
    #     type=Datetime,
    #     a_eln={'component': 'DateTimeEditQuantity'},
    # )
    # ending_date = Quantity(
    #     type=Datetime,
    #     a_eln={'component': 'DateTimeEditQuantity'},
    # )
    # step_type = Quantity(type=str, a_eln={'component': 'StringEditQuantity'})
    # definition_of_process_step = Quantity(
    #     type=EquipmentTechnique,
    #     a_eln={'component': 'ReferenceEditQuantity'},
    # )
    # recipe_name = Quantity(
    #     type=str,
    #     a_eln={'component': 'StringEditQuantity'},
    # )
    # notes = Quantity(
    #     type=str,
    #     a_eln={'component': 'RichTextEditQuantity'},
    # )

    instruments = SubSection(
        section_def=EquipmentReference,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `FabricationProcessStep` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class FabricationProcess(EntryData, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={
            'properties': {
                'order': [
                    'name',
                    'project',
                    'affiliation',
                    'id_proposal',
                    'id_item_processed',
                    'locations',
                    'cost_model',
                    'description',
                    'author',
                    'starting_date',
                    'ending_date',
                    'generic_product_name',
                    'fabricationProductType',
                    'notes',
                ]
            },
            'hide': [
                'end_time',
                'datetime',
                'lab_id',
                'method',
                'location',
            ],
        },
    )
    id_proposal = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    project = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    id_item_processed = Quantity(type=str, a_eln={'component': 'StringEditQuantity'})
    affiliation = Quantity(
        type=MEnum(
            [
                'NFFA-DI',
                'iENTRANCE@ENL',
            ],
        ),
        a_eln={'component': 'EnumEditQuantity'},
    )
    locations = Quantity(
        type=str,
        shape=['*'],
        a_eln={'component': 'StringEditQuantity', 'label': 'institutions'},
    )
    name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    description = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )
    author = Quantity(type=str, a_eln={'component': 'StringEditQuantity'})
    cost_model = Quantity(type=str, a_eln={'component': 'StringEditQuantity'})
    starting_date = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity'},
    )
    ending_date = Quantity(
        type=Datetime,
        a_eln={'component': 'DateTimeEditQuantity'},
    )
    notes = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )
    generic_product_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    fabricationProductType = Quantity(
        type=ListofProductType,
        a_eln={'component': 'ReferenceEditQuantity'},
    )
    steps = Quantity(
        type=FabricationProcessStep,
        shape=['*'],
        a_eln={'component': 'ReferenceEditQuantity'},
    )
    instruments = SubSection(
        section_def=EquipmentReference,
        repeats=True,
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `FabricationProcess` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)

class StartingMaterial(Chemical, FabricationProcessStep, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
                'recipe_name',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'short_name',
                    'chemical_formula',
                    'manufacturer_name',
                    'wafer_quantity',
                    'wafer_resistivity',
                    'wafer_orientation',
                    'wafer_thickness',
                    'wafer_surface_finish',
                    'wafer_diameter',
                    'wafer_doping',
                    'notes',
                ]
            },
        },
    )
    short_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity', 'label':'wafer material'},
    )
    manufacturer_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    wafer_quantity = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    wafer_resistivity = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'ohm*cm'},
        unit='ohm*cm',
    )
    wafer_thickness = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'um'},
        unit='um',
    )
    wafer_orientation = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    wafer_surface_finish = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    wafer_diameter = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'mm'},
        unit='mm',
    )
    wafer_doping = Quantity(
        type=MEnum(
            'p',
            'n',
            'no',
        ),
        a_eln={'component': 'EnumEditQuantity'},
    )

    elemental_composition = SubSection(section_def=ElementalComposition, repeats=True)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
        if self.chemical_formula:
            elements, counts = parse_chemical_formula(self.chemical_formula)
            total = 0
            for token in counts:
                total += int(token)
            if total != 0:
                elemental_fraction = np.array(counts) / total
                elementality = []
                i = 0
                for entry in elements:
                    elemental_try = ElementalComposition()
                    elemental_try.element = entry
                    elemental_try.atomic_fraction = elemental_fraction[i]
                    i += 1
                    elementality.append(elemental_try)
            else:
                print('No elements provided')
            self.elemental_composition = elementality


class SampleParenting(Entity, EntryData, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln={
            'hide': ['lab_id'],
            'properties': {
                'order': [
                    'name',
                    'datetime',
                    'id',
                ],
            },
        }
    )
    id = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    inputs = SubSection(
        section_def=StartingMaterial,
        repeats=True,
    )
    parenting_steps = SubSection(section_def=FabricationProcessStep, repeats=True)
    outputs = SubSection(
        section_def=Item,
        repeats=True,
    )

class SampleParentingLink(Link, ArchiveSection):
    m_def = Section()

    Section = Quantity(
        type=SampleParenting,
        a_eln={'component': 'ReferenceEditQuantity'},
    )

class ObservationMeasurements(FabricationProcessStep, ArchiveSection):
    m_def = Section(
        a_eln={
            'hide': [
                'description',
                'lab_id',
                'datetime',
                'comment',
                'duration',
                'end_time',
                'start_time',
            ],
            'properties': {
                'order': [
                    'job_number',
                    'name',
                    'description',
                    'location',
                    'operator',
                    'room',
                    'id_item_processed',
                    'starting_date',
                    'ending_date',
                    'step_type',
                    'definition_of_process_step',
                    'recipe_name',
                    'activity_type',
                    'short_name',
                    'duration_target',
                    'image_name',
                    'thickness_measurements',
                    'electrical_measurements',
                    'notes',
                ]
            },
        },
    )
    short_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity', 'label':'Equipment used'},
    )
    activity_type = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    duration_target = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'minute'},
        unit='minute',
    )
    image_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    thickness_measurements = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    electrical_measurements = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )

m_package.__init_metainfo__()
