.. Copyright (C) 2015, Wazuh, Inc.

.. meta::
  :description: Learn considerations for configuring multiple services with the Wazuh Azure module in this section of the Wazuh documentation.

.. _azure_considerations:

Considerations for configuration
================================

Configuring multiple services
-----------------------------

It is possible to add more than one ``request`` block at the same time in the same configuration. Each request will be processed sequentially. Here is an example configuration:

.. code-block:: xml

    <wodle name="azure-logs">
        <disabled>no</disabled>
        <run_on_start>yes</run_on_start>

        <log_analytics>
            <auth_path>/var/ossec/wodles/credentials/log_analytics_credentials</auth_path>
            <tenantdomain>wazuh.onmicrosoft.com</tenantdomain>

            <request>
                <tag>azure-activity</tag>
                <query>AzureActivity | where SubscriptionId == 2d7...61d </query>
                <workspace>d6b...efa</workspace>
                <time_offset>36h</time_offset>
            </request>

            <request>
                <tag>azure-activity</tag>
                <query>AzureActivity | where SubscriptionId == 3f5...21g </query>
                <workspace>d6b...efa</workspace>
                <time_offset>2d</time_offset>
            </request>

        </log_analytics>

        <graph>
            <auth_path>/var/ossec/wodles/credentials/graph_credentials</auth_path>
            <tenantdomain>wazuh.onmicrosoft.com</tenantdomain>

            <request>
                <tag>microsoft-entra_id-1</tag>
                <query>auditLogs/directoryAudits</query>
                <time_offset>1d</time_offset>
            </request>

            <request>
                <tag>microsoft-entra_id-2</tag>
                <query>auditLogs/directoryAudits</query>
                <time_offset>1d</time_offset>
            </request>

        </graph>

        <storage>
            <auth_path>/var/ossec/wodles/credentials/storage_credentials</auth_path>
            <tag>azure-activity</tag>

            <container name="insights-operational-logs">
                <blobs>.json</blobs>
                <content_type>json_inline</content_type>
                <time_offset>24h</time_offset>
            </container>

            <container name="insights-operational-logs">
                <blobs>.txt</blobs>
                <content_type>json_inline</content_type>
                <time_offset>24h</time_offset>
            </container>

        </storage>
    </wodle>