<template>
    <BasicCard class="m-2 md:m-16 text-gray-800 dark:text-gray-200 text-center">
        <h1 class="text-4xl mb-4 font-bold">About</h1>
        <h2 class="text-2xl mb-4 mt-8 font-bold">What is this website?</h2>
        <p class="text-lg lg:w-3/4 2xl:w-1/4 mx-auto text-justify">
            This website is a tool to analyse a public website on certain factors (called metrics and criteria). The metrics
            represent statistics about that webpage, like the size of data transfer or the estimated CO2 emissions that was
            caused by loading the website once. The criteria are certain factors how a website can be more efficiant or
            improved, for example by using more modern technologies. The context of this analysis is Green IT and how
            websites can be improved with regard to data minimisation and efficiency.
        </p>
        <h2 class="text-2xl mb-4 mt-8 font-bold">Why?</h2>
        <p class="text-lg lg:w-3/4 2xl:w-1/4 mx-auto text-justify">
            The climate change is one of the biggest challenges in the modern world and the Information and technology
            sector is one of factor which is causing emissions which is believed to increase with time.
            The Information and technology has an estimated share between 2.1% and 3.9% of the global GHG emissions
            <RouterLink to="#literature" class="cursor-pointer">[1]</RouterLink>.
        </p>


        <h2 class="text-2xl mb-4 mt-8 font-bold">Methology</h2>
        <h3 class="text-lg mb-2 mt-4 font-bold">CO2 estimations</h3>
        <p class="text-lg lg:w-3/4 2xl:w-1/4 mx-auto text-justify list-decimal">
            In order to estimate the caused CO2 emissions for one visit of the website the CO2.js library
            <RouterLink to="#literature" class="cursor-pointer">[2]</RouterLink> by the Green Web Foundation is used. This
            blog article <RouterLink to="#literature" class="cursor-pointer">[3]</RouterLink> explains how the estimations
            are calculated in detail.
        </p>
        <h3 class="text-lg mb-2 mt-4 font-bold">Green energy</h3>
        <p class="text-lg lg:w-3/4 2xl:w-1/4 mx-auto text-justify list-decimal">
            To check if a website is using renewable energy sources, the so called Greencheck API by the Green Web
            Foundation is used <RouterLink to="#literature" class="cursor-pointer">[4]</RouterLink>. This API will
            crossreference the server used with their dataset which includes hosting provider that are using renewable
            energy.
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