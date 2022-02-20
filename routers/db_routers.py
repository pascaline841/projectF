class RouterDefault:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {'client', 'auth', 'contenttypes'}
    
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        return 'default' if model._meta.app_label in self.route_app_labels else None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth_db.
        """
        return 'default' if model._meta.app_label in self.route_app_labels else None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        return db == 'default' if app_label in self.route_app_labels else None


class RouterDb1:
    route_app_labels = {'client'}

    def db_for_read(self, model, **hints):
        """Reads go to db_1."""
        return 'db_1' if model._meta.app_label in self.route_app_labels else None

    def db_for_write(self, model, **hints):
        """Writes always go to db_1."""
        return 'db_1' if model._meta.app_label in self.route_app_labels else None
    
    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the db_1 pool.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """All non-auth models end up in this pool."""
        return db == 'db_1' if app_label in self.route_app_labels else None   
    