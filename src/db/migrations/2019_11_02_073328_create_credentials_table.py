from orator.migrations import Migration


class CreateCredentialsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('credentials') as table:
            table.increments('id')
            table.timestamps()
            table.char('username', 25)
            table.char('password', 50).nullable()
            table.char('private_key', 100).nullable()
            table.char('public_key', 100).nullable()
            table.boolean('active')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('credentials')
