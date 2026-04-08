<template>
  <div class="flex h-full flex-col-reverse md:flex-row">
    <div class="sidebar">
      <h2>Download Paper</h2>
      <p>The content on this page has been published as a standalone paper.</p>
      <a :href="downloadUrl" class="btn btn-external"
        download="MITRE F3 Design Principles and Methodology.pdf">Download Paper <i class="pi pi-download"></i></a>

      <h2>On This Page</h2>
      <template v-for="heading of topLevelHeadings" :key="heading.label">
        <h3 @click="scrollToHeading(heading.id)" class=" cursor-pointer">
          {{ heading.label }}
        </h3>
        <h4 v-for="subheading of heading.subheadings" :key="subheading.label" @click="scrollToHeading(subheading.id)"
          class="ml-4 cursor-pointer">{{ subheading.label }}</h4>
      </template>
    </div>
    <div class="main">
      <breadcrumb-component :breadcrumbItems="breadcrumbItems" class="mb-2 -ml-3" />

      <h1>Design Principles and Methodology </h1>

      <p>The MITRE Fight Fraud Framework (F3)™ is a curated knowledge base of tactics and techniques
        used by fraud actors. MITRE F3™ includes behaviors that characterize known fraud TTPs and references existing <a
          href="https://attack.mitre.org/" target="blank">MITRE ATT&CK®</a> techniques as applicable to financial
        fraud. These incidents involve the intentional use of deceptive or illegal practices to fraudulently obtain money, assets, or information from individuals or institutions and include actions carried out over cyber channels. F3 provides a common structure and taxonomy and a collective ability to enumerate the material events of cyber fraud incidents and enable partnership on fraud prevention and response.</p>

      <p>The initial release focuses on financial fraud as seen by banking institutions<sup><a href=""
            target="blank">1</a></sup>. </p>
      <p>At a high level, F3 is a behavioral model that consists of the following core components: </p>
      <ul>
        <li>Tactics, denoting short-term, tactical fraud actor goals during an attack; </li>
        <li>Techniques, describing the means by which fraud actors achieve tactical goals; and </li>
        <li>Sub-techniques, describing more specific means by which fraud actors achieve tactical goals at a lower level
          than techniques. </li>
      </ul>

      <p>This relatively simple representation strikes a useful balance between sufficient technical detail at the
        technique level and the context around why actions occur at the tactic level.
      </p>
      <p>
        F3 will evolve over time as fraud actor TTPs evolve and new behaviors are identified. New information relevant
        to fraud TTPs can come from many different sources, including fraud incident reports and contributions from the
        fraud community. </p>

      <h2 id="background">Background</h2>
      <p>Preventing fraud is an ongoing challenge for many institutions. Banking institutions in particular are
        regulated by the government and are legally required to follow Anti-Money Laundering (AML) rules and regulations
        under laws like the Bank Secrecy Act. These institutions must conduct due diligence (i.e., Know Your Customer or
        KYC), monitor transactions to detect and prevent illegal activity, and report suspicious activities to the
        proper authorities. Success depends on access to data, insight, and specialized capabilities, but these are
        often fragmented across cybersecurity, fraud, anti-money laundering, and other teams. </p>
      <p>F3 was created by and for fraud-fusion analysts to help teams coordinate and focus their anti-fraud efforts
        using a shared, consistent language. By anchoring the framework in actual fraud incidents, it ensures the
        knowledge base remains closely aligned with real-world threats that analysts are likely to encounter over the
        course of a cyber fraud incident.
      </p>
      <p>
        F3 is grounded in real-world fraud actor behavior derived from existing fraud frameworks and developed by fraud
        fusion analysts. The framework is modeled after ATT&CK, inspired by the MITRE ATT&CK®: Design and
        Philosophy<sup>2</sup>,
        to enumerate fraud actor behavior. F3 includes new content to describe fraud technical behaviors for which there
        is no existing ATT&CK content, and references and refines existing ATT&CK techniques when they are applicable to
        financial fraud. The initial release focuses on financial fraud as seen by banking institutions. </p>

      <h2 id="the-f3-model">The F3 Model</h2>
      <p>Fraud incidents contain cyber artifacts that can be used to find future fraud, and F3 provides that fusion of
        cyber and fraud data sources into tactics and techniques specific to fraud incidents. The framework provides a
        collective ability to enumerate the material events of a fraud incident and to implement controls that disrupt
        fraud through emulating, detecting, and preventing the TTPs used in these incidents. Key aspects of the F3 model
        are: </p>
      <ul>
        <li>Common structure and taxonomy</li>
        <li>Partnership on fraud prevention and response</li>
        <li>Shared indicators among institutions </li>
      </ul>
      <p>The basis of F3 is the set of techniques and sub-techniques that represent actions that fraud actors perform to
        accomplish objectives. Those objectives are represented by the tactic categories that the techniques and
        sub-techniques fall under. This relatively simple representation strikes a useful balance between sufficient
        technical detail at the technique level and the context around why actions occur at the tactic level. </p>
      <h3 id="design-principles">Design Principles</h3>
      <p>F3 was developed using a set of clear design principles, informed by the practical experience of fraud fusion
        analysts and applied to define its tactics, techniques, and sub-techniques. These design principles form the
        conceptual foundation of the methodology used to create F3 and will continue to guide its maintenance and future
        enhancement.
      </p>
      <p>Fraud methods will evolve over time and additional knowledge will be gained. The F3 development process will
        remain focused on accurately representing how fraud actors operate, through following these design principles
        and providing information in a way that makes it easy to categorize fraud actor actions and relate those actions
        to defenses. This enables defenders to consistently describe, detect, and prevent fraud incidents using a
        common, structured approach.
      </p>
      <p>There are four Design Principles that are core to the development of F3:</p>
      <ul>
        <li>Design Principle #1: The financial institution must see the effects of a technique during the fraud
          incident.
        </li>
        <li>Design Principle #2: The fraud incident must contain a cyber-based technique.
        </li>
        <li>Design Principle #3: Techniques must describe the behavior of the adversary.
        </li>
        <li>Design Principle #4: For behaviors with the same "how” performed in different ways, we must create a
          technique/sub-technique relationship.
        </li>
      </ul>
      <p>Fraud methods will evolve over time and additional knowledge will be gained. The F3 development process will
        remain focused on accurately representing how fraud actors operate, through following these design principles
        and providing information in a way that makes it easy to categorize fraud actor actions and relate those actions
        to defenses. This enables defenders to consistently describe, detect, and prevent fraud incidents using a
        common, structured approach. </p>
      <h4>Design Principle #1: The institution must see the effects of a technique during the fraud incident. </h4>
      <p>The institution must be able to observe and understand how a technique impacts a fraud incident. Seeing how the
        behavior or action fits in the overall outcome of the fraud incident is needed so that its effectiveness,
        limitations, and side effects can be accurately evaluated and used to improve future strategies for mitigating
        and detecting the behavior. </p>
      <p>Visibility into what the fraud actor does during each step of a fraud incident provides a clear understanding
        of their methods and behaviors. This insight can then be used to inform and shape future fraud strategies,
        rules, and processes, helping organizations better prevent, detect, and respond to similar threats in the
        future. </p>
      <h4>Design Principle #2: The fraud incident must contain a cyber-based technique. </h4>
      <p>The fraud incident must involve the use of a cyber-based technique as an element of how the fraud is carried
        out. This means the fraud incident includes use of digital or technological methods, such as phishing, malware,
        unauthorized access to information systems, or other forms of cyber manipulation, rather than being solely
        physical, social, or paper-based in nature. The requirement to contain a cyber artifact is for analysts to use
        to help detect future fraud attempts. </p>
      <p>The purpose is to provide actionable support for cyber threat intelligence, detection engineering, security
        control implementation, and performing investigations. This ensures that insights are not only understood but
        can be effectively applied to strengthen an organization’s overall security posture. </p>
      <h4>Design Principle #3: Techniques must describe the behavior of the adversary. </h4>
      <p>Techniques represent 'how' a fraud actor achieves a tactical goal by performing an action. Each technique
        captures a distinct, observable action or behavior that is used by the fraud actor to achieve their objective. A
        technique is not an entity or a tool, but rather the specific way those entities or tools are used. Techniques
        focus on actions known to be used by threat actors, represented by standardized terms. </p>
      <p>Defining techniques in this way enables clear recognition and consistent categorization of fraud behaviors
        within an incident. This also provides operational value by ensuring that defenses such as detection logic and
        security control design can be mapped to the actions performed by fraud actors, rather than to the specific
        entities or tools used to achieve their goals. </p>
      <h4>Design Principle #4: Behaviors with the same "how” performed in different ways must use a
        technique/sub-technique relationship. </h4>
      <p>Not all techniques will have sub-techniques. Sub-techniques describe more specific means by which fraud actors
        achieve tactical goals at a lower level than techniques. Sub-techniques further break down behaviors described
        by techniques into more specific descriptions of how behavior is used to achieve an objective. </p>
      <p>Techniques provide a high-level, manageable view of fraud behavior, while sub-techniques provide the additional
        detail needed for demonstrating the many ways that techniques are performed. This structure helps to reduce
        overlap and allows for a similar abstraction level of techniques across the framework, capturing variations and
        lower-level details as sub-techniques. </p>
      <h3 id="matrix">The F3 Matrix</h3>
      <p>The relationship between tactics, techniques, and sub-techniques can be visualized in the F3
        matrix<sup>3</sup>. Figure 1 depicts the F3 Matrix: </p>
      <figure>
        <img :src="matrixImage"
          alt="F3 matrix which visualizes relationships between tactics, techniques, and subtechniques" />
        <figcaption>Figure 1: Placeholder for F3 Matrix Overview</figcaption>
      </figure>
      <p>For example, under the Resource Development tactic (this is the fraud actor's goal, to prepare for fraud in the
        target environment), there are a series of techniques including Acquire Infrastructure and Create Fake
        Materials. Each of these is a single technique that fraud actors may use to achieve the goal of setting up
        infrastructure and capabilities to support fraud activities. </p>
      <p>Furthermore, some techniques can be broken down into sub-techniques that describe in more detail how those
        behaviors can be performed. For example, Create Fake Materials has two sub-techniques, Fake Documents and Fake
        Website, to describe how forged or fraudulent resources may be created to support attempted fraud. Figure 3
        depicts the Acquire Infrastructure and Create Fake Materials techniques under the Resource Development tactic,
        expanded to show their respective sub-techniques. </p>
      <figure>
        <img :src="expandedImage" class=" m-auto"
          alt="Expanded technique in matrix that shows what it looks like for a technique to have subtechniques" />
        <figcaption>Figure 2: Examples of Expanded Techniques</figcaption>
      </figure>
      <h3 id="tactics">Tactics</h3>
      <p>Tactics represent the “why” of an F3 technique or sub-technique: the fraud actor's tactical goal and the reason
        for performing an action. Tactics are not the same as phases of a fraud incident and not every tactic will be
        present in every fraud incident. </p>
      <p>F3 is composed of seven tactics: </p>

      <table>
        <thead>
          <tr>
            <th>Tactic</th>
            <th>Tactic Description</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Reconnaissance</td>
            <td>
              <p>The adversary's actions to gather information they can use to plan future operations, including both
                cyber
                intrusions and attempted fraud.</p>
              <p>Reconnaissance consists of techniques that involve adversaries actively or passively gathering
                information
                that can be used to support targeting. Such information may include details of the victim organization,
                infrastructure, or staff/personnel. This information can be leveraged by the adversary to aid in other
                phases of the adversary lifecycle, such as using gathered information to plan and execute Initial
                Access,
                to
                scope and prioritize post-compromise objectives, or to drive and lead further Reconnaissance efforts.
              </p>
            </td>
          </tr>
          <tr>
            <td>Resource Development </td>
            <td>
              <p>The fraud actor's actions to establish resources they can use to support both cyber and fraud
                activities.
              </p>
              <p>Resource Development consists of techniques that involve fraud actors creating, purchasing, or
                compromising/stealing resources that can be used to support targeting. Such resources include
                infrastructure, accounts, or capabilities. These resources can be leveraged by the fraud actor to aid in
                other phases of the fraud lifecycle, such as using purchased domains to support Execution, email
                accounts
                for phishing as a part of Initial Access, or spoofing to help with Defense Evasion. </p>
            </td>
          </tr>
          <tr>
            <td>Initial Access</td>
            <td>
              <p>The fraud actor's actions to gain a foothold in a selected environment. </p>
              <p>Initial Access consists of techniques that use various entry vectors to gain their initial foothold
                within a selected environment. Techniques used to gain a foothold include targeted spearphishing and
                exploiting weaknesses in browsers. Footholds gained through initial access may allow for continued
                access,
                like compromise accounts and use of external remote services, or may be limited-use due to changing
                passwords.</p>
            </td>
          </tr>
          <tr>
            <td>Defense Evasion</td>
            <td>
              <p>The fraud actor's actions to avoid being detected. </p>
              <p>Defense Evasion consists of techniques that fraud actors use to avoid detection throughout their
                compromise. Techniques used for defense evasion include phone number spoofing or social engineering.
                Fraud
                actors also leverage and abuse trusted processes to hide and masquerade their activities. Other tactics’
                techniques are cross listed here when those techniques include the added benefit of subverting defenses.
              </p>
            </td>
          </tr>
          <tr>
            <td>Positioning</td>
            <td>
              <p>The fraud actor's actions in a selected environment, after initial access, to collect or manipulate
                data
                or otherwise prepare for execution. </p>
              <p>Positioning consists of techniques that involve fraud actors gathering sensitive information, altering
                account configurations, manipulating transaction parameters, or establishing conditions necessary for
                successful fraud operations. These preparatory activities enable fraud actors to maximize the value
                extracted during fraud execution or establish persistent access for future operations.</p>
            </td>
          </tr>
          <tr>
            <td>Execution</td>
            <td>
              <p>The fraud actor's actions to run malicious code or initiate fraudulent transactions that will convert
                stolen data to money. </p>
              <p>Execution consists of techniques that result in fraud actor-controlled code or actions running on a
                local, remote, or transaction-processing system. Techniques that run malicious code or automate actions
                are often paired with other tactics to achieve broader goals, such as exploring a network, manipulating
                applications, initiating unauthorized payments, or altering transaction data to support fraud. For
                example, a fraud actor might use a remote access tool to run a PowerShell script that performs Remote
                System Discovery and then launch scripts or bots that submit fraudulent transfers, modify payment
                instructions, or replay payment messages through compromised banking or merchant platforms.</p>
            </td>
          </tr>
          <tr>
            <td>Monetization</td>
            <td>
              <p>The fraud actor's actions to convert assets, often stolen, into usable funds or value in their
                possession. </p>
              <p>Fraud actors may convert fraudulently obtained funds or assets into a form they can utilize or transfer
                to their possession. Monetization consists of techniques that involve fraud actors liquidating stolen
                digital assets, transferring funds from compromised accounts, converting fraud proceeds into
                difficult-to-trace monetary instruments, or manipulating markets. These techniques represent the final
                stages of fraud operations where fraud actors secure their gains and attempt to obscure the transaction
                trail.</p>
            </td>
          </tr>
        </tbody>
      </table>

      <h3 id="techniques">Techniques and Sub-Techniques</h3>
      <p>Techniques represent “how” a fraud actor achieves a tactical goal by performing an action. There may be many
        ways, or techniques, to achieve tactical goals or objectives, resulting in multiple techniques in each tactic
        category. Likewise, there may be multiple ways to perform a technique, resulting in distinct sub-techniques
        under a technique. In addition, a single technique can be used to achieve multiple goals, meaning a technique
        can be listed under multiple tactics. </p>
      <p>Sub-techniques further break down behaviors described by techniques into more specific descriptions of how
        behavior is used to achieve an objective. The purpose behind sub-techniques is to provide more detail on how
        techniques can be used. Not all techniques have sub-techniques. There are several techniques that do not have a
        natural breakout into sub-techniques or do not make sense to generalize into higher level techniques. </p>

      <h3 id="versioning">Versioning</h3>
      <p>F3 uses a system for versioning objects (e.g., techniques, sub-techniques), the matrix view, and releases. The
        system is designed to inform users when parts of F3 have changed, give an indication as to the degree of the
        change, allow users to differentiate between versions of the matrix, and have stable references for content
        releases. </p>
      <p>Versions will only increment between content releases. That means that if two changes are made to a technique
        between scheduled updates, then the version will only increase once. </p>
      <h4>Objects</h4>
      <p>Objects in F3 refer to any item in the knowledge base that can have a relationship with another object. Each
        has their own criteria for how versions are incremented between releases. </p>
      <p>All objects are assigned a two-part numerical version MAJOR.MINOR that starts at 1.0 for any new object. </p>
      <h5>Techniques and Sub-Techniques</h5>
      <p>For techniques and sub-techniques, major version changes should happen infrequently. Major version changes
        consist of: </p>
      <ul>
        <li>Name changes: modifications to the word or set of words used to identify and distinguish the technique or
          sub-technique. </li>
        <li>Scope changes: modifications of how the technique could be interpreted or what it covers or does not cover
          in the description, or changes to associated tactics. </li>
      </ul>
      <p>Minor version changes to techniques and sub-techniques consist of: </p>
      <ul>
        <li>Descriptive information changes: modifications such as minor updates that do not change the scope, procedure
          examples, detections, mitigations, and references. </li>
      </ul>
      <h5>Tactics</h5>
      <p>Since tactics represent the tactical goals of a fraud actor, these remain relatively static over time because
        fraud actors' goals are unlikely to change. There may be cases where tactics need to be refined or created for
        better definition of what fraud actors are trying to accomplish by performing certain actions. </p>
      <h5>Matrix</h5>
      <p>Each matrix that appears on the F3 website is assigned a numerical MAJOR.MINOR as its version number. </p>
      <h5>Releases</h5>
      <p>A release occurs when the changes to the STIX representation of F3 are bundled and released along with any
        updates to the F3 website. Prior versions of the content and website will be saved and stored for historical
        reference. </p>

      <h2 id="methodology">The F3 Methodology</h2>
      <p>The previous sections of this document have described and defined the purpose and structure of the F3 knowledge
        base. This section describes the components of the methodology used in the creation of F3. It also describes the
        process recommended to determine if and when new tactics or techniques should be added to the knowledge base.
      </p>
      <p>
        The information within F3 will evolve over time, as will the considerations used for what information gets
        included and how it's structured. The process is as much of an art as it is a science. The focus remains on
        providing an accurate representation of how fraud actors conduct operations in a way that is easy to categorize
        the actions they take and to relate those actions in a way that defenders can use to describe, prevent, and
        detect and/or stop them. </p>

      <h3 id="conceptual">Conceptual</h3>
      <p>There are three conceptual ideas that are core to the philosophy behind F3: </p>
      <ul>
        <li>Maintain the fraud actor's perspective. </li>
        <li>Follow real-world use of fraud activity. </li>
        <li>Apply a usable level of abstraction. </li>
      </ul>

      <h4>Fraud Actor Perspective</h4>
      <p>F3 takes on the perspective of the fraud actor in its terminology and descriptions for tactics and techniques
        described in the model. Use of the fraud actor’s perspective makes it easier to understand actions and potential
        countermeasures in context than it would from a purely defense perspective. Defenders are then able to follow
        the fraud actor’s motivation for individual actions and understand how the actions and dependencies relate to
        specific classes of defenses that may be deployed in an environment. </p>
      <h4>Empirical Use</h4>
      <p>Empirical use refers to action based on direct observation, experience, or experiment rather than theory. F3 is
        based upon real-world cyber and fraud data sources, including the experience and broad knowledge of fraud
        analysts, fused into a common language of tactics and techniques specific to cyber fraud incidents. </p>
      <p>The activity described by F3 is drawn from fraud actor TTPs that have been used in cyber fraud incidents, which
        provides a grounding for the knowledge base so that it accurately portrays activity happening or likely to
        happen in the wild. The tie to incidents keeps the model grounded to real-world threats that are likely to be
        encountered rather than theoretical techniques that are unlikely to be seen due to difficulty of use or low
        utility. </p>

      <h5>Sources of Information</h5>
      <p>F3 also includes derivation from prior work. Fraud activities documented in other fraud models were analyzed
        through empirical use examples and fused: </p>
      <ul>
        <li>
          <a href="https://www.fsisac.com/knowledge/cyber-fraud-prevention-framework" target="blank"
            class="font-medium">FS-ISAC Cyber Fraud
            Prevention Framework </a>
          <ul>
            <li>Framework that enables gathering and sharing of cyber fraud information across the financial sector
              regarding fraud conducted on cyber channels</li>
          </ul>
        </li>

        <li><a href="https://nrf.com/research/retail-fraud-taxonomy" target="blank" class="font-medium">National Retail
            Federation Retail
            Fraud Taxonomy</a>
          <ul>
            <li>Framework for assessing and categorizing retail fraud threats and identifying appropriate actions to
              mitigate them </li>
          </ul>
        </li>
        <li><a href="https://www.group-ib.com/products/cyber-fraud-intelligence-platform/" target="blank"
            class="font-medium">Group-IB Cyber
            Fraud Intelligence</a>
          <ul>
            <li>Framework to systematically break down fraud actor actions and behaviors across an incident into stages
              and techniques </li>
          </ul>
        </li>

        <li><a href="https://github.com/stripe/ft3" target="blank" class="font-medium">Stripe Fraud Tools Tactics and
            Techniques (FT3)</a>
          <ul>
            <li>Framework to enhance understanding of the tactics, techniques, and procedures (TTPs) used by actors in
              fraudulent activities </li>
          </ul>
        </li>
      </ul>

      <h4>Abstraction</h4>
      <p>The level of abstraction for fraud actor tactics and techniques within F3 is modeled in a way to be appropriate
        to bridge offensive action with defensive countermeasures. The tactics and techniques in F3 are behavior-based
        and provided in the context of individual actions fraud actors make and which actions can be used to achieve a
        goal. Defining the actions used in fraud incidents in this way provides a common taxonomy of individual actions
        and goals that can be understood by both offensive and defensive teams for more effective fraud prevention. </p>

      <h3 id="methodology-tactics">Tactics</h3>
      <p>Tactics represent the tactical goals of a fraud actor. The tactics in F3 will remain relatively static over
        time since what the fraud actors are trying to accomplish is unlikely to change. There may be cases where
        tactics need to be refined for better definition of the actions occurring. New tactics will follow the need to
        define existing, but uncategorized, or new fraud goals as a way to provide accurate context for what a fraud
        actor is accomplishing by performing a technique action. </p>

      <h4>Naming and Identifier Conventions </h4>
      <p>Tactics are assigned identifiers or IDs, names, and descriptions to describe their specific information.
        Additional entities, such as references, may be added in future versions of F3. </p>

      <h5>Identifiers (IDs) </h5>
      <p>F3 tactics are of the format FA#### and are unique within the knowledgebase; or, if a tactic already exists in
        the ATT&CK knowledgebase, the ATT&CK identifier is used (i.e., TA####). The identifiers are assigned to ensure
        machine readability and compatibility with related MITRE and other frameworks and tools, such as ATT&CK and
        STIX. </p>
      <h5>Names</h5>
      <p>Tactic naming conventions focus on the “why” or the tactical objective of the fraud actors that make it unique.
        The names are meant to be useful contextual categories for human readability and reference. </p>
      <h5>Descriptions</h5>
      <p>Tactic descriptions provide a definition describing the category and serve as a guide for what techniques
        should be within the tactic. This includes the fraud actors tactical objective or reason for performing an
        action. </p>
      <h3 id="methodology-techniques">Techniques and Sub-techniques </h3>
      <p>Techniques and sub-techniques are the foundation of F3 and represent the individual actions fraud actors take.
        The Design Principles are applied in the decision process to create a technique or sub-technique and contribute
        to their respective details within the knowledge base.
      </p>
      <p>Technique names focus on the aspect of the technique that makes it unique: what the adversary achieves at an
        intermediate level of abstraction from using the tactic. Sub-techniques often signify how a technique is used at
        a lower level of abstraction. Industry-accepted terminology tends to be used if a technique or sub-technique is
        already established and documented (e.g., in ATT&CK).
      </p>
      <p>When a potential new behavior is identified, it may be included in F3 by:</p>
      <ul>
        <li>Adding an entirely new technique,
        </li>
        <li>Adding a new sub-technique under an existing technique, or
        </li>
        <li>Enhancing or abstracting an existing technique or sub-technique
        </li>
      </ul>
      <p>The decision will require consideration of whether the newly identified or previously uncategorized behavior is
        similar to other techniques and how, if it naturally fits under a similar technique as a sub-technique, and if
        the new behavior would conceptually be treated differently by F3 users (e.g., incident description, defensive
        measures). If a new behavior is not conceptually different in how it is implemented or defended against, then it
        likely should be included in an existing technique or sub-technique. </p>
      <h4>Naming and Identifier Conventions</h4>
      <p>Techniques and sub-techniques are assigned identifiers or IDs, names, and descriptions to describe their
        specific information. Additional entities, such as references, may be added in future versions of F3. </p>
      <h5>Identifiers (IDs) </h5>
      <p>F3 technique and sub-technique identifiers are of the format F#### for techniques and F####.#### for
        sub-techniques and are unique within the knowledgebase; or, if a technique or sub-technique already exists in
        the ATT&CK knowledgebase, the ATT&CK identifier is used (i.e., T####, T####.###). The identifiers are assigned
        to ensure machine readability and compatibility with related MITRE and other frameworks and tools, such as
        ATT&CK and STIX. </p>
      <h5>Names</h5>
      <p>Technique naming conventions focus on the actions fraud actors take that make it unique to achieve their
        tactical goals. Sub-technique names typically signify how a technique is used at a lower level of abstraction.
        The names are meant to serve as useful contextual designations for human readability and reference. </p>
      <h5>Descriptions</h5>
      <p>Technique and sub-technique descriptions provide explanatory information about the technique or sub-technique.
        This includes what the action is and what fraud actors typically use it for. Descriptions may also indicate how
        a fraud actor can take advantage of it or variations on how it could be used. </p>

      <h2 id="usage">Usage</h2>
      <p>Collaboration and shared understanding across teams is highly important to effectively combat financial fraud.
        Responsibility for detecting, investigating, and responding to financial fraud may be spread across multiple
        groups within an organization, and each may have its own tools, processes, and terminology. F3 is designed to
        bridge these gaps by giving all stakeholders a common language for describing fraud incidents, behaviors, and
        countermeasures. Through this shared model, teams can coordinate more effectively and align their efforts.
      </p>
      <p>The following scenario demonstrates how F3 enables teams to work together: </p>
      <ul>
        <li>Fraud analysts produce F3-based fraud incident reports and share actionable fraud intelligence.
        </li>
        <li>Offensive security operations teams identify and validate detections for F3 techniques.
        </li>
        <li>Defensive detection engineers implement countermeasures for techniques observed in fraud incidents.
        </li>
        <li>Security officers report suspected fraudulent activity using the F3 model.
        </li>
      </ul>
      <p>Fraud team use of F3 goes beyond identification of the fraud actor’s actions taken during the cyber fraud
        incident. In response, the fraud team may also recommend a combination of organizational efforts, such as: </p>
      <ul>
        <li>New fraud-related rules, such as temporarily lowering transaction limits or introducing additional
          verification for higher transfers. </li>
        <li>A customer notification campaign, which may include warnings about social engineering attempts or
          instructing customers on password security. </li>
        <li>Targeted training is provided to the workforce including contact center agents and branch staff to recognize
          fraud indicators and escalate suspected cases of account takeover. </li>
        <li>Adjusted dispute handling workflows to rapidly work with impacted customers while preserving evidence needed
          for investigation. </li>
      </ul>
      <p>This shared foundation strengthens coordination across teams and helps institutions to work cohesively to
        maintain a secure financial environment. Users of F3 will encompass many roles and responsibilities associated
        with organizational cyber defense, fraud prevention and detection, and incident response. These include: </p>
      <ul>
        <li>Fraud Incidents: Create detailed incident reports using F3 to describe fraud actor goals, behaviors, and
          impacts.
        </li>
        <li>Fraud Intelligence: Use the F3 common language to structure, compare, and analyze reported fraud
          intelligence.
        </li>
        <li>Defensive Measures: Apply recommendations for aligning operational defensive measures to protect from
          threats contained in F3 and mitigate financial fraud.
        </li>
        <li>Information Sharing: Share intelligence on threats and fraud techniques with other institutions as described
          with F3 to strengthen industry-wide defense.
        </li>
      </ul>
      <h2 id="summary">Summary</h2>
      <p>This page provides the motivation behind the creation of F3, its design philosophy, the components contained
        within the knowledge base, and how it can be used. It is meant to be used as an authoritative source of
        information about F3, as well as to help guide how the framework is expanded and maintained. By defining what
        the framework contains and how it should be maintained, the document helps ensure consistency, clarity, and
        alignment as the framework evolves over time. </p>
      <p>F3 is grounded in real-world fraud actor behavior and developed by fraud fusion analysts. Existing fraud
        frameworks were used as foundational inputs, and the methodology and principles used by ATT&CK were used as a
        model to derive this knowledge base of real-world fraud actor behavior. This combination of real threat data and
        a proven analytical approach gives users greater transparency into how the framework was constructed, increases
        confidence in the information it provides, and demonstrates how it can be applied by the fraud-fusion community.
      </p>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import BreadcrumbComponent from "../components/BreadcrumbComponent.vue";
import matrixImage from "@/assets/matrix-img.png";
import expandedImage from "@/assets/expanded-techniques.png";

export default defineComponent({
  components: { BreadcrumbComponent },
  data() {
    const baseUrl = import.meta.env.BASE_URL
    return {
      downloadUrl: `${baseUrl}MITRE F3 Design Principles and Methodology.pdf`,
      matrixImage,
      expandedImage,
      breadcrumbItems: [
        { label: "About", route: "/about" },
        { label: "Design Principles", route: "/about/methodology" },
      ],
      topLevelHeadings: [
        {
          label: "Introduction",
          id: "introduction"
        }, {
          label: "Background",
          id: "background"
        }, {
          label: "The F3 Model",
          id: "the-f3-model",
          subheadings: [
            {
              label: "Design Principles",
              id: "design-principles"
            }, {
              label: "The F3 Matrix",
              id: "matrix"
            }, {
              label: "Tactics",
              id: "tactics"
            }, {
              label: "Techniques and Sub-Techniques",
              id: "techniques"
            }, {
              label: "Versioning",
              id: "versioning"
            },
          ]
        }, {
          label: "The F3 Methodology",
          id: "methodology",
          subheadings: [{
            label: "Conceptual",
            id: "conceptual"
          }, {
            label: "Tactics",
            id: "methodology-tactics"
          }, {
            label: "Techniques and Sub-techniques",
            id: "methodology-techniques"
          },
          ]
        }, {
          label: "Usage",
          id: "usage"
        }, {
          label: "Summary",
          id: "summary"
        },
      ]
    }
  },
  methods: {
    scrollToHeading(id: string) {
      console.log("scroll to ", id)
      const element = document.getElementById(id);
      if (element) {
        const headerOffset = 100; // Adjust this based on your fixed header height
        const elementPosition = element.getBoundingClientRect().top + window.scrollY;
        const offsetPosition = elementPosition - headerOffset;

        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth', // Smooth scrolling behavior
        });
      }
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

.subheading {
  @apply -mt-2 mb-3 italic normal-case text-lg
}

.main h1 {
  @apply font-medium
}

.main h2 {
  @apply text-3xl font-medium
}

.main h3 {
  @apply text-2xl font-medium
}

.main h4 {
  @apply text-xl font-medium mt-2
}

.main h5 {
  @apply text-lg font-medium
}

.subtitle {
  @apply font-medium italic
}

table {
  @apply mb-8
}

td, th, tr {
  @apply border-ctid-light-gray border-[1px]
}

td {
  @apply px-2
}

ul {
  @apply ml-4
}

figcaption {
  @apply text-center italic mt-2 mb-6
}
</style>
