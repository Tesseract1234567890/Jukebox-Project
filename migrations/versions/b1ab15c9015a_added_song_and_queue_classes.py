"""Added song and queue classes

Revision ID: b1ab15c9015a
Revises: 
Create Date: 2024-02-23 08:28:35.033301

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b1ab15c9015a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('song',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('track_name', sa.String(length=255), nullable=False),
    sa.Column('artist_name', sa.String(length=255), nullable=False),
    sa.Column('track_length', sa.String(length=255), nullable=False),
    sa.Column('cover_url', sa.String(length=255), nullable=False),
    sa.Column('track_id', sa.String(length=255), nullable=False),
    sa.Column('uri', sa.String(length=255), nullable=False),
    sa.Column('bpm', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('queue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('song_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['song_id'], ['song.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('auth_user_user_permissions', schema=None) as batch_op:
        batch_op.drop_index('auth_user_user_permissions_permission_id_1fbb5f2c')
        batch_op.drop_index('auth_user_user_permissions_user_id_a95ead1b')

    op.drop_table('auth_user_user_permissions')
    with op.batch_alter_table('auth_user_groups', schema=None) as batch_op:
        batch_op.drop_index('auth_user_groups_group_id_97559544')
        batch_op.drop_index('auth_user_groups_user_id_6a12ed8b')

    op.drop_table('auth_user_groups')
    with op.batch_alter_table('django_admin_log', schema=None) as batch_op:
        batch_op.drop_index('django_admin_log_content_type_id_c4bce8eb')
        batch_op.drop_index('django_admin_log_user_id_c564eba6')

    op.drop_table('django_admin_log')
    with op.batch_alter_table('auth_permission', schema=None) as batch_op:
        batch_op.drop_index('auth_permission_content_type_id_2f476e4b')

    op.execute('DROP TABLE IF EXISTS auth_permission CASCADE')
    with op.batch_alter_table('django_session', schema=None) as batch_op:
        batch_op.drop_index('django_session_expire_date_a5c62663')
        batch_op.drop_index('django_session_session_key_c0390e0f_like')

    op.drop_table('django_session')
    op.drop_table('django_migrations')
    op.drop_table('django_content_type')
    op.execute('DROP TABLE IF EXISTS songs_song CASCADE')
    with op.batch_alter_table('auth_group', schema=None) as batch_op:
        batch_op.drop_index('auth_group_name_a6ea08ec_like')

    op.execute('DROP TABLE IF EXISTS auth_group CASCADE')
    with op.batch_alter_table('auth_group_permissions', schema=None) as batch_op:
        batch_op.drop_index('auth_group_permissions_group_id_b120cbf9')
        batch_op.drop_index('auth_group_permissions_permission_id_84c5c92e')

    op.drop_table('auth_group_permissions')
    with op.batch_alter_table('songs_queue', schema=None) as batch_op:
        batch_op.drop_index('songs_queue_song_id_70ed71bd')

    op.execute('DROP TABLE IF EXISTS songs_queue CASCADE')
    with op.batch_alter_table('auth_user', schema=None) as batch_op:
        batch_op.drop_index('auth_user_username_6821ab7c_like')

    op.drop_table('auth_user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auth_user',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('password', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('last_login', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('username', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=254), autoincrement=False, nullable=False),
    sa.Column('is_staff', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('date_joined', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='auth_user_pkey'),
    sa.UniqueConstraint('username', name='auth_user_username_key'),
    postgresql_ignore_search_path=False
    )
    with op.batch_alter_table('auth_user', schema=None) as batch_op:
        batch_op.create_index('auth_user_username_6821ab7c_like', ['username'], unique=False)

    op.create_table('songs_queue',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('song_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['song_id'], ['songs_song.id'], name='songs_queue_song_id_70ed71bd_fk_songs_song_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='songs_queue_pkey')
    )
    with op.batch_alter_table('songs_queue', schema=None) as batch_op:
        batch_op.create_index('songs_queue_song_id_70ed71bd', ['song_id'], unique=False)

    op.create_table('auth_group_permissions',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('group_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('permission_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['auth_group.id'], name='auth_group_permissions_group_id_b120cbf9_fk_auth_group_id', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['permission_id'], ['auth_permission.id'], name='auth_group_permissio_permission_id_84c5c92e_fk_auth_perm', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='auth_group_permissions_pkey'),
    sa.UniqueConstraint('group_id', 'permission_id', name='auth_group_permissions_group_id_permission_id_0cd325b0_uniq')
    )
    with op.batch_alter_table('auth_group_permissions', schema=None) as batch_op:
        batch_op.create_index('auth_group_permissions_permission_id_84c5c92e', ['permission_id'], unique=False)
        batch_op.create_index('auth_group_permissions_group_id_b120cbf9', ['group_id'], unique=False)

    op.create_table('auth_group',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='auth_group_pkey'),
    sa.UniqueConstraint('name', name='auth_group_name_key'),
    postgresql_ignore_search_path=False
    )
    with op.batch_alter_table('auth_group', schema=None) as batch_op:
        batch_op.create_index('auth_group_name_a6ea08ec_like', ['name'], unique=False)

    op.create_table('songs_song',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('track_name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('artist_name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('track_length', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('cover_url', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('track_id', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('uri', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('bpm', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='songs_song_pkey')
    )
    op.create_table('django_content_type',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('app_label', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('model', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='django_content_type_pkey'),
    sa.UniqueConstraint('app_label', 'model', name='django_content_type_app_label_model_76bd3d3b_uniq'),
    postgresql_ignore_search_path=False
    )
    op.create_table('django_migrations',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('app', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('applied', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='django_migrations_pkey')
    )
    op.create_table('django_session',
    sa.Column('session_key', sa.VARCHAR(length=40), autoincrement=False, nullable=False),
    sa.Column('session_data', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('expire_date', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('session_key', name='django_session_pkey')
    )
    with op.batch_alter_table('django_session', schema=None) as batch_op:
        batch_op.create_index('django_session_session_key_c0390e0f_like', ['session_key'], unique=False)
        batch_op.create_index('django_session_expire_date_a5c62663', ['expire_date'], unique=False)

    op.create_table('auth_permission',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('content_type_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('codename', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['content_type_id'], ['django_content_type.id'], name='auth_permission_content_type_id_2f476e4b_fk_django_co', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='auth_permission_pkey'),
    sa.UniqueConstraint('content_type_id', 'codename', name='auth_permission_content_type_id_codename_01ab375a_uniq'),
    postgresql_ignore_search_path=False
    )
    with op.batch_alter_table('auth_permission', schema=None) as batch_op:
        batch_op.create_index('auth_permission_content_type_id_2f476e4b', ['content_type_id'], unique=False)

    op.create_table('django_admin_log',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('action_time', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('object_id', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('object_repr', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('action_flag', sa.SMALLINT(), autoincrement=False, nullable=False),
    sa.Column('change_message', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('content_type_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.CheckConstraint('action_flag >= 0', name='django_admin_log_action_flag_check'),
    sa.ForeignKeyConstraint(['content_type_id'], ['django_content_type.id'], name='django_admin_log_content_type_id_c4bce8eb_fk_django_co', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name='django_admin_log_user_id_c564eba6_fk_auth_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='django_admin_log_pkey')
    )
    with op.batch_alter_table('django_admin_log', schema=None) as batch_op:
        batch_op.create_index('django_admin_log_user_id_c564eba6', ['user_id'], unique=False)
        batch_op.create_index('django_admin_log_content_type_id_c4bce8eb', ['content_type_id'], unique=False)

    op.create_table('auth_user_groups',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('group_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['auth_group.id'], name='auth_user_groups_group_id_97559544_fk_auth_group_id', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name='auth_user_groups_user_id_6a12ed8b_fk_auth_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='auth_user_groups_pkey'),
    sa.UniqueConstraint('user_id', 'group_id', name='auth_user_groups_user_id_group_id_94350c0c_uniq')
    )
    with op.batch_alter_table('auth_user_groups', schema=None) as batch_op:
        batch_op.create_index('auth_user_groups_user_id_6a12ed8b', ['user_id'], unique=False)
        batch_op.create_index('auth_user_groups_group_id_97559544', ['group_id'], unique=False)

    op.create_table('auth_user_user_permissions',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('permission_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['permission_id'], ['auth_permission.id'], name='auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name='auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='auth_user_user_permissions_pkey'),
    sa.UniqueConstraint('user_id', 'permission_id', name='auth_user_user_permissions_user_id_permission_id_14a6b632_uniq')
    )
    with op.batch_alter_table('auth_user_user_permissions', schema=None) as batch_op:
        batch_op.create_index('auth_user_user_permissions_user_id_a95ead1b', ['user_id'], unique=False)
        batch_op.create_index('auth_user_user_permissions_permission_id_1fbb5f2c', ['permission_id'], unique=False)

    op.drop_table('queue')
    op.drop_table('song')
    # ### end Alembic commands ###