<template>
  <div class="flex">
    <div class="sidebar">
      <h2>On This Page</h2>
      <h4>Introduction</h4>
      <h4>Background</h4>
      <h4>The F3 Framework</h4>
      <h4>Design Principles</h4>
      <h4>Foundation</h4>
      <h4>How to Use</h4>
      <h4>Appendix</h4>
    </div>
    <div class="main">
      <breadcrumb-component :breadcrumbItems="breadcrumbItems" class="mb-2 -ml-3" />

      <h1>Design Principles and Methodology </h1>
      <!-- <h2 id="introduction">Introduction</h2>
      <p>The Fight Financial Fraud (F3) Framework is a curated knowledge base of tactics, techniques, and procedures
        (TTPs) used by fraud actors. The F3 Framework includes behaviors that characterize known fraud TTPs and
        references existing <a href="https://attack.mitre.org/">MITRE ATT&CK®</a> cyber techniques as applicable to
        financial fraud. The F3 Framework provides a living
        knowledge base of fraud actor TTPs based on real-world observations of fraud incidents as seen by banking
        institutions. </p>
      <blockquote>
        A banking institution is a type of financial organization that is legally authorized to provide the public with
        services and products related to money, such as deposit accounts and loans. Banking institutions are regulated
        by
        the government and are legally required to follow Anti-Money Laundering (AML) rules and regulations under laws
        like the Bank Secrecy Act. Banking institutions must conduct due diligence (i.e., Know Your Customer or KYC),
        monitor transactions to detect and prevent illegal activity, and report suspicious activities to the proper
        authorities.
      </blockquote>
      <p>At a high level, the F3 Framework is a behavioral model that consists of the following core components: </p>
      <ul>
        <li><span class="font-bold">Tactics</span>, denoting short-term, tactical fraud actor goals during an attack;
        </li>
        <li><span class="font-bold">Techniques</span>, describing the means by which fraud actors achieve tactical
          goals; and </li>
        <li><span class="font-bold">Sub-techniques</span>, describing more specific means by which fraud actors achieve
          tactical goals at a lower level
          than techniques. </li>
      </ul>
      <p>This relatively simple representation strikes a useful balance between sufficient technical detail at the
        technique level and the context around why actions occur at the tactic level. </p>
      <p>The F3 Framework will evolve over time as fraud actor TTPs evolve and new behaviors are identified. New
        information relevant to fraud TTPs can come from many different sources, including fraud incident reports and
        contributions from the fraud community. </p>
      <h2 id="background">Background</h2>

      <p>Preventing fraud is an ongoing challenge for banking institutions. Success depends on access to data, insight,
        and specialized capabilities, but these are often fragmented across cybersecurity, fraud, anti-money laundering,
        and other teams.</p>
      <p>The F3 Framework was developed by and for fraud-fusion analysts to allow fraud incidents to help such teams
        coordinate and direct their anti-fraud efforts using a common language.</p>

      <p>Fraud incidents contain cyber artifacts that can be used to find future fraud, and the F3 Framework provides
        that fusion of cyber and fraud data sources into tactics and techniques specific to fraud incidents. The
        framework provides a collective ability to enumerate the material events of a fraud incident and to implement
        controls that disrupt fraud through emulating, detecting, and preventing the TTPs used in these incidents.</p>

      <h3>Foundation</h3>
      <p>Includes derivation from prior work, including</p>
      <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
        <div class="foundation-item">
          <h4><a href="https://www.fsisac.com/knowledge/cyber-fraud-prevention-framework" target="_blank">FS-ISAC Cyber
              Fraud Prevention Framework</a></h4>
          <p>Framework that enables gathering and sharing of cyber fraud information across the financial sector
            regarding fraud conducted on cyber channels </p>
        </div>
        <div class="foundation-item">
          <h4><a href="https://nrf.com/research/retail-fraud-taxonomy" target="_blank">National Retail Federation Retail
              Fraud Taxonomy</a></h4>
          <p>Framework for assessing and categorizing retail fraud threats and identifying appropriate actions to
            mitigate them </p>
        </div>
        <div class="foundation-item">
          <h4><a href="https://www.group-ib.com/products/cyber-fraud-intelligence-platform/" target="_blank">Group-IB
              Cyber Fraud Intelligence</a></h4>
          <p>Framework to systematically break down fraud actor actions and behaviors across an incident into stages and
            techniques </p>
        </div>
        <div class="foundation-item">
          <h4><a href="https://github.com/stripe/ft3" target="_blank">Stripe Fraud Tools Tactics and Techniques
              (FT3)</a></h4>
          <p>Framework to enhance understanding of the tactics, techniques, and procedures (TTPs) used by actors in
            fraudulent activities </p>
        </div>
      </div> -->
      <p>The F3 Framework is grounded in real-world fraud actor behavior derived from the as and developed by fraud
        fusion analysts. The framework is modeled after ATT&CK, inspired by the MITRE ATT&CK®: Design and Philosophy2,
        to enumerate fraud actor behavior in banking institutions. The F3 Framework includes new content to describe
        fraud technical behaviors for which there is no existing ATT&CK content, and references and refines existing
        ATT&CK techniques when they are applicable to financial fraud. </p>

      <h2 id="design-principles">Design Principles</h2>
      <p>The F3 Framework was developed using a set of clear design principles, informed by the practical experience of
        fraud fusion analysts and applied to define its tactics, techniques, and sub-techniques. These design principles
        form the conceptual foundation of the methodology used to create the F3 Framework and will continue to guide its
        maintenance and future enhancement.
      </p>
      <p>
        Fraud methods will evolve over time and additional knowledge will be gained. The F3 development process will
        remain focused on accurately representing how fraud actors operate, through following these design principles
        and providing information in a way that makes it easy to categorize fraud actor actions and relate those actions
        to defenses. This enables defenders to consistently describe, detect, and prevent fraud incidents using a
        common, structured approach. </p>
      <p>There are four Design Principles that are core to the development of the F3 Framework: </p>
      <div class="design-principle">
        <h3>Design Principle #1: The financial institution must see the effects of a technique during the fraud
          incident.
        </h3>
        <p>The financial institution must be able to observe and understand how a technique impacts a fraud incident.
          Seeing how the behavior or action fits in the overall outcome of the fraud incident is needed so that its
          effectiveness, limitations, and side effects can be accurately evaluated and used to improve future strategies
          for mitigating and detecting the behavior. </p>
        <p>Visibility into what the fraud actor did during each step. Future fraud strategies, rules, processes </p>
      </div>
      <div class="design-principle">
        <h3>Design Principle #2: The fraud incident must contain a cyber-based technique. </h3>
        <p>The fraud incident must involve the use of a cyber-based technique as an element of how the fraud is carried
          out. This means the fraud incident includes use of digital or technological methods, such as phishing,
          malware, unauthorized access to information systems, or other forms of cyber manipulation, rather than being
          solely physical, social, or paper-based in nature. The requirement to contain a cyber artifact is for analysts
          to use to help detect future fraud attempts.</p>
        <p>WHY: actionable support of cyber threat intelligence, detection engineering, or security control
          implementation</p>
      </div>
      <div class="design-principle">
        <h3>Design Principle #3: Techniques must describe the behavior of the adversary.</h3>
        <p>Techniques represent 'how' a fraud actor achieves a tactical goal by performing an action. Each technique
          captures a distinct, observable action or behavior that is used by the fraud actor to achieve their objective.
        </p>
        <p>Not an entity, not a tool</p>
      </div>
      <div class="design-principle">
        <h3>Design Principle #4: For behaviors with the same "how” performed in different ways, we must create a
          technique/sub-technique relationship.</h3>
        <p> Not all techniques will have sub-techniques. Sub-techniques describe more specific means by which fraud
          actors achieve tactical goals at a lower level than techniques. Sub-techniques further break down behaviors
          described by techniques into more specific descriptions of how behavior is used to achieve an objective. </p>
        <p>Sub-techniques allow for a similar abstraction level of techniques across the framework, while demonstrating
          the many ways that techniques are performed. </p>
      </div>
      <h2>Design Principle #1: The financial institution must see the effects of a technique during the fraud incident.
      </h2>
      <p>The banking institution must be able to observe and understand how a technique impacts a fraud incident. Seeing
        how the behavior or action fits in the overall outcome of the fraud incident is needed so that its
        effectiveness, limitations, and side effects can be accurately evaluated and used to improve future strategies
        for mitigating and detecting the behavior. </p>
      <p>Visibility into what the fraud actor does during each step of a fraud incident provides a clear understanding
        of their methods and behaviors. This insight can then be used to inform and shape future fraud strategies,
        rules, and processes, helping organizations better prevent, detect, and respond to similar threats in the
        future. </p>
      <h2>Design Principle #2: The fraud incident must contain a cyber-based technique. </h2>
      <p>The fraud incident must involve the use of a cyber-based technique as an element of how the fraud is carried
        out. This means the fraud incident includes use of digital or technological methods, such as phishing, malware,
        unauthorized access to information systems, or other forms of cyber manipulation, rather than being solely
        physical, social, or paper-based in nature. The requirement to contain a cyber artifact is for analysts to use
        to help detect future fraud attempts. </p>
      <p>The purpose is to provide actionable support for cyber threat intelligence, detection engineering, and security
        control implementation, and performing investigations. This ensures that insights are not only understood but
        can be effectively applied to strengthen an organization's overall security posture. </p>
      <h2>Design Principle #3: Techniques must describe the behavior of the adversary. </h2>
      <p>Techniques represent 'how' a fraud actor achieves a tactical goal by performing an action. Each technique
        captures a distinct, observable action or behavior that is used by the fraud actor to achieve their objective. A
        technique is not an entity or a tool, but rather the specific way those entities or tools are used. Techniques
        focus on actions known to be used by threat actors, represented by standardized terms. </p>
      <p>Defining techniques in this way enables clear recognition and consistent categorization of fraud behaviors
        within an incident. This also provides operational value by ensuring that defenses such as detection logic and
        security control design can be mapped to the actions performed by fraud actors, rather than to the specific
        entities or tools used to achieve their goals. </p>
      <h2>Design Principle #4: For behaviors with the same "how” performed in different ways, we must create a
        technique/sub-technique relationship. </h2>
      <p>Not all techniques will have sub-techniques. Sub-techniques describe more specific means by which fraud actors
        achieve tactical goals at a lower level than techniques. Sub-techniques further break down behaviors described
        by techniques into more specific descriptions of how behavior is used to achieve an objective. </p>
      <p>Techniques provide a high-level, manageable view of fraud behavior, while sub-techniques provide the additional
        detail needed for demonstrating the many ways that techniques are performed. This structure helps to reduce
        overlap and allows for a similar abstraction level of techniques across the framework, capturing variations and
        lower-level details as sub-techniques. </p>



    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import BreadcrumbComponent from "../components/BreadcrumbComponent.vue";

export default defineComponent({
  components: { BreadcrumbComponent },
  data() {
    return {
      breadcrumbItems: [
        { label: "About", route: "/about" },
        { label: "Design Principles", route: "/about/methodology" },

      ],
    }
  }
})
</script>

<style scoped>
ul {
  @apply list-inside;
  list-style-type: square;
}

p {
  @apply mb-2 mt-1
}

blockquote {
  @apply bg-ctid-light-gray/30 border-l-4 border-ctid-light-gray px-8 py-4 italic my-4 text-base
}

.design-principle, .foundation-item {
  @apply border-ctid-light-gray border-[1px] py-4 px-6 my-1
}

.design-principle h3 {
  @apply font-medium
}

.subtitle {
  @apply font-medium italic
}
</style>
