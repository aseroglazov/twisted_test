Ext.Loader.setConfig({

});


Ext.application({
    views: [
        'MyViewport'
    ],
    name: 'MyApp',

    launch: function() {
        Ext.create('MyApp.view.MyViewport');
    }

});
