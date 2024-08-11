/*
Copyright (c) 2003-2015, CKSource - Frederico Knabben. All rights reserved.
For licensing, see license.txt or http://cksource.com/ckfinder/license
*/

CKFinder.customConfig = function( config )
{
	// http://docs.cksource.com/ckfinder_2.x_api/symbols/CKFinder.config.html
    config.basePath = '/static/admin/plugins/ckfinder/'
    config.filebrowserBrowseUrl = '/static/admin/plugins/ckfinder/ckfinder.html'
    config.filebrowserUploadUrl = '/static/admin/plugins/ckfinder/core/connector/php/connector.php?command=QuickUpload&type=Files'
	// Sample configuration options:
	// config.uiColor = '#BDE31E';
	// config.language = 'fr';
	// config.removePlugins = 'basket';

};
