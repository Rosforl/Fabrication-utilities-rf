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
from nomad.datamodel.metainfo.eln import Instrument
from nomad.datamodel.metainfo.workflow import Link
from nomad.metainfo import (
    MEnum,
    Package,
    Quantity,
    Section,
    SubSection,
)

from fabrication_facilities.schema_packages.Items import ItemPropertyDefinition
from fabrication_facilities.schema_packages.utils import Jobdone

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
                    'manufacturer',
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
    manufacturer = Quantity(
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
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    notes = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )

    section = Quantity(
        type=Instrument,
        a_eln={'component': 'ReferenceEditQuantity'},
    )


m_package.__init_metainfo__()
