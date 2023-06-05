<template>
    <BasicCard class="m-2 md:m-16 text-gray-800 dark:text-gray-200 text-center">
        <h1 class="text-4xl mb-4 font-bold">About</h1>
        <h2 class="text-2xl mb-4 mt-8 font-bold">What is this website?</h2>
        <p class="text-lg lg:w-3/4 2xl:w-1/4 mx-auto text-justify">
            This website is a tool for analysing a public website according certain factors (called metrics and criteria).
            The metrics are statistics about this webpage, such as the amount of data transferred or the estimated CO2
            emissions caused by loading the website once. Criteria are specific factors about how a website can be made more
            efficiant or improved, for example by using more modern technology. The context of this analysis is Green IT
            and how websites can be improved in terms of data minimisation and efficiency.
        </p>
        <h2 class="text-2xl mb-4 mt-8 font-bold">Why?</h2>
        <p class="text-lg lg:w-3/4 2xl:w-1/4 mx-auto text-justify">
            Climate change is one of the biggest challenges facing the modern world, and the information and technology
            sector is one of drivers of emissions which is believed to increase over time. The ICT sector has an estimated
            to account for between 2.1% and 3.9% of the global greenhouse gas emissions
            <RouterLink to="#literature" class="cursor-pointer">[1]</RouterLink>.
        </p>


        <h2 class="text-2xl mb-4 mt-8 font-bold">Methology</h2>
        <h3 class="text-lg mb-2 mt-4 font-bold">CO2 estimations</h3>
        <p class="text-lg lg:w-3/4 2xl:w-1/4 mx-auto text-justify list-decimal">
            The CO2.js library <RouterLink to="#literature" class="cursor-pointer">[2]</RouterLink> from the Green Web
            Foundation is used to estimate the CO2 emissions caused by a website visit. This blog post
            <RouterLink to="#literature" class="cursor-pointer">[3]</RouterLink> explains in detail how the estimates are
            calculated.

        </p>
        <h3 class="text-lg mb-2 mt-4 font-bold">Green energy</h3>
        <p class="text-lg lg:w-3/4 2xl:w-1/4 mx-auto text-justify list-decimal">
            To check wether a website uses renewable energy sources, the Green Web Foundation's Greencheck API is used
            <RouterLink to="#literature" class="cursor-pointer">[4]</RouterLink>. This API will compares the server used
            with their dataset which includes hosting providers that use renewable energy.
        </p>


        <h2 class="text-2xl mb-4 mt-16 font-bold" id="literature">Literature</h2>
        <p>
        <ol class="text-lg w-4/5 lg:w-3/4 2xl:w-1/4 mx-auto text-justify list-decimal break-words">
            <li>C. Freitag, M. Berners-Lee, K. Widdicks, B. Knowles, G. S. Blair und A. Friday, “The real climate and
                transformative impact of ICT: A critique of estimates, trends, and regulations”, Patterns, Jg. 2, Nr. 9, S.
                100 340, Sep. 2021. DOI:
                <a href="https://doi.org/10.1016/j.patter.2021.100340" target="_blank"
                    class="hover:underline cursor-pointer">
                    10.1016/j.patter.2021.100340.
                </a>
            </li>
            <li>
                The Green Web Foundation, CO2.js, online, 2022. URL:
                <a href="https://developers.thegreenwebfoundation.org/co2js/overview/" target="_blank"
                    class="hover:underline cursor-pointer">
                    https://developers.thegreenwebfoundation.org/co2js/overview/
                </a>
            </li>
            <li>
                C. Adams, R. Baouendi, T. Frick, T. Greenwood und D. Williams, Calculating Digital Emissions, online, Apr.
                2022. URL:
                <a href="https://sustainablewebdesign.org/calculating-digital-emissions/" target="_blank"
                    class="hover:underline cursor-pointer">
                    https://sustainablewebdesign.org/calculating-digital-emissions/
                </a>
            </li>
            <li>
                The Green Web Foundation, Greencheck API, online, URL:
                <a href="https://developers.thegreenwebfoundation.org/api/greencheck/v3/check-single-domain/"
                    target="_blank" class="hover:underline cursor-pointer">
                    https://developers.thegreenwebfoundation.org/api/greencheck/v3/check-single-domain/
                </a>
            </li>
        </ol>
        </p>
    </BasicCard>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({})
</script>