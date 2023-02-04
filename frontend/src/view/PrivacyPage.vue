<template>
    <article class="lg:w-1/2 m-auto text-gray-800 dark:text-gray-200 text-justify md:p-16 pt-8">
        <h1 class="text-center text-4xl mb-4 font-bold">Privacy Policy</h1>
        <span class="text-gray-600 dark:text-gray-400">Last updated: 04.02.2023</span><br />
        This privacy policy provides an overview of the data that is collected, stored and, if necessary, processed.
        The data protection declaration only applies to this page ("green-web-analyzer.eu"). I, the operator of the
        site, believe that data protection should be a universal right of everyone, therefore as little data as possible
        is stored. By using the tool, you agree to the collection and use of information in accordance with this
        Privacy Policy.
        <h2 class="text-2xl mb-1 mt-4">What data do I collect?</h2>
        By requesting a report the following data is transmitted automatically and logged. The logs are not stored in
        files or a database, but are stored temporarely in-memory.
        <ul class="list-disc list-inside">
            <li>Date and time of request</li>
            <li>Browser type and version</li>
            <li>Operating system</li>
            <li>IP address of the person requesting the report</li>
            <li>The specified URL which is needed to create the report</li>
        </ul>

        <h2 class="text-2xl mb-1 mt-4">How will I use your data?</h2>
        The data of report requests is used for error analysis and ensuring the security of the systems. The data is
        stored for purely technical reasons and is not associated with a specific person. No data is shared with third
        parties.

        <h2 class="text-2xl mb-1 mt-4">Privacy policies of other websites</h2>
        This website contains links to other websites. Our privacy policy applies only to our website, so if
        you click on a link to another website, you should read their privacy policy.

        <h2 class="text-2xl mb-1 mt-4">Changes to the privacy policy</h2>
        I reserve the right to change this privacy policy. If there is a change to the privacy statement, it will apply
        to your next visit.

        <h2 class="text-2xl mb-1 mt-4">How to contact me</h2>
        If you have any questions about the privacy policy, the data I hold on you, or you would like to
        exercise one of your data protection rights granted by the GDPR, please do not hesitate to contact me.
        <ul class="list-disc list-inside">
            <li>Patrick Geiger</li>
            <li>dev[at]patrickgeiger.eu</li>
        </ul>

    </article>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({})
</script>