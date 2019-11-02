from orator.migrations import Migration


class CreateServersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('servers') as table:
            table.increments('id')
            table.timestamps()
            table.char('name', 50)
            table.char('hostname', 50)
            table.enum('base_os', ['CentOS 6', 'CentOS 7', 'Ubuntu 16.04', 'Ubuntu 18.04'])
            table.integer('credentials_id').unsigned()
            table.foreign('credentials_id').references('id').on('credentials')
            table.enum('client', ['Nxtra', 'Ooredoo', 'Datahub', 'IndiQus'])
            table.enum('environment', ['Staging', 'Production', 'R&D'])
            table.char('ip_address', 30)

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('servers')
