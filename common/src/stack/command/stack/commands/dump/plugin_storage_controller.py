#
# @SI_Copyright@
# Copyright (c) 2006 - 2017 StackIQ Inc.
# All rights reserved. stacki(r) v4.0 stacki.com
# https://github.com/Teradata/stacki/blob/master/LICENSE.txt
# @SI_Copyright@
# 
# @Copyright@
# Copyright (c) 2000 - 2010 The Regents of the University of California
# All rights reserved. Rocks(r) v5.4 www.rocksclusters.org
# https://github.com/Teradata/stacki/blob/master/LICENSE-ROCKS.txt
# @Copyright@
#

import stack.commands

class Plugin(stack.commands.Plugin):

	def provides(self):
		return 'storage-controller'
		
	def requires(self):
		return [ 'appliance', 'host' ]
		
	def run(self, args):
		self.owner.addText(self.owner.command('dump.storage.controller',
			[]))
		
