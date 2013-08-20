#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2012 Rackspace

# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os
import pyrax

pyrax.set_setting("identity_type", "rackspace")
creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)
clb = pyrax.cloud_loadbalancers

lb = clb.list()[0]
orig_meta = lb.get_metadata()
print "Initial metadata:", orig_meta
lb.set_metadata({"a": "one", "b": "two", "c": "three"})
print "New metadata:", lb.get_metadata()
lb.update_metadata({"d": "four"})
print "Updated metadata:", lb.get_metadata()
lb.set_metadata({"e": "five"})
print "After set_metadata:", lb.get_metadata()
lb.delete_metadata()
print "After delete_metadata:", lb.get_metadata()
if orig_meta:
    lb.set_metadata(orig_meta)
    print "After restoring original metadata:", lb.get_metadata()
