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
# import datetime
from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.datamodel.data import (
    ArchiveSection,
    EntryData,
)
from nomad.datamodel.metainfo.basesections import Entity
from nomad.metainfo import (
    MEnum,
    Package,
    Quantity,
    Section,
    SubSection,
)

from nomad.units import ureg

if TYPE_CHECKING:
    pass

m_package = Package(name='Items plugin')

# class Staging_quantity(MSection):
#    m_def=Section()
#
#    def __init_metainfo__(self, txt):
#        self.measure = txt
#    def select_quantity(self):
#       return Quantity(
#            type=np.float64 if self.measure!=None or self.measure != ""  else str,
#            a_eln={"component": "NumberEditQuantity" if self.measure!=None or self.measure != "" else "StringEditQuantity"},
#            unit=self.measure if self.measure!=None or self.measure != ""  else None
#        )


class ItemPropertyDefinition(EntryData, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    id = Quantity(
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
    unit = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    value = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )
class StringProperties(ItemPropertyDefinition):
    m_def = Section()
    id = Quantity(
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
    value = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )

class NumericProperties(ItemPropertyDefinition):
    m_def = Section()
    id = Quantity(
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
    unit = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    value = Quantity(
        type=np.float64,
        a_eln={'component': 'NumberEditQuantity'},
    )

class DopingProperties(ItemPropertyDefinition):
    m_def = Section()
    id = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    description = Quantity(
        type=str,
        a_eln={'component': 'RichTextEditQuantity'},
    )
    doping_type= Quantity(
        type= MEnum(
            [
                "p",
                "n",
                "no_doping",
            ]
        )
        a_eln={'component': 'EnumEditQuantity'},
    )
    unit = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    value =Quantity(
        type= np.float64,
        a_eln={'component': "NumberEditQuantity"},
    )
#
#    def __init_metainfo__(self, unit_of_measure):
#        super().__init_metainfo__(unit_of_measure)
#        self.value = self.select_quantity()
#    def __init__(self, unit_of_measure=None):
#        super().__init__(**kwargs)  # Inizializza l'oggetto normalmente
#        # Creiamo `value` dinamicamente in base al flag `unit_of_measure`
#        self.m_add_quantity(
#            "value",
#            Quantity(
#                type=np.float64 if unit_of_measure else str,
#                a_eln={"component": "NumberEditQuantity" if unit_of_measure else "StringEditQuantity"},
#                unit=unit_of_measure if unit_of_measure else None,
#            )
#        )

class ItemShapeType(EntryData, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    id = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    description = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )


#    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
#        '''
#        The normalizer for the `ItemShapeType` class.
#
#
#        Args:
#            archive (EntryArchive): The archive containing the section that is being
#            normalized.
#            logger (BoundLogger): A structlog logger.
#        '''
#        super().normalize(archive, logger)


class ListOfItemPropertyDefinition(EntryData, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    description = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    id = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
    )
    list_of_possible_properties = SubSection(
        section_def=ItemPropertyDefinition,
        repeats=True,
    )
    list_of_items_shape_type = SubSection(
        section_def=ItemShapeType,
        repeats=True,
    )


#    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
#        '''
#        The normalizer for the `ListOfItemPropertyDefinition` class.
#
#        Args:
#            archive (EntryArchive): The archive containing the section that is being
#            normalized.
#            logger (BoundLogger): A structlog logger.
#        '''
#        super().normalize(archive, logger)


class StartingMaterial(Entity, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    wafer_material = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    manufacturer_name = Quantity(
        type=str,
        a_eln={'component': 'StringEditQuantity'},
    )
    wafer_doping = Quantity(
        type=bool,
        a_eln={'component': 'BoolEditQuantity'},
    )
    properties = SubSection(
        section_def=ItemPropertyDefinition,
        repeats=True,
    )


#    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
#        '''
#        The normalizer for the `StartingMaterial` class.
#
#        Args:
#            archive (EntryArchive): The archive containing the section that is being
#            normalized.
#            logger (BoundLogger): A structlog logger.
#        '''
#        super().normalize(archive, logger)


class Item(Entity, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    id_wafer_parent = Quantity(
        type=int,
        a_eln={'component': 'NumberEditQuantity'},
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
        section_def=ItemPropertyDefinition,
        repeats=True,
    )


#    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
#        '''
#        The normalizer for the `Item` class.
#
#        Args:
#            archive (EntryArchive): The archive containing the section that is being
#            normalized.
#            logger (BoundLogger): A structlog logger.
#        '''
#        super().normalize(archive, logger)


class Sample_parenting(Entity, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    #    m_def = Section()
    #    date = Quantity(
    #        type=datetime,
    #        a_eln={
    #            "component": "DateTimeEditQuantity"
    #        },
    #    )
    inputs = SubSection(
        section_def=StartingMaterial,
        repeats=True,
    )
    outputs = SubSection(
        section_def=Item,
        repeats=True,
    )


#    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
#        '''
#        The normalizer for the `Sample_parenting` class.
#
#        Args:
#            archive (EntryArchive): The archive containing the section that is being
#            normalized.
#            logger (BoundLogger): A structlog logger.
#        '''
#        super().normalize(archive, logger)


m_package.__init_metainfo__()
