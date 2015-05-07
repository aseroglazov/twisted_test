Ext.define('MyApp.view.MyViewport', {
    extend: 'Ext.container.Viewport',
    alias: 'widget.myviewport',

    requires: [
        'MyApp.view.MyViewportViewModel',
        'MyApp.view.MyViewportViewController',
        'Ext.form.Panel',
        'Ext.form.field.File',
        'Ext.button.Button'
    ],

    controller: 'myviewport',
    viewModel: {
        type: 'myviewport'
    },

    items: [
        {
            xtype: 'form',
            reference: 'flipping_form',
            bodyPadding: 10,
            title: 'Image flipping',
            titleAlign: 'center',
            url: '/api/images/add',
            layout: {
                type: 'vbox',
                align: 'stretch'
            },
            items: [
                {
                    xtype: 'filefield',
                    fieldLabel: 'Choose image',
                    name: 'image'
                },
                {
                    xtype: 'container',
                    flex: 1,
                    items: [
                        {
                            xtype: 'button',
                            text: 'Download flipped image',
                            listeners: {
                                click: 'onDownloadFlippedImageClick'
                            }
                        }
                    ]
                }
            ],
            listeners: {
                actioncomplete: 'onSuccess',
                actionfailed: 'onFailed'
            }
        }
    ]

});
