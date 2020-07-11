from rest_framework.serializers import ModelSerializer

from emp.models import (
    News,
    Offer,
    Requests,
    Employee,
    Existence,
    Owner,
    Compound,
    Block,
    Tower,
    Flat,
    Store,
    ownershipStore,
    Family,
)

# News Section


class NewsCreateSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = [
            'admin',
            'Title',
            'Desc',
            'created_date',
            'Avatar'
        ]
        # read_only_fields = ["id"]


class NewsUpdateSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = [
            'admin',
            'Title',
            'Desc',
            'created_date',
            'Avatar'
        ]
        # read_only_fields = ["id"]


class NewsListSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = [
            'id',
            'admin',
            'Title',
            'Desc',
            'created_date',
            'Avatar'
        ]


class NewsDetailSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = [
            'id',
            'admin',
            'Title',
            'Desc',
            'created_date',
            'Avatar'
        ]
        # read_only_fields = ["id"]

# Offers Section


class OffersCreateSerializer(ModelSerializer):
    class Meta:
        model = Offer
        fields = [
            'admin',
            'Title',
            'Desc',
            'created_date',
            'Installement',
            'Cost',
            'minPayment',
            'Duration',
            'Avatar',
        ]


class OffersUpdateSerializer(ModelSerializer):
    class Meta:
        model = Offer
        fields = [
            'admin',
            'Title',
            'Desc',
            'created_date',
            'Installement',
            'Cost',
            'minPayment',
            'Duration',
            'Avatar',
        ]


class OffersListSerializer(ModelSerializer):
    class Meta:
        model = Offer
        fields = [
            'id',
            'admin',
            'Title',
            'Desc',
            'created_date',
            'Installement',
            'Cost',
            'minPayment',
            'Duration',
            'Avatar',
        ]


class OfferDetailSerializer(ModelSerializer):
    class Meta:
        model = Offer
        fields = [
            'id',
            'admin',
            'Title',
            'Desc',
            'created_date',
            'Installement',
            'Cost',
            'minPayment',
            'Duration',
            'Avatar',
        ]
        # read_only_fields = ["id"]

# Request Section


class RequestCreateSerializer(ModelSerializer):
    class Meta:
        model = Requests
        fields = [
            'Title',
            'Desc',
            'Type',
            'created_date',
            'Email',
            'Mobile',
        ]
        # read_only_fields = ["id"]


class RequestListSerializer(ModelSerializer):
    class Meta:
        model = Requests
        fields = [
            'id',
            'Title',
            'Desc',
            'Type',
            'created_date',
            'Email',
            'Mobile',
        ]
        # read_only_fields = ["id"]


class RequestDetailSerializer(ModelSerializer):
    class Meta:
        model = Requests
        fields = [
            'id',
            'Title',
            'Desc',
            'Type',
            'created_date',
            'Email',
            'Mobile',
        ]
        # read_only_fields = ["id"]

# Employee Section


class EmployeeCreateSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'NID',
            'Name',
            'Address',
            'Proof',
            'Birthdate',
            'jobDesc',
            'Mobile',
            'DSL',
            'Avatar',
        ]
        # read_only_fields = ["id"]


class EmployeeUpdateSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'id',
            'NID',
            'Name',
            'Address',
            'Proof',
            'Birthdate',
            'jobDesc',
            'Mobile',
            'DSL',
            'Avatar',
        ]
        # read_only_fields = ["id"]


class EmployeeListSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'id',
            'NID',
            'Name',
            'Address',
            'jobDesc',
        ]
        # read_only_fields = ["id"]


class EmployeeDetailSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'id',
            'NID',
            'Name',
            'Address',
            'Proof',
            'Birthdate',
            'jobDesc',
            'Mobile',
            'DSL',
            'Avatar',
        ]
        # read_only_fields = ["id"]

# Existance Section


class ExistenceSerializer(ModelSerializer):
    class Meta:
        model = Existence
        fields = [
            'Name',
            'Type',
            'Timing',
            'NID',
        ]

# Owner Section


class OwnerCreateSerializer(ModelSerializer):
    class Meta:
        model = Owner
        fields = [
            'NID',
            'Name',
            'Proof',
            'Birthdate',
            'Mobile',
            'DSL',
            'Avatar',
            'Type',
            'Notes',
        ]


class OwnerUpdateSerializer(ModelSerializer):
    class Meta:
        model = Owner
        fields = [
            'NID',
            'Name',
            'Proof',
            'Birthdate',
            'Mobile',
            'DSL',
            'Avatar',
            'Type',
            'Notes',
        ]


class OwnerListSerializer(ModelSerializer):
    class Meta:
        model = Owner
        fields = [
            'id',
            'NID',
            'Name',
            'Proof',
            'Birthdate',
            'Mobile',
            'DSL',
            'Avatar',
            'Type',
            'Notes',
        ]


class OwnerDetailSerializer(ModelSerializer):
    class Meta:
        model = Owner
        fields = [
            'id',
            'NID',
            'Name',
            'Proof',
            'Birthdate',
            'Mobile',
            'DSL',
            'Avatar',
            'Type',
            'Notes',
        ]


class OwnerSerializer(ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'


class FamilySerializer(ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'

# Compound Section


class CompoundCreateSerializer(ModelSerializer):
    class Meta:
        model = Compound
        fields = [
            'Name',
            'Number',
            'Address',
            'Latitude',
            'Longitude',
            'Area',
            'Desc',
        ]


class CompoundUpdateSerializer(ModelSerializer):
    class Meta:
        model = Compound
        fields = [
            'Name',
            'Number',
            'Address',
            'Latitude',
            'Longitude',
            'Area',
            'Desc',
        ]


class CompoundListSerializer(ModelSerializer):
    class Meta:
        model = Compound
        fields = [
            'id',
            'Name',
            'Number',
            'Address',
            'Desc',
            'Latitude',
            'Longitude',
        ]


class CompoundDetailSerializer(ModelSerializer):
    class Meta:
        model = Compound
        fields = [
            'id',
            'Name',
            'Number',
            'Address',
            'Latitude',
            'Longitude',
            'Area',
            'Desc',
        ]

# Block Section


class BlockCreateSerializer(ModelSerializer):
    class Meta:
        model = Block
        fields = [
            'Number',
            'compound',
            'Area',
            'Desc',
            'towersNumber',
            'Number',
        ]


class BlockUpdateSerializer(ModelSerializer):
    class Meta:
        model = Block
        fields = [
            'Number',
            'compound',
            'Area',
            'Desc',
            'towersNumber',
            'Number',
        ]


class BlockListSerializer(ModelSerializer):
    class Meta:
        model = Block
        fields = [
            'id',
            'Number',
            'compound',
            'Area',
            'towersNumber',
            'Number',
        ]


class BlockDetailSerializer(ModelSerializer):
    class Meta:
        model = Block
        fields = [
            'id',
            'Number',
            'compound',
            'Area',
            'Desc',
            'towersNumber',
            'Number',
        ]

# Tower Section


class TowerCreateSerializer(ModelSerializer):

    class Meta:
        model = Tower
        fields = [
            'block',
            'Name',
            'Number',
            'Area',
            'flatsNumber',
            'Cost',
            'Notes',
            'floorsNumber',
            'storesNumber',
            'Type',
            'Number',
            'owner',
        ]


class TowerUpdateSerializer(ModelSerializer):
    class Meta:
        model = Tower
        fields = [
            'block',
            'Name',
            'Number',
            'Area',
            'flatsNumber',
            'Cost',
            'Notes',
            'floorsNumber',
            'storesNumber',
            'Type',
            'Number',
            'owner',
        ]


class TowerListSerializer(ModelSerializer):
    class Meta:
        model = Tower
        fields = [
            'id',
            'Number',
            'block',
            'Name',
            'Area',
            'flatsNumber',
            'Cost',
            'Notes',
            'floorsNumber',
            'storesNumber',
            'Type',
            'Number',
            'owner',
        ]


class TowerDetailSerializer(ModelSerializer):
    class Meta:
        model = Tower
        fields = [
            'id',
            'Number',
            'block',
            'Name',
            'Area',
            'flatsNumber',
            'Cost',
            'Notes',
            'floorsNumber',
            'storesNumber',
            'Type',
            'Number',
            'owner',
        ]

# Flat Section


class FlatCreateSerializer(ModelSerializer):
    class Meta:
        model = Flat
        fields = [
            'owner',
            'tower',
            'floorNumber',
            'Area',
            'Inhabited',
            'Number',
        ]


class FlatUpdateSerializer(ModelSerializer):
    class Meta:
        model = Flat
        fields = [
            'owner',
            'tower',
            'Number',
            'floorNumber',
            'Area',
            'Inhabited',
        ]


class FlatListSerializer(ModelSerializer):
    class Meta:
        model = Flat
        fields = [
            'id',
            'owner',
            'tower',
            'Number',
            'Inhabited',
            'floorNumber',
            'Area',
            'owner'
        ]


class FlatDetailSerializer(ModelSerializer):
    class Meta:
        model = Flat
        fields = [
            'id',
            'owner',
            'tower',
            'Number',
            'floorNumber',
            'Area',
            'Inhabited',
        ]

# Store Section


class StoreCreateSerializer(ModelSerializer):
    class Meta:
        model = Store
        fields = [
            'tower',
            'Number',
            'floorNumber',
            'Name',
            'Desc',
            'Type',
        ]


class StoreUpdateSerializer(ModelSerializer):
    class Meta:
        model = Store
        fields = [
            'tower',
            'Number',
            'floorNumber',
            'Name',
            'Desc',
            'Type',
        ]


class StoreListSerializer(ModelSerializer):
    class Meta:
        model = Store
        fields = [
            'id',
            'tower',
            'Number',
            'floorNumber',
            'Name',
            'Type',
            'Desc'
        ]


class StoreDetailSerializer(ModelSerializer):
    class Meta:
        model = Store
        fields = [
            'id',
            'tower',
            'Number',
            'floorNumber',
            'Name',
            'Desc',
            'Type',
        ]

# Ownership Store Section


class ownershipStoreCreateandUpdateSerializer(ModelSerializer):
    class Meta:
        model = ownershipStore
        fields = [
            'owner',
            'store',
        ]


class ownershipStoreListSerializer(ModelSerializer):
    class Meta:
        model = ownershipStore
        fields = [
            'id',
            'owner',
            'store',
        ]

# Family Section


class FamilyCreateSerializer(ModelSerializer):
    class Meta:
        model = Family
        fields = [
            'owner',
            'Name',
            'Birthdate',
            'Relationship',
            'Proof',
        ]


class FamilyUpdateSerializer(ModelSerializer):
    class Meta:
        model = Family
        fields = [
            'owner',
            'Name',
            'Birthdate',
            'Relationship',
            'Proof',
        ]


class FamilyListSerializer(ModelSerializer):
    class Meta:
        model = Family
        fields = [
            'id',
            'owner',
            'Name',
            'Birthdate',
            'Relationship',
            'Proof'
        ]


class FamilyDetailSerializer(ModelSerializer):
    class Meta:
        model = Family
        fields = [
            'id',
            'owner',
            'Name',
            'Birthdate',
            'Relationship',
            'Proof',
        ]
