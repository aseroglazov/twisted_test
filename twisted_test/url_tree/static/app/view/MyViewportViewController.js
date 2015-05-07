Ext.define('MyApp.view.MyViewportViewController', {
    extend: 'Ext.app.ViewController',
    alias: 'controller.myviewport',

    onDownloadFlippedImageClick: function(button, e, eOpts) {

        this.lookupReference('flipping_form').submit();
    },

    onSuccess: function(basic, action, eOpts) {
        var response = Ext.JSON.decode(action.response.responseText);

        window.open('/api/images/get/' + response.data.id + '/flip');
    },

    onFailed: function(basic, action, eOpts) {
        var response = Ext.JSON.decode(action.response.responseText);
        alert(response.error);
    }

});
