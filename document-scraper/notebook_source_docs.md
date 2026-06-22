# Optilogic ドキュメント - 全コンテンツ
# CosmicFrog / DataStar / Ada / Composable Apps 操作ガイド



---
## Connecting to External Data
**URL:** https://optilogic.com/resources/help-center/connecting-to-external-data

Fast, AI-driven supply chain decision orchestration for every individual and team —from strategic design to tactical planning.
Model, optimize, and simulate even the most complex supply chains at scale and trade off cost, service, risk, and sustainability.
Eliminate data challenges with AI-automated cleansing and workflow orchestration for decision-ready intelligence instantly.
Optilogic's breakthrough agentic AI system for supply chain design — compresses months of supply chain design work into a single day.
Purpose-built apps for every stakeholder — Deploy across your entire organization today. Act on insights from day one.
Stay updated on the latest from Optilogic.
Enhance your skills with our hands-on training sessions and courses.
Dive into expert insights, industry trends, and practical tips for success.
Discover Optilogic's partner network empowering transformation and supply chain success.
Discover on-demand interviews, demos, and customer sessions.
Find step-by-step guides, FAQs, and support.
Access our full library of guides, case studies, and tools to help you succeed.
Connect with Optilogic peers, exchange insights, and accelerate supply chain success.


---
## Adding Custom Columns In Cosmic Frog
**URL:** https://optilogic.com/resources/help-center/docs/adding-custom-columns-in-cosmic-frog

Custom Columns can be added to any input table directly through Cosmic Frog. To add a custom column to a table, open the table and then select Grid > Create Custom Column
This will open a window on the right-hand side of the screen where you can configure your custom column. Each of the required entries are used as follows:
This will be the name of the custom column. Please note that column names will only be allowed to contain alphanumeric characters and underscores. Spaces are not allowed in column names, and you will not be able to create a column name that begins with a number. If you enter any sort of an invalid column name, you will not be able to save the column and a message will be displayed noting the issues with the name currently entered.
Pseudo typing allows for the data entered into this column to accept all sorts of input formatting without strictly adhering to the Data Type selected for the custom column. For example, if the Data Type for a given custom column is set to numeric and you attempt to import a string into the field, Pseudo Typed = TRUE will allow for this import to succeed. If Pseudo Typed = FALSE, then this import would fail as the field would only accept numbers. This also applies for editing the field within the grid directly.
For reference, all fields within the standard Anura schema are pseudo typed. We will allow for all entries into the data fields and then cast the entries to their appropriate data type for use within maps, dashboards and the application of scenario items.
Select one of the available data types that the data in your custom column will be formatted in. Depending on the selection chosen for the Pseudo Typed setting, this data type will be strictly enforced (Pseudo Typed = FALSE) or be relaxed and only used when generating visuals or applying scenario items (Pseudo Typed = TRUE).
This setting informs Cosmic Frog if the custom column should be used as a primary key for the table when evaluating file imports. If True, the custom column will be included in addition to the table’s default primary key columns.
When data is imported into a Cosmic Frog model through the Import File action, data is loaded using Upsert logic. This means that rows which already exist in a table will be updated, and rows which do not exist will be inserted. Existing rows will be identified using the table’s primary key – all input tables have a preconfigured set of columns that represent the primary key of the input table. For information on which columns represent the primary key of any given table, please reference Downloadable Anura Data Structure – Inputs | Optilogic.
Once all of the settings have been filled out, click Save and your table will refresh with the custom column now being displayed on the far-right of the table. You’ll notice that the column name has been down cased – this is done to align with standard naming convention for PSQL.
If any issues arise during the Custom Column creation, please reach out to sup
…（省略）


---
## Adding Demand (Simulation)
**URL:** https://optilogic.com/resources/help-center/docs/adding-demand-simulation

Simulations are generally (mostly) driven by demand specified as customer orders. These orders can be entered in the Customer Orders and/or the Customer Order Profiles input tables. The Customer Orders table typically contains historical transactional demand records to simulate a historical baseline. The Customer Order Profiles table on the other hand contains descriptions of customer order behaviors from which the simulation engine (Throg) generates orders that follow these profiles.
In this documentation we cover both these input table, the Customer Orders table and the Customer Order Profiles table.
To achieve the level of granularity needed and the time-based events to mimic reality as best as possible, every customer order to be simulated is explicitly defined in the customer orders table; this includes line items, order and due dates, and order quantities:
Users can utilize the following additional fields available on the Customer Orders table if required. The single sourcing, allow partial fill, and allow backorder settings behave the same as those that can be set on the Customers table (see this help article), except these here apply to individual orders/individual line items rather than to all orders at the customer over the whole simulation horizon. Note that if these are set here on the Customer Orders table, these values take precedence over any values set for the particular customer in the Customers table:
Rather than specifying individual orders and line items, the Customer Order Profiles table generates these individual orders from profiles which can for example disaggregate monthly demand forecasts into assumed or inferred profiles, using variability to randomize characteristics like quantities and time between orders.
Note that by using start and end dates for profiles, users can control the portion of the simulation horizon in which a profile is used. This enables users to for example capture seasonal demand behaviors by defining a profile for Customer A/Product X in winter, and another profile for the same customer-product combination in summer.
Two scenarios were run, 1 named “CZ_CO P4 profile a” where customer order profile a to generate orders at CZ_CO for Product_4 is included and 1 named “CZ_CO P4 profile b” where customer order profile b to generate orders at CZ_CO for Product_4 is included. These are the profiles shown in the 2 screenshots above. In the Simulation Order Report output table one can see the individual orders generated by these profiles during the simulation runs of these 2 scenarios:
Simulations are generally (mostly) driven by demand specified as customer orders. These orders can be entered in the Customer Orders and/or the Customer Order Profiles input tables. The Customer Orders table typically contains historical transactional demand records to simulate a historical baseline. The Customer Order Profiles table on the other hand contains descriptions of customer order behaviors from which the simulation 
…（省略）


---
## Adding Inventory Policies (Simulation)
**URL:** https://optilogic.com/resources/help-center/docs/adding-inventory-policies-simulation

Inventory policies describe how inventory is managed across facilities in our supply chain. These policies can include how and when to replenish, how stock is picked out of inventory, and many other important rules.
In general, we add inventory policies using the Inventory Policies table in Cosmic Frog.
In this documentation we will cover the types of inventory simulation policies available and also other settings contained in the Inventory Policies table.
An (R,Q) policy is a commonly used inventory management approach. Here, when inventory drops below a value of R units, the policy is to order Q units. In Cosmic Frog, when an (R,Q) policy is selected, we can define R and Q in “SimulationPolicyValue1” and “SimulationPolicyValue2”, respectively. We can define the unit of measure (e.g. pallets, volume, individual units, etc.) for both parameters in their corresponding simulation policy value UOM column.
In the following example, MFG_STL has an (R,Q) inventory policy of (100,1900) for Product_2, measured in terms of individual units (i.e. “each”).
(s,S) policies are like (R,Q) policies in that they define a reorder point and how much to reorder. In an(s,S) policy, when inventory is below s units, the policy is to “order up to” S units. In other words, if x is the current inventory level, and x < s, the policy is to order (S-x) units of inventory.
In the example below, DC_VA has an (s,S) inventory policy of (150,750) for Product_1. If inventory dips below 150, the policy is to order so that inventory would replenish to 750 units.
(s,S) policies may also be referred to as (Min,Max) policies; both policy names are accepted in the Anura schema and both behave as described above.
A (T,S) inventory policy is like an (s,S) inventory policy in that whenever inventory is replenished, it is replenished up to level S. Under an (s,S) inventory policy, we check the inventory level in each period when making reorder decisions. In contrast, under a (T,S) inventory policy, the current inventory level is only checked every T periods. During one of these checks, if the inventory level is below S, then inventory is replenished up to level S.
In the example below, DC_VA manages Product_1 using a (T,S) inventory policy. The DC checks the inventory level every 5 days. If inventory is below 750 units during any of these checks, inventory is replenished up to 750 units.
As the name suggests a Do Nothing inventory policy does not trigger any replenishment orders. This policy can for example be used for products that are being phased out or at manufacturing locations where production occurs based on a schedule.
In the example below, MFG_STL uses the Do Nothing inventory policy for the 3 products it manufactures.
On the inventory policies table, other fields available to the user to model inventory include those to set initial inventory, how often inventory is reviewed, and the inventory carrying cost percentage:
When Only Source From Surplus is set to True on a customer ful
…（省略）


---
## Adding Model Constraints
**URL:** https://optilogic.com/resources/help-center/docs/adding-model-constraints

Model constraints allow us to capture real-world limitations in our supply chain. These limitations might include production capacity, transportation restrictions, storage limits, etc. 
By default, Cosmic Frog allows us to incorporate the following constraint types for Neo optimization models:
Each set of constraints has its own table in the Cosmic Frog data schema.
Flow Constraints introduce a limit on the amount of flow (product) that can pass between an origin/destination pair in our supply chain.
In the example below, we limit the number of pencils that the Ashland production site can ship to the Chicago customer to a maximum of 20 per period.
Note that we can adjust the unit of measure of our constraints as needed. For example, we might be interested in limiting the total weight of product shipped between locations, instead of the total count of product.
Inventory constraints limit the amount of product that can be stored at a facility. They can represent both minimum and maximum inventory limits.
In the example below we limit the capacity of the Bakersfield distribution center such that it can hold at most 500 pens. We are also requiring that the DC stores at least 100 pencils.
Production constraints limit the amount of product a supplier or a production facility can produce. Like inventory constraints, you can set both minimum and maximum production limits.
In the example below, the Memphis production can produce at most 250 pens in each period. Additionally, the Ashland site has a fixed production constraint, which requires it to always produce exactly 400 pencils in each period.
Facility count constraints limit the number of facilities that can be used in a Cosmic Frog model. These constraints are often used in facility location and selection problems.
For many of the “count” constraints, we want to apply our constraint across a number of different supply chain elements (e.g. across all facilities). To do this, the group functionality of Cosmic Frog is particularly useful, and often necessary. For more detailed information on using groups in constraints, see Using Groups to Write Model Constraints.
In the following example we want to design a supply chain with exactly 2 facilities, and we want to know the optimal location of these 2 facilities. First, we set the status of candidate locations in our Facilities table to “consider”. Without making this change, our model will be forced to include all facilities where Status = “Include” in our network.
Then, we create a constraint requiring the model to select exactly 2 facilities from the “ProductionSites” group.
Flow count constraints limit the number of flows of a particular product. Flow count constraints are particularly useful in problems where the available transportation resources are limited.
In the following example we are implementing a “single-sourced” rule where each customer is served by exactly one production site. For each customer (enumeration) we look across all production s
…（省略）


---
## Adding Sourcing Policies via the Sourcing Tables (Simulation)
**URL:** https://optilogic.com/resources/help-center/docs/adding-sourcing-policies-via-the-sourcing-tables-simulation

In a supply chain model, sourcing policies describe how network components create and order necessary materials. In Cosmic Frog, sourcing rules & policies appear in two different table categories:
In this section, we will discuss how to use these Sourcing policy tables to incorporate real-world behavior. In the sourcing policy tables we define 4 different types of sourcing relationships:
First we will discuss the options user has for the simulation policy logic used in these 4 tables and the last section covers the other simulation specific fields that can be found on these sourcing policies tables.
Customer fulfillment policies describe which supply chain elements fulfill customer demand. For a Throg (Simulation) run, there are 3 different policy types that we can select in the “Simulation Policy” column:
If “By Preference” is selected, we can provide a ranking describing which sites we want to serve customers for different products. We can describe our preference using the “Simulation Policy Value” column.
In the following example we are describing how to serve customer CZ_CA’s demand. For Product_1, we prefer that demand is fulfilled by DC_AZ. If that is not possible, then we prefer DC_IL to fulfill demand. We can provide rankings for each customer and product combination.
Under this policy, the model will source material from the highest ranked site that can completely fill an order. If no sites can completely fill an order, and if partial fulfillment is allowed, the model will partially fill orders from multiple sources in order of their preference.
If “Single Source” is selected, the customer must receive the given product from 1 specific source, 1 of the 3 DCs in this example.
The “Allocation” policy is similar to the “By Preference” policy, in that it sources from sites in order of a preference ranking. The “Allocation” policy, however, does not look to see whether any sites can completely fill an order before doing partial fulfillment. Instead, it will source as much as possible from source 1, followed by source 2, etc. Note that the “Allocation” and “By Preference” policies will only be distinct if partial fulfillment is allowed for the customer/product combination.
Consider the following example, customer CZ_MA can source the 3 products it puts orders in for from 3 DCs using the By Preference simulation policy. For each product the order of preference is set the same: DC_VA is the top choice, then DC_IL, and DC_AZ is the third (last) choice. Also note that in the Customers table, CZ_MA has been configured so that it is allowed to partially fill orders and line items for this customer.
The first order of the simulation is one that CZ_MA places (screenshot from the Customer Orders table), it orders 20 units of Product_1, 600 units of Product_2, and 160 units of Product_3:
The inventory at the DCs for the products at the time this orders comes in is the same as the initial inventory as this customer order is the first event of the simulat
…（省略）


---
## Adding Sourcing Rules via the Model Element Tables (Simulation)
**URL:** https://optilogic.com/resources/help-center/docs/adding-sourcing-rules-via-the-model-element-tables-simulation

In a supply chain model, sourcing policies describe how network components create and order necessary materials. In Cosmic Frog, sourcing policies and rules appear in two different table categories:
In this section, we describe how to use the model elements tables to define sourcing rules for customers and facilities. Specifically, we can decide if each element is single sourced, allows backorders, and/or allows partial fulfillment.
Single source policies can be defined on either the order level or the line-item level. Setting “Single Source Orders” to “True” for a location means that for each order placed by that location, every item in that order must come from a single source. Setting this value to “False” does not prohibit single sourcing, it just removes the requirement.
Setting “Single Source Line Items” to “True” only requires each individual line-item come from a single source. In other words, even if this is “True”, an individual order can have multiple sources, as long as each line item is single sourced.
If “Single Source Orders” is set to “True” and “Single Source Line Items” is set to “False”, the “Single Source Orders” value takes precedence.
In case an order cannot be fulfilled by the due date (as set on the Customer Orders table in the case of Customers), it is possible to allow backorders where the order will still be filled, but it will be late, by setting the “Allow Backorders” value to “True”. A time limit can be set on this by using the “Backorder Time Limit” field and its UOM field, set to 7 days in the below screenshot. This means that the orders are allowed to be backordered, but if after 7 days the order still is not filled, it is cancelled. Leaving Backorder Time Limit blank means there is no time limit, and the order can be filled late indefinitely.
We can also decide to allow partial fulfillment of orders or individual line-items. If “Allow Partial Fill Orders” is set to “False”, orders need to be filled in full. If set to “True”, then only filling part of an order on time (by the due date) is allowed. What happens with the unfulfilled part of the order depends on if backorders are allowed. If so (“Allow Backorders” = “True”), then the remaining quantity of a partially filled order can be satisfied in the future with additional shipments. If a time limit on backorders is set and is reached on a partially filled order, the remaining quantity will be cancelled. “Partial Fill Orders” and “Partial Fill Line Items” behave similarly to the single sourcing policies, where it is possible to for example allow partially filling orders, but not partially filling line items. If “Partial Fill Orders” is set to “True”, then “Partial Fill Line Items” will also be forced to “True”.
In a supply chain model, sourcing policies describe how network components create and order necessary materials. In Cosmic Frog, sourcing policies and rules appear in two different table categories:
In this section, we describe how to use the model elements
…（省略）


---
## Adding Transportation Modes (Simulation)
**URL:** https://optilogic.com/resources/help-center/docs/adding-transportation-modes-simulation

The Transportation Modes table is an often used optional input table to run a simulation. Mode attributes like fill levels and capacities are specified in this table to control the size of shipments, which will be explained first in this documentation. Rules of precedence when using multiple fill level / capacity fields and when using On Volume / Weight / Quantity transportation simulation policies will be covered also.
The same capacity and fill level fields as for Volume are also available in this table for Quantity and Weight (not shown in the screenshot above).
When utilizing more than 1 of the Fill Level fields, the one that is reached first is applied. For example, if a shipment’s weight has reached the weight fill level, but its volume has not yet reached the volume fill level, the shipment is allowed to be dispatched.
Similarly, if more than 1 Capacity field has been populated, the one that is reached first is applied. For example, if a shipment’s volume has reached the volume capacity but not yet the weight capacity, it cannot be filled up further and will be dispatched.
As mentioned above, when transportation simulation policies of On Quantity / Weight / Volume are being used, the fill levels and capacities of these Modes are specified in the simulation policy value field on the Transportation Policies table. If also using the Transportation Modes table to set any fill level and/or capacity for these modes, user needs to take note of the effects this may have:
The Transportation Modes table is an often used optional input table to run a simulation. Mode attributes like fill levels and capacities are specified in this table to control the size of shipments, which will be explained first in this documentation. Rules of precedence when using multiple fill level / capacity fields and when using On Volume / Weight / Quantity transportation simulation policies will be covered also.
The same capacity and fill level fields as for Volume are also available in this table for Quantity and Weight (not shown in the screenshot above).
When utilizing more than 1 of the Fill Level fields, the one that is reached first is applied. For example, if a shipment’s weight has reached the weight fill level, but its volume has not yet reached the volume fill level, the shipment is allowed to be dispatched.
Similarly, if more than 1 Capacity field has been populated, the one that is reached first is applied. For example, if a shipment’s volume has reached the volume capacity but not yet the weight capacity, it cannot be filled up further and will be dispatched.
As mentioned above, when transportation simulation policies of On Quantity / Weight / Volume are being used, the fill levels and capacities of these Modes are specified in the simulation policy value field on the Transportation Policies table. If also using the Transportation Modes table to set any fill level and/or capacity for these modes, user needs to take note of the effects this may have:


---
## Adding Transportation Policies (Simulation)
**URL:** https://optilogic.com/resources/help-center/docs/adding-transportation-policies-simulation

Transportation policies describe how material flows throughout a supply chain. In Cosmic Frog, we can define our transportation policies using the Transportation Policies (required) and Transportation Modes (optional) tables. The Transportation Policies table will be covered in this documentation. In general, we can have a unique transportation policy for each combination of origin, destination, product, and transport mode.
Typically in simulation models, transportation policies are defined over the group of all products (which can be done by leaving Product Name blank as is done in the screenshot above), unless some products need to be prevented from being combined into shipments together on the same mode. If Transportation Policies list products explicitly, these products will not be combined in shipments.
Here, we will first cover the available transportation policies; other transportation characteristics that can be specified in the Transportation Policies table will be discussed in the sections after.
Currently supported transportation simulation policies are:
Selecting “On Volume”, “On Weight”, or “On Quantity” as a simulation policy means that either the volume, weight, or quantity of the shipment will determine which transportation mode is selected. In this case, the “Simulation Policy Value” defines the lowest volume that will go by that mode. We can use multiple lines to define multiple breakpoints for this policy.
Please note that:
If “By Preference” is selected, we can provide a ranking describing which transportation mode we want to use for different origin-destination-product combinations. We can describe our preference using the “Simulation Policy Value” column.
This screenshot shows that all MFG to DC transportation lanes only have 1 Mode of Container and the Simulation Policy is set to By Preference for all of them. If there are multiple Modes available, the By Preference policy will select them pending availability in the order of preference specified by the Simulation Policy Value field, the lowest value being the most preferred mode. If there were 2 modes available and the policy set to By Preference, where 1 mode has a simulation policy value of 1 and the other of 2, the Mode with simulation policy value = 1 will be used if available, if it is not available, the mode with simulation policy value = 2 will be used.
In the following example, the “Container” mode is preferred over the “Truck” mode for the MFG_CA to DC_IL route. Note that since the “Product Name” column is left blank, this policy applies to all products using this route.
Selecting “By Due Date” is like “By Preference” in that different modes can be ranked via the “Simulation Policy Value”. However, selecting “By Due Date” adds the additional component of demand timing into its selection. This policy selects the highest preference option that can meet the due date of the shipment. The following screenshot shows that the By Due Date simulation policy is used on cert
…（省略）


---
## Advanced Data Enrichment and Transformation using the Run Python Task
**URL:** https://optilogic.com/resources/help-center/docs/advanced-data-enrichment-and-transformation-using-the-run-python-task

The Run Python task allows you to execute Python scripts within a DataStar macro. You select a script, define its inputs (arguments), and run it as part of your workflow. This is ideal when built-in tasks are insufficient or when you want to reuse existing Python logic.
The Run Python task is especially useful when:
This walkthrough uses the end state of the DataStar Quick Start: Creating a Task using Natural Language guide as a starting point. At that point, a raw_shipments table has been imported and a Run SQL task has produced a customers table with unique customers. We will use a Run Python task to transform customer names from the format CZ1, CZ10, CZ100 to Cust_0001, Cust_0010, Cust_0100 - ensuring alphabetical sort matches customer number order and aligning the prefix with other data sources. The transformation steps are:
The screenshot below shows the "Change customer names" Run Python task added to the macro:
Once a Python task is added to the macro canvas, its configuration tab opens on the right:
After clicking Use File with update_customer_names.py selected, the configuration updates as follows:
Before configuring arguments, we will cover the update_customer_names.py script. We can review its arguments so we can verify auto-detection is correct and look at the script body to understand what it does. You can copy the full script text from the Appendix.
With the script understood, let us use Detect arguments and configure the task:
The Notes section is the final configuration area. It is especially valuable for complex tasks or collaborative projects, enabling users to quickly understand what the task does. Formatting options are available above the text box:
Before running the task, we examine the customers table in the sandbox:
Now run the "Change customer names" task (hover over it on the macro canvas and click the play button) and examine the results:
The Run Manager logs are useful for monitoring progress and troubleshooting:
Instead of using an existing file, users can click the Create File button in the Code File area (see bullet 10 underneath the first screenshot of the Code File section) to create a new script directly on the Optilogic platform:
Templates are pre-built scripts available to all users from the Resource Library, covering common import/export patterns. To browse them, open the Resource Library application, filter for DataStar resources (button at the right top) and the Script tag. Clicking a resource also shows available documentation, which can be copied to your Optilogic account or downloaded.
The Python base image used by the Run Python task contains the Python libraries most used in conjunction with DataStar. If your script uses a library that is not included in this base image, you need to create a requirements.txt file and place it in the same location as your Python script. In this file, you need to list the names of the libraries (without quotes), 1 library name per line.
If your script uses a library that 
…（省略）


---
## AI Agents and Utilities - Overview
**URL:** https://optilogic.com/resources/help-center/docs/ai-agents-and-utilities---overview

Exciting tools that drastically shorten the time spent wrangling data, building supply chain models for Cosmic Frog, and analyzing outputs of these models are now available on the Optilogic platform.
Collectively, the Optilogic agentic AI tools are called Ada. This is after Ada Lovelace, widely regarded as the world’s first computer programmer and one of the earliest visionaries to recognize the potential of computational systems beyond pure calculation.
This documentation briefly explains how to access these AI Agents and Utilities, lists the available tools with a short description of each, and provides links to detailed documentation for several of these tools.
Before we dive into how to access the AI Agents & Utilities, here are a few links you may find helpful:
Four of the available agents can be accessed by chatting with Ada and all of them can be accessed by using Run AI Agent tasks in DataStar.
When chatting with Ada on the next generation Optilogic platform, users can select the agent they want to use for their prompt:
Please note that:
Please refer to the detailed documentation on the individual agents and the getting started with Ada & Agentic AI article to learn more about using these when chatting with Ada.
At a high level, the steps in DatsStar are as follows (screenshots follow beneath):
Your macro canvas will look similar to the following screenshot after step #4:
After adding a task, its configuration tab is automatically shown on the right-hand side. Give the task a name, and then select the Agent you want to use from the list of available Agents in the Select Utility section. You can also use the Search box to quickly find any Agent that contains certain text in its name or description. Hover over the description of an Agent to see the full description in case it is not entirely visible:
Once an Agent has been selected by clicking on it, the Configure Utility section becomes available. The inputs here will differ based on the Agent/Utility that has been selected. In the next screenshot the Configure Utility section of the Modeler Agent is shown:
Provide the inputs for at least the required parameters, and if desired for any optional ones. Note that hovering over a blue question mark icon will bring up a hover box with a description of the parameter.
Using Utilities works in the same way as using AI Agents, just through the Run Utility task instead of the Run AI Agent task. The following 3 screenshots show 1) a Run Utility task added to a Macro, 2) its Select Utility section, and 3) the Configure Utility section of the Duplicate Macro utility:
Resource Size for both Run AI Agent and Run Utility tasks can be set in the Run Configuration section, which is indicated as optional. However, for most agents and utilities, the default 3XS Resource Size is not sufficient. It is recommended to update this to XS:
The folloing AI Agents and Utilities are currently available. More are being added as they come available. For each a short desc
…（省略）


---
## AI Agents: Architecture and Components
**URL:** https://optilogic.com/resources/help-center/docs/ai-agents-architecture-and-components

Ada, Optilogic's Agentic AI, is a suite of specialized AI agents designed to help supply chain teams work faster and with greater confidence across the full modeling lifecycle. Each agent is tailored to a specific part of the supply chain workflow.
In this documentation we will cover what AI agents and their components are.
AI agents are software systems that use a large language model (LLM) as a reasoning engine but go beyond chat by taking actions in an environment. Instead of only generating text, an agent can interpret a goal, decide what to do next, call external capabilities (tools), observe the results, and iterate until the objective is achieved.
In practice, an "agent" is not a single model call - it is a control system wrapped around an LLM:
This architecture matters because it turns the LLM from a passive text generator into an adaptive problem-solver that can:
An agent is not just a chat model. A chat model produces responses; an agent operates - it can run commands, fetch data, write artifacts, and iterate autonomously within defined constraints. Think of an AI agent as a smart assistant that can:
Agents are most useful when tasks are multi-step, partially specified, and feedback-driven, for example:
If a task is single-shot and fully specified (e.g., "summarize this paragraph"), a non-agent LLM call is often simpler and cheaper.
Most agents follow a ReAct-style loop (Reason + Act), sometimes with explicit planning:
A useful way to think about the loop is that each iteration should:
Well-behaved agents stop for explicit reasons, such as:
An agent is the intelligent layer that decides what to do. It's like a project manager who understands the goal, plans the approach, and uses available skills and tools to get the job done.
Note that not all these agents are exposed to users, in which case they are available as skills for other agents to use under the hood.
The Ada ecosystem includes many specialized agents (some of which are shown in the image above), each designed for specific analytical and reporting tasks.
Why specialization helps:
The agent toolkit is built on four foundational concepts that enable flexible and powerful agent development:
The core reasoning component - a large language model equipped with specialized skills and capabilities.
In addition to the model itself, an agent definition typically includes:
A versatile building block that packages how to do something. This modularity allows agents to be composed and extended dynamically.
A skill may:
A mechanism for injecting domain-specific expertise into agents at runtime, enabling them to operate effectively in specialized fields without requiring model retraining.
An intelligent storage system that helps agents overcome context-management challenges by preserving important information for future use, enabling continuity across interactions.
Current implementation supports several advanced capabilities enabled by the agent toolkit:
Agents can build structured plans that
…（省略）


---
## Anura 2.8.19 Upgrade - Release Notes
**URL:** https://optilogic.com/resources/help-center/docs/anura-2-8-19-upgrade---release-notes

We are excited to announce the upcoming release of Anura schema version 2.8.19, with enhancements to our engines and model run options. The migration rollout will start soon and is expected to be completed by the end of March.
All updates in this release are additive — there are no breaking changes.
Neo
Hopper
Other
Model Run Options
MaxNumberOfSourcesToConsiderForMultiStopRoutes DendroTimeoutCYCLO - Multi-Echelon Inventory Optimization
CompartmentConfigurationsInventorySettingsUtilityCurvesInventoryNetworkSummaryInventorySafetyStockSummaryInventoryValidationErrorReportTransportationAssets.CompartmentConfigurationNameTransportationPolicies.MaximumServiceTimeTransportationPolicies.MaximumServiceTimeUOMTransportationPolicies.MinimumServiceTimeTransportationPolicies.MinimumServiceTimeUOMOptimizationProcessSummary.DisposalBehaviorTransportationShipmentSummary.CompartmentNameIf you have any questions or concerns about this upcoming Anura upgrade, please reach out to Optilogic Support at support@optilogic.com.
We are excited to announce the upcoming release of Anura schema version 2.8.19, with enhancements to our engines and model run options. The migration rollout will start soon and is expected to be completed by the end of March.
All updates in this release are additive — there are no breaking changes.
Neo
Hopper
Other
Model Run Options
MaxNumberOfSourcesToConsiderForMultiStopRoutes DendroTimeoutCYCLO - Multi-Echelon Inventory Optimization
CompartmentConfigurationsInventorySettingsUtilityCurvesInventoryNetworkSummaryInventorySafetyStockSummaryInventoryValidationErrorReportTransportationAssets.CompartmentConfigurationNameTransportationPolicies.MaximumServiceTimeTransportationPolicies.MaximumServiceTimeUOMTransportationPolicies.MinimumServiceTimeTransportationPolicies.MinimumServiceTimeUOMOptimizationProcessSummary.DisposalBehaviorTransportationShipmentSummary.CompartmentNameIf you have any questions or concerns about this upcoming Anura upgrade, please reach out to Optilogic Support at support@optilogic.com.


---
## Anura 2.8 Upgrade Information
**URL:** https://optilogic.com/resources/help-center/docs/anura-2-8-upgrade-information

Anura 2.8 Upgrade Information
With the 2.8 version of Anura there are quite a few new tables and columns being added, along with a small number of existing columns that have been renamed. These updates enable new features including, but not limited to, the following:
- Time window support for HOPPER
- Detailed rate structures for HOPPER
- Load Balancing for HOPPER
- CO2 Emissions for HOPPER / NEO
- New costs and constraints in NEO
- Production Wheels in THROG
- Transportation Route Planning in THROG
We will cover the 2 instances of breaking changes below, followed by a more detailed review of schema adjustments specific to each solver. If you have any questions regarding these updates, please do not hesitate to reach out to support@optilogic.com for further information.
BREAKING CHANGES
2.7_TransportationRates
The Transportation Rates table previously used by NEO has been renamed to Transportation Band Costing in 2.8. This is done to allow for a Hopper-specific table to be built out and take the name of Transportation Rates. All data upgrades will be processed automatically, but any ETL workflows that targeted the Transportation Rates table in 2.7 will need to be updated.
2.7_OptimizationCostToServeParentInformationReport
Optimization Cost To Serve Parent Information Report has had the CurrentNodeName and ParentNodeName renamed to CurrentSiteName and ParentSiteName. All upgrades will be handled automatically, but any dashboards or external data visualizations that target these columns would need to be updated.
HOPPER Enhancements
- Time Windows- OperatingSchedule has been added to the Transportation Assets table
- OperatingSchedule will now be supported for Facilities and Customers
- MaxWaitTimePerRoute has been added to the Assets table
 
- Breaks / Rests- Many fields added to the Transportation Assets table to cover the max drive and max duty time before breaks / rests, how long breaks / rests will be
 
- Delivery / Pickup Time- Fixed and unit delivery time fields have been added to the Customers and Facilities tables
 
- Out Of Route Distance- Fields added to the Transportation Assets table to define the max out of route distance
 
- Transportation Rates- The existing 2.7 Transportation Rates table has been renamed to Transportation Band Costing, with a new Hopper-specific table added taking the name of Transportation Rates. This will now support location-specific rate structures
- TransportationRateName / TransportationRateType columns added to the Transportation Assets table
 
- Load Balancing Tables- Load Balancing Demand / Schedules have been added to enable load balancing problems
 
- CO2- CO2 inputs have been added to the Transportation Assets table
- Asset Weight has been added to the Transportation Assets table
 
- Output Tables- New columns added to relevant tables to report new input capabilities
- Transportation Activity Report
- Transportation Tour Summary
- Transportation Validation Report
 
NEO Enhancements
- Demand Origin Constr
…（省略）


---
## Application Stuck On Loading Screen
**URL:** https://optilogic.com/resources/help-center/docs/application-stuck-on-loading-screen

If you are running into issues loading Atlas or Cosmic Frog initially where the loading spinner is stuck on the screen you can attempt to perform a hard refresh of the browser. This spinner being stuck can be caused by the website loading a stale token and refreshing the page without loading from cache should generate a fresh token.
To perform a hard refresh of the browser hit CTRL + F5. Alternatively, you can hit the refresh button in the browser while holding down CTRL.
If the issue persists, please reach out to support@optilogic.com.
If you are running into issues loading Atlas or Cosmic Frog initially where the loading spinner is stuck on the screen you can attempt to perform a hard refresh of the browser. This spinner being stuck can be caused by the website loading a stale token and refreshing the page without loading from cache should generate a fresh token.
To perform a hard refresh of the browser hit CTRL + F5. Alternatively, you can hit the refresh button in the browser while holding down CTRL.
If the issue persists, please reach out to support@optilogic.com.


---
## Auto-Archiving Databases
**URL:** https://optilogic.com/resources/help-center/docs/auto-archiving-databases

The Auto-Archiving feature helps keep your account clean and efficient while ensuring Optilogic maintains a streamlined, cost-effective storage footprint. By automatically archiving inactive databases, we reduce unnecessary server load, improve overall performance, and free up space so you can always create new Cosmic Frog models or DataStar projects when you need them.
From your perspective, Auto-Archiving means less manual cleanup and more confidence that your account is organized, fast, and ready for your next project.
Archiving moves a database from an active state into long-term storage. Once archived:
Important: Auto-archiving does not delete your data. You are always in control and can restore an archived database back into an active state.
With Auto-Archiving, you do not need to manually track and archive inactive databases. Our system will automatically archive any database that has been inactive for 90 days.
The screenshot below shows the notifications you will receive when 1) there are databases in your account that meet the criteria for an auto-archive event and 2) once databases have been archived:
Now, we will take a look at the Notifications Page, which is opened using the pop-out icon in the in-app notification, described under bullet #4 above:
Clicking on the “View Items” link of a “Scheduled Database Archive” in-app notification (see bullet #5 of the first screenshot) will take you to a filtered view in the Cloud Storage application where you can see all the databases that will be auto-archived (note that this shows a different example with different databases to be archived as the previous screenshots):
This next screenshot shows the filter that is applied on the Databases tab:
Clicking on the “View Items” link of a “Databases Archived” in-app notification (see bullet #5 of the first screenshot) will again take you to a filtered view in the Cloud Storage application where you can see the databases that have been auto-archived:
Finally, the following screenshot shows the filter that was applied on the Archived Databases tab:
Archiving is not just about organization — it also enhances performance across the platform. By reducing the number of idle databases consuming system resources, we lower the likelihood of “noisy neighbor” effects (when unused databases cause latency or compete with active ones).
With fewer inactive databases on high-availability servers, your active databases run faster and more reliably.
To keep a database active, simply interact with it. Any of the following actions will reset its inactivity timer:
Performing any of these actions ensures the database will not be archived.
Restoring an archived database is quick and straightforward:
The system will start a background job to restore the database. You can track progress at any time on the Account Activity page.
What to expect:
Quota reminder: To unarchive a database, you will need enough space in your database quota. If you have already reached your limit, y
…（省略）


---
## Building Scenarios
**URL:** https://optilogic.com/resources/help-center/docs/building-scenarios

Fast, AI-driven supply chain decision orchestration for every individual and team —from strategic design to tactical planning.
Model, optimize, and simulate even the most complex supply chains at scale and trade off cost, service, risk, and sustainability.
Eliminate data challenges with AI-automated cleansing and workflow orchestration for decision-ready intelligence instantly.
Optilogic's breakthrough agentic AI system for supply chain design — compresses months of supply chain design work into a single day.
Purpose-built apps for every stakeholder — Deploy across your entire organization today. Act on insights from day one.
Stay updated on the latest from Optilogic.
Enhance your skills with our hands-on training sessions and courses.
Dive into expert insights, industry trends, and practical tips for success.
Discover Optilogic's partner network empowering transformation and supply chain success.
Discover on-demand interviews, demos, and customer sessions.
Find step-by-step guides, FAQs, and support.
Access our full library of guides, case studies, and tools to help you succeed.
Connect with Optilogic peers, exchange insights, and accelerate supply chain success.
Watch the video to learn how to create, manage and hyperscale scenarios:


---
## Building Your First Cosmic Frog Model
**URL:** https://optilogic.com/resources/help-center/docs/building-your-first-cosmic-frog-model

We have prepared step-by-step instructions to build your own version of the Global Supply Chain Strategy model from scratch.
Please download the “Build your first Frog model.zip” file, save to your local machine, and follow the overview and instructions laid out in the following videos.
We have prepared step-by-step instructions to build your own version of the Global Supply Chain Strategy model from scratch.
Please download the “Build your first Frog model.zip” file, save to your local machine, and follow the overview and instructions laid out in the following videos.


---
## Categorizing Anura Tables
**URL:** https://optilogic.com/resources/help-center/docs/categorizing-anura-tables

The Anura data model contains 11 categories of tables. The most basic of models can be built by only populated six tables (Customers, Facilities, Products, Customer Demand, Production Policies, and Transportation Policies); however, most models require a few tables from each modeling category to build out a realistic interpretation of the supply chain.
Tables are grouped into the following sections:
The Anura data model contains 11 categories of tables. The most basic of models can be built by only populated six tables (Customers, Facilities, Products, Customer Demand, Production Policies, and Transportation Policies); however, most models require a few tables from each modeling category to build out a realistic interpretation of the supply chain.
Tables are grouped into the following sections:


---
## Choosing to “Run in Studio” versus “Run as Job”
**URL:** https://optilogic.com/resources/help-center/docs/choosing-to-run-in-studio-versus-run-as-job

Python models can be run on your “local” IDE instance or you can leverage the power of hyper-scaling by running the module as a Job. When running as a job you have access to a number of different machine configurations as follows:
For reference, a typical laptop will be equivalent to either a XS or S machine configuration.
Complex optimization models may require more CPU cores to solve quickly and large scale simulations may require the use of more RAM due to increase in data required for model fidelity.
Python models can be run on your “local” IDE instance or you can leverage the power of hyper-scaling by running the module as a Job. When running as a job you have access to a number of different machine configurations as follows:
For reference, a typical laptop will be equivalent to either a XS or S machine configuration.
Complex optimization models may require more CPU cores to solve quickly and large scale simulations may require the use of more RAM due to increase in data required for model fidelity.


---
## Comparing Cosmic Frog to Other Supply Chain Design Software
**URL:** https://optilogic.com/resources/help-center/docs/comparing-cosmic-frog-to-other-supply-chain-design-software

If this isn’t your first time using a supply chain design software, then take heart: the transition to Cosmic Frog is a smooth one. There are a few key differences worth noting below:
Most of these changes will be self-explanatory – if you used to write Customer Sourcing Policies you will now put similar data in a table called Customer Fulfillment Policies. Others may become easier to see over time — instead of many tables to create process logic you can enter everything you need in one table.
Have you ever wanted to put a site in your model and distinguish whether you owned the site or not? Have you ever wanted to make clear what you own and what you outsource? If so, the suppliers tables are for you:
Do you really need a corresponding transportation policy for every sourcing policy and vice versa? Did you know that by doing so you actually making the model take longer to build and solve? Have you ever built a model that was infeasible because you forgot to add a policy?
We put the power in you, the user’s, hands. Simply change the lane creation rule and you can ensure that your model builds and solves the way you want.
We split inventory policies into three sections because we believe there is a lot going on when you process how to model inventory in your models, especially when you process inventory in simulation. Other than that, we cleaned up the table structure, why enter data in multiple tables if you don’t need to? Where possible we streamlined the table structure to make it easier to enter your data.
If this isn’t your first time using a supply chain design software, then take heart: the transition to Cosmic Frog is a smooth one. There are a few key differences worth noting below:
Most of these changes will be self-explanatory – if you used to write Customer Sourcing Policies you will now put similar data in a table called Customer Fulfillment Policies. Others may become easier to see over time — instead of many tables to create process logic you can enter everything you need in one table.
Have you ever wanted to put a site in your model and distinguish whether you owned the site or not? Have you ever wanted to make clear what you own and what you outsource? If so, the suppliers tables are for you:
Do you really need a corresponding transportation policy for every sourcing policy and vice versa? Did you know that by doing so you actually making the model take longer to build and solve? Have you ever built a model that was infeasible because you forgot to add a policy?
We put the power in you, the user’s, hands. Simply change the lane creation rule and you can ensure that your model builds and solves the way you want.
We split inventory policies into three sections because we believe there is a lot going on when you process how to model inventory in your models, especially when you process inventory in simulation. Other than that, we cleaned up the table structure, why enter data in multiple tables if you don’t need to? Where possible we 
…（省略）


---
## Connecting to Optilogic with Alteryx
**URL:** https://optilogic.com/resources/help-center/docs/connecting-to-optilogic-with-alteryx

The following instructions show how to establish a local connection, using Alteryx, to an Optilogic model that resides within our platform. These instructions will show you how to:
Watch the video for an overview of the connection process:
A step by step set of instructions can also be downloaded in the slide deck here: CosmicFrog-Alteryx-Connection-Instructions
To make a local connection you must first open a Firewall connection between your current IP address and the Optilogic platform. Navigate to the Cloud Storage app – note that the app selection found on the left-hand side of the screen might need to be expanded. Check to see if your current IP address is authorized and if not, add a rule to authorize this IP address. You can optionally set an expiration date for this authorization.
If you are working from a new IP Address, a banner notification should be displayed to let you know that the new IP Address will need to be authorized.
From the Databases section of the Cloud Storage page, click on the database that you want to connect to. Then, click on the Connection Strings button to display all of the required connection information.
We have connection information for the following formats:
To select the format of your connection information, use the drop-down menu labeled Select Connection String:
For this example, we will copy and paste the strings for the ‘PSQL’ connection. The screen should look something like the following:
You can click on any of the parameters to copy them to your clipboard, and then paste them into the relevant field when establishing the PSQL ODBC connection.
Many tools, including Alteryx, use Open Database Connectivity (ODBC) to enable a connection to the Cosmic Frog model database. To access the Cosmic Frog model, you will need to download and install the relevant ODBC drivers. Latest versions of the drivers are located here: https://www.postgresql.org/ftp/odbc/releases/
From here, click on the latest parent folder, which as of June 20, 2024 will be REL-16_00_0005. Select and download the psqlodbc_x64.msi file.
When installing, use the default settings from the installation wizard.
At this point we have the pieces to make a connection in Alteryx. Open Alteryx and start a new Workflow. Drag the Input Data action into the Workflow and click to “Connect a File or Database.”
Select “Data sources” and scroll down to select “PostgresSQL ODBC”
On the next screen click “ODBC Admin” to setup the connection.
Click “Add” to create a new connection and then select “PostgreSQL ANSI(x64)” then click “Finish.”
Now we need to configure the connection with the information we gathered from the connection strings.
“Data Source” and “Description” allow you to name the connection, these can be named whatever you wish.
Copy the values for “Server”, “Database”, “User Name”, “Password” and “Port” from the connection string information copied from Optilogic Cloud Storage (see above).
DON’T FORGET to select “require” in “SSL Mode”
You may 
…（省略）


---
## Connecting to Optilogic with Azure Data Studio
**URL:** https://optilogic.com/resources/help-center/docs/connecting-to-optilogic-with-azure-data-studio

The following instructions show how to establish a local connection, using Azure Data Studio, to an Optiogic model that resides in the platform. These instructions will show you how to:
Watch the video for an overview of the connection process:
To make a local connection you must first open a Firewall connection between your current IP address and the Optilogic platform. Navigate to the Cloud Storage app – note that the app selection found on the left-hand side of the screen might need to be expanded. Check to see if your current IP address is authorized and if not, add a rule to authorize this IP address. You can optionally set an expiration date for this authorization.
If you are working from a new IP Address, a banner notification should be displayed to let you know that the new IP Address will need to be authorized.
From the Databases section of the Cloud Storage page, click on the database that you want to connect to. Then, click on the Connection Strings button to display all of the required connection information.
We have connection information for the following formats:
To select the format of your connection information, use the drop-down menu labeled Select Connection String:
For this example, we will copy and paste the strings for the ‘PSQL’ connection. The screen should look something like the following:
You can click on any of the parameters to copy them to your clipboard, and then paste them into the relevant field in Azure Data Studio when establishing the PSQL connection.
Within Azure Data Studio click the “Extensions” button and type in “postgres” in the search box to find and install the PostgreSQL extension.
Add a new connection in Azure Data Studio, change the connection type to “PostgreSQL, “and enter the arguments for “PSQL” from the Cloud Storage page. NOTE: you will need to click “Advanced” to type in the Port and to change the SSL mode to “require.”
Depending on your organization’s security protocols, one additional step might need to be taken to whitelist Optilogic’s Postgres SQL Server. This can be done by whitelisting the host URL (*.database.optilogic.app) and the port (6432). If you are unsure how to whitelist the server or do not have the necessary permissions, please contact your IT department or network administrator for assistance.
The following instructions show how to establish a local connection, using Azure Data Studio, to an Optiogic model that resides in the platform. These instructions will show you how to:
Watch the video for an overview of the connection process:
To make a local connection you must first open a Firewall connection between your current IP address and the Optilogic platform. Navigate to the Cloud Storage app – note that the app selection found on the left-hand side of the screen might need to be expanded. Check to see if your current IP address is authorized and if not, add a rule to authorize this IP address. You can optionally set an expiration date for this authorization.
If you are wor
…（省略）


---
## Connecting to Optilogic with External Data Tools
**URL:** https://optilogic.com/resources/help-center/docs/connecting-to-optilogic-with-external-data-tools

Fast, AI-driven supply chain decision orchestration for every individual and team —from strategic design to tactical planning.
Model, optimize, and simulate even the most complex supply chains at scale and trade off cost, service, risk, and sustainability.
Eliminate data challenges with AI-automated cleansing and workflow orchestration for decision-ready intelligence instantly.
Optilogic's breakthrough agentic AI system for supply chain design — compresses months of supply chain design work into a single day.
Purpose-built apps for every stakeholder — Deploy across your entire organization today. Act on insights from day one.
Stay updated on the latest from Optilogic.
Enhance your skills with our hands-on training sessions and courses.
Dive into expert insights, industry trends, and practical tips for success.
Discover Optilogic's partner network empowering transformation and supply chain success.
Discover on-demand interviews, demos, and customer sessions.
Find step-by-step guides, FAQs, and support.
Access our full library of guides, case studies, and tools to help you succeed.
Connect with Optilogic peers, exchange insights, and accelerate supply chain success.
Watch the video to learn how to connect your data tool of choice directly to your Optilogic model:


---
## Connecting to Optilogic with Microsoft Power BI
**URL:** https://optilogic.com/resources/help-center/docs/connecting-to-optilogic-with-microsoft-power-bi

The following instructions show how to establish a local connection, using Power BI, to an Optilogic model that resides within our platform. These instructions will show you how to:
To make a local connection you must first open a Firewall connection between your current IP address and the Optilogic platform. Navigate to the Cloud Storage app – note that the app selection found on the left-hand side of the screen might need to be expanded. Check to see if your current IP address is authorized and if not, add a rule to authorize this IP address. You can optionally set an expiration date for this authorization.
If you are working from a new IP Address, a banner notification should be displayed to let you know that the new IP Address will need to be authorized.
From the Databases section of the Cloud Storage page, click on the database that you want to connect to. Then, click on the Connection Strings button to display all of the required connection information.
We have connection information for the following formats:
To select the format of your connection information, use the drop-down menu labeled Select Connection String:
For this example, we will copy and paste the strings for the ‘PSQL’ connection. The screen should look something like the following:
You can click on any of the parameters to copy them to your clipboard, and then paste them into the relevant field when establishing the PSQL ODBC connection.
Many tools, including Alteryx, use Open Database Connectivity (ODBC) to enable a connection to the Cosmic Frog model database. To access the Cosmic Frog model, you will need to download and install the relevant ODBC drivers. Latest versions of the drivers are located here: https://www.postgresql.org/ftp/odbc/releases/
From here, click on the latest parent folder, which as of June 20, 2024 will be REL-16_00_0005. Select and download the psqlodbc_x64.msi file.
When installing, use the default settings from the installation wizard.
Within Windows, open the ODBC Data Sources App (hint search: “ODBC” in your Windows spotlight search).
Click “Add” to create a new connection and then select “PostgreSQL ANSI(x64)” then click “Finish.”
Enter the details from your Cloud Storage connection — (hint: click to copy/paste)
You may click “Test” to confirm the connection works or click “Save.”
Open Power BI and select “Get data from another source”
Enter “ODBC” in the Get Data window and select connect
Select your Database connection from the dropdown and click OK
Enter your username and password one last time from the Cloud Storage page
Select the tables you wish to see and use within PowerBI
Create Dashboards of Data from Cosmic Frog tables!
The following instructions show how to establish a local connection, using Power BI, to an Optilogic model that resides within our platform. These instructions will show you how to:
To make a local connection you must first open a Firewall connection between your current IP address and the Optilogic platform. Navigate
…（省略）


---
## Connecting to Optilogic with Snowflake
**URL:** https://optilogic.com/resources/help-center/docs/connecting-to-optilogic-with-snowflake

An example of how to connect a Cosmic Frog model to a Snowflake database, along with a video walkthrough, can be found in the Resource Library. To get a copy of this demo into your own Optilogic account simply navigate to the Resource Library and copy the Snowflake template into your workspace.
An example of how to connect a Cosmic Frog model to a Snowflake database, along with a video walkthrough, can be found in the Resource Library. To get a copy of this demo into your own Optilogic account simply navigate to the Resource Library and copy the Snowflake template into your workspace.


---
## Connecting via API
**URL:** https://optilogic.com/resources/help-center/docs/connecting-via-api

Optilogic provides a uniform, easy to use way to connect to your models and embed optimization and simulation in any application that can make an API call.
With a free account you have access to our API capabilities to build and deploy custom solutions.
There are a number of calls that you will need to make to fully automate the use of optimization and simulation in your models. Below you will find more information on how to go about this task.
For full API documentation see our Optilogic API Documentation. From this page you will be able to view detailed API documentation and live test code within your account.
First, to use any API call you must be authenticated. One authenticated you will be provided with an API key that remains active for an hour. If your API key expires you will be required to re-authenticate to acquire a new key.
The Account API section of calls allows you to lookup your account information such as username, email, how many concurrent solves you have access to, and the number of workspaces in your account.
The Workspace API section of calls allows you to lookup information about a specific workspace. You can look up the workspace by name, obtaining a list of files in the workspace as well as a list of jobs associated with the models of that workspace.
The Job API section of calls allows you to view information relating to jobs in the system. Each time you execute a model solve, the Optilogic back end solver system, Andromeda, will spawn a new job to handle the request. The API call to start a job will return a key with which you can lookup information about that job, even after it has completed. With these API calls you can get any job’s status, start a new job, or delete a particular job.
The Files API section of calls allows you to interact with the files of a given workspace. Each model is made up of a collection of files (mainly code and data files). With these calls you can copy, delete, upload or download any file of in a specified workspace.
Optilogic provides a uniform, easy to use way to connect to your models and embed optimization and simulation in any application that can make an API call.
With a free account you have access to our API capabilities to build and deploy custom solutions.
There are a number of calls that you will need to make to fully automate the use of optimization and simulation in your models. Below you will find more information on how to go about this task.
For full API documentation see our Optilogic API Documentation. From this page you will be able to view detailed API documentation and live test code within your account.
First, to use any API call you must be authenticated. One authenticated you will be provided with an API key that remains active for an hour. If your API key expires you will be required to re-authenticate to acquire a new key.
The Account API section of calls allows you to lookup your account information such as username, email, how many concurrent solves you have access
…（省略）


---
## Cosmic Frog Data Tables – Row Grouping, Aggregation, and Pivoting
**URL:** https://optilogic.com/resources/help-center/docs/cosmic-frog-data-tables-row-grouping-aggregation-and-pivoting

Cosmic Frog users can now perform additional quick analyses on their supply chain models’ input and output data through Cosmic Frog’s new grid features. This functionality enables users to easily apply different types of grouping and aggregation to their data, while also allowing users to view their data in a pivoted format. Think for example of the following use cases:
In this documentation we will cover how grids can be configured to use these new features, show several additional examples, and conclude with a few pointers for effective use of these features.
These new grid features can be accessed from the “Columns” section on the side bar on the right-hand side of input and output tables while in the Data module of Cosmic Frog:
Alternatively, users can also start grouping and subsequently aggregating by right clicking on the column names in the table grid:
We will first cover Row Grouping, then Aggregated Table Mode, and finally Pivot Mode.
Using the row grouping functionality allows users to select 1 column in an input or output table by which all the records in the table will be grouped. These groups of records can be collapsed and expanded as desired to review the data. In the following screenshot the row grouping feature is used to compare the sources of a certain finished good in a particular period for 1 scenario:
When clicking on Columns on the right hand-side of the table to open the row grouping / aggregated table / pivot grid configuration pane shows the configuration for this row grouping:
Once a table is grouped by a field, a next step can be to aggregate one or multiple columns by this grouped field. When this is done, we call this aggregated table mode. Different types of aggregation are available to the user, which will be discussed in this section.
When configuring the grid through the configuration panel that comes up when clicking on Columns on the right-hand side of input & output tables, several options are available to help users find field names quickly and turn multiple on/off simultaneously:
To configure the grid, fields can be dragged and dropped:
Alternatively, instead of dragging and dropping, user can also right-click on the field(s) of interest to add them to the configuration areas. This can be done both in the list with column names at the top of the configuration window as shown in the following screenshot, but also on the column names in the grid itself (which we have seen an example of in the “How to Access the New Grid Features” section above):
In the screenshot above (taken with Pivot Mode on which is why the Column Labels area is also visible), user right-clicked on the Flow Volume field and now user can choose to add it to the Row Groups area (“Group by FlowVolume”), to the ∑ Values area (“Add FlowVolume to values”), or to the Column Labels area (“Add FlowVolume to labels”).
The next screenshot shows the result of a configured aggregated table grid:
When adding numeric fields to the ∑ Values area, the fol
…（省略）


---
## Cosmic Frog’s Integrity Checker
**URL:** https://optilogic.com/resources/help-center/docs/cosmic-frogs-integrity-checker

Finding problems with any Cosmic Frog model’s data has just become easier with the release of the Integrity Checker. This tool scans all tables or a selected table in a model and flags any records with potential issues. Field level checks to ensure fields contain the right type of data or a valid value from a drop-down list are included, as are referential integrity checks to ensure the consistency and validity of data relationships across the model’s input tables.
In this documentation we will first cover the Integrity Checker tool’s scope, how to run it, and how to review its results. Next, we will compare the Integrity Checker to other Cosmic Frog data validation tools, and we will wrap up with several tips & tricks to help users make optimal use of the tool.
Integrity Checker Scope
The Integrity Checker extends cell validation and data entry helper capabilities to support users identify a range of issues relating to referential integrity and data types before running a model. The following types of data and referential integrity issues are being checked for when the Integrity Checker is run:
Here, we provide a high-level description for each of these 4 categories; in the appendix at the end of this help center article more details and examples for each type of check are given. From left to right:
Numeric: checks that the field contains a number within the expected valid range. Specific checks for this type of issue are:
Unit of Measure (UoM): checks that UoM fields contain valid values from the Units of Measure table Symbol column for any of the allowed Unit of Measure Types for that field.
Master table: these are referential integrity checks to ensure data relationships between input tables are consistent and valid.
Data Type: checks that the type of data that is entered into the field matches the data type of the field.
Running the Integrity Checker
The Integrity Checker can be accessed in two ways while in Cosmic Frog’s Data module: from the pane on the right-hand side that also contains Model Assistant and Scenario Errors or from the Grid drop-down menu. The latter is shown in the next screenshot:
We are in Cosmic Frog on the Optilogic platform (optilogic.app).
If you are not in the Data module yet, click on the Module Menu icon (the icon with 3 horizontal bars) and select “Data”.
From the Grid drop-down menu, user can choose from 2 options to run the Integrity Checker:
Check all tables* in the model.
Check only the selected table, which is the active table showing in the center of Cosmic Frog.
*Please note that in this first version of the Integrity Checker, the Inventory Policies and Inventory Policies Multi-Time Period tables are not included in any checks the Integrity Checker performs. All other tables are.
The second way to access the Integrity Checker is, as mentioned above, from the pane on the right-hand side in Cosmic Frog:
This pane on the right-hand side either shows the Model Assistant when the first of the 3 icons (the one w
…（省略）


---
## Cost to Serve Outputs (Optimization)
**URL:** https://optilogic.com/resources/help-center/docs/cost-to-serve-outputs-optimization

When modeling supply chains, stakeholders are often interested in understanding the cost to serve specific customers and/or products for segmentation and potential reposition purposes. In order to calculate the cost to serve, variable costs incurred all along the path through the supply chain need to be aggregated, while fixed costs that are incurred need to be apportioned to the correct customer/product. This is not always straightforward and easy to do, think for example of multi-layer BOMs.
When running a network optimization (using the Neo engine) in Cosmic Frog, these cost to serve calculations are automatically done, and the outputs are written into three output tables. In this help center article, we will cover these output tables and how the calculations underneath to populate them work.
First, we will briefly cover the example model used for screenshots for most of this help center article, then we will cover the 3 cost to serve output tables in some detail, and finally we will discuss a more complex example that uses detailed production elements too.
Network Optimization Output Tables related to Cost To Serve
There are 3 network optimization output tables which contain cost to serve results; they can be found in the Output Summary Tables section of the output tables list:
Use Cosmic Frog’s Module menu to go to the Data module.
Once in the Data module, click on the round grid icon to show output tables.
User here searched for “cost” to filter out the tables which contain this word in their names.
There are 3 tables which contain outputs related to cost to serve:
The Optimization Cost To Serve Summary table – contains per unit cost calculations at the period-customer-product level and can be used if desired to aggregate further to the customer or product level.
The Optimization Cost To Serve Path Summary table – contains 1 record for each path in the network (path: from most upstream to furthest downstream location), including all costs that have been incurred along and allocated to the path.
The Optimization Cost To Serve Path Segment Details table – contains details for each segment of each path, including all costs that are incurred on and allocated to the segment.
We will cover the contents and calculations used for these tables by using a relatively simple US Distribution model, which does use quite a few different cost types in it. This model consists of:
50 customers (CZs), 1 in the capital of each of the states in the US
3 distribution centers (DCs) located in Jacksonville FL, Reno NV, and Memphis TN
2 manufacturing locations (MFGs) located in Detroit MI and Dallas TX
4 products
3 yearly periods: 2025, 2026, and 2027
Following screenshot shows the locations and flows of one of the scenarios on a map:
One additional important input to mention is the Cost To Serve Unit Basis field on the Model Settings input table:
User can select Quantity, Volume, or Weight. This basis is used when needing to allocate costs based on amounts of prod
…（省略）


---
## Creating and Managing Models
**URL:** https://optilogic.com/resources/help-center/docs/creating-and-managing-models

The Model Manager in Cosmic Frog is the central place to create, view, organize, and maintain your supply chain models. It provides tools for quickly finding models, understanding their status, and performing common management actions such as editing, duplicating, and deleting models.
This guide walks you through the Model Manager interface step by step, explaining each major feature and control as it appears on screen. Screenshots are annotated with green outlines to highlight key areas, and numbered callouts are explained in corresponding lists so you can easily follow along.
Accessing the Model Manager
When logged into the Optilogic platform, you can open Cosmic Frog by clicking on its icon in the list of applications on the left. Note that the order of the applications may be different in your list so you may need to scroll down:
After opening Cosmic Frog, the model manager will typically be the active module. However, if you have been working in a specific model in Cosmic Frog previously, it may immediately open that model with its Data module being the active module. In that case, you can open the Model Manager from within Cosmic Frog by clicking on the icon with 3 horizontal bars at the left top to open the Module Menu, then select Models:
Model Manager Overview
The Model Manager screen displays a table or grid of your existing models along with high level details such as name, status, and last modified date. This view is designed to give you immediate insight into your model library. The following screenshot shows at a high level the different features of the model manager. Each feature will be explained in more detail in subsequent sections of this documentation:
The icon at the left top indicates we are in the Models module (i.e. Model Manager) of Cosmic Frog.
In the main area of the Model Manager, the models available in the user's account are being shown.
Currently, the models are being show in card format, which is activated by clicking on the left of these 2 icons. Clicking on the right icon will switch the view to list format; the next screenshot shows this.
At the top left of the model grid/list there is an option to (de)select all models simultaneously and there is an indication of how many models are currently selected.
These icons represent common management actions for Cosmic Frog models; each will be explained in more detail in the "Model Management Actions" section further below.
At the top of the Model Manager, there are buttons that can be used to quickly create new Cosmic Frog models. These options are covered in the "Creating a New Model" section.
Search and sort options are available to enable users to quickly find the model(s) of interest. The "Search, Sort, and Filter" section walks through these.
Besides searching and sorting, standard filters can be applied to the model list/grid too to help users find the model(s) they are looking for. These are also explained in the "Search, Sort, and Filter" section.
Clicking on 
…（省略）


---
## Creating Scenarios in Cosmic Frog
**URL:** https://optilogic.com/resources/help-center/docs/creating-scenarios-in-cosmic-frog

To create a scenario you need to do three things:
From the Scenario tab in Cosmic Frog select the blue button called “Scenario” and click on “New Scenario.”
Type the name of the scenario you would like to create in the panel window.
From the same drop down as “New Scenario” select “New Item” to create a scenario item. Enter the name of your scenario item in the window. After you press enter the Scenario Item window will be active where you will select the following:
After you have created and saved the Scenario Item you need to assign that item to a scenario. On the right hand side of your screen there is a table called “Assign Scenarios.” From here you can check/uncheck the Scenarios where you wish to use the new Scenario Item.
To create a scenario you need to do three things:
From the Scenario tab in Cosmic Frog select the blue button called “Scenario” and click on “New Scenario.”
Type the name of the scenario you would like to create in the panel window.
From the same drop down as “New Scenario” select “New Item” to create a scenario item. Enter the name of your scenario item in the window. After you press enter the Scenario Item window will be active where you will select the following:
After you have created and saved the Scenario Item you need to assign that item to a scenario. On the right hand side of your screen there is a table called “Assign Scenarios.” From here you can check/uncheck the Scenarios where you wish to use the new Scenario Item.


---
## CSV File Data Connection
**URL:** https://optilogic.com/resources/help-center/docs/csv-file-data-connection

This documentation covers how to create and configure DataStar CSV File data connections.
Selecting your Data Source File
After opening DataStar, you can use the Create Data Connection button to add new data connections which can be used by all your DataStar projects:
On the DataStar start page, click on the Create Data Connection button which opens the Create Data Connection form.
Type the name for the connection in the Connection Name text box.
Optionally, add a description for the connection in the Connection Description text box. Especially when working with lots of data files and/or collaborating with others, descriptions can be helpful to understand quickly what data is contained in a connection.
Choose the Connection Type from the drop-down list. Options are CSV Files, Excel Files, Cosmic Frog Models, and Postgres Databases. This documentation focuses on the CSV Files connection type.
You can either choose a CSV file already present in your Optilogic account from the list below or drag and drop a file from your local computer on top of this "Drag and Drop" area to upload it to the My Files/DataStar folder in your Optilogic account.
When uploading a file through the drag and drop option, a message confirming successful upload appears here once the upload has completed.
To quickly find the file you want to use for the connection, use this free type Search text box to find CSV files in your account that contain the typed text in their file names.
After clicking on a file in the list, it will appear at the top of the list with a colored background. This is so users can easily see which file they have selected as the file itself could be much further down the list.
The selected file will be greyed out in the list and cannot be clicked on, since it is already the actively selected file.
The list of files contains 3 columns: File Name, Size, and Location. Users can click on the column headings to sort the list by the column's values. Use Ctrl + Shift to sort by multiple columns. Columns can also be resized and dragged to change their order. Click on the 3 vertical dots to bring up a context menu from which additional options for sorting, pinning, auto-sizing, and choosing columns can be accessed.
Once the user has configured the parameters on the right-hand side of the form (not shown in the above screenshot; covered in the screenshots that follow), clicking on the Add Connection button will create the connection.
Configuration Options
On the right-hand side of the Create Data Connection form, configuration options for the creation of the CSV File data connection are available. These will be covered now using the following screenshots.
Parameters
There are 3 different configuration sections; each can be expanded or collapsed by using the caret icon to the left of the section's name.
Parameters - setting these appropriately ensures the data in the CSV file is interpreted correctly.
Column Selection - this allows users to choose a subset of columns
…（省略）


---
## Custom Risk Profiles in Cosmic Frog
**URL:** https://optilogic.com/resources/help-center/docs/custom-risk-profiles-in-cosmic-frog

Being able to assess the Risk associated with your supply chain has increasingly become more important in a quickly changing world with high levels of volatility. Not only does Cosmic Frog calculate an overall supply chain risk score for each scenario that is run, but it also gives you details about the risk at the location and flow level, so you can easily identify the highest and lowest risk components of your supply chain and use that knowledge to quickly set up new scenarios to reduce the risk in your network.
By default, any Neo optimization, Triad greenfield or Throg simulation model run will have the default risk settings, called OptiRisk, applied using the DART risk engine. See also the Getting Started with the Optilogic Risk Engine documentation. Here we will cover how a Cosmic Frog user can set up their own risk profile(s) to rate the risk of the locations and flows in the network and that of the overall network. Inputs and outputs are covered and in the last section notes & tips & additional resources are listed.
The following diagram shows the Cosmic Frog risk categories, their components, and subcomponents.
A description of these risk components and subcomponents follows here:
Custom risk profiles are set up and configured using the following 9 tables in the Risk Inputs section of Cosmic Frog’s input tables. These 9 input tables can be divided into 5 categories:
Following is a summary of these table categories; more details on individual tables will be discussed below:
We will cover some of the individual Risk Input tables in more detail now, starting with the Risk Rating Configurations table:
In the Risk Summary Configurations table, we can set the weights for the 4 different risk components that will be used to calculate the overall Risk Score of the supply chain. The 4 components are: customers, facilities, suppliers, and network. In the screenshot below, customer and supplier risk are contributing 20% each to the overall risk score while facility and network risk are contributing 30% each to the overall risk score.
These 4 weights should add up to 1 (=100%). If they do not add up to 1, Cosmic Frog will still run and automatically scale the Risk Score up or down as needed. For example, if the weights add up to 0.9, the final Risk Score that is calculated based on these 4 risk categories and their weights will be divided by 0.9 to scale it up to 100%. In other words, the weight of each risk category is multiplied by 1/0.9 = 1.11 so that the weights then add up to 100% instead of 90%. If you do not want to use a certain risk category in the Risk Score calculation, you can set its weight to 0. Note that you cannot leave a weight field blank. These rules around automatically scaling weights up or down to add up to 1 and setting a weight to 0 if you do not want to use that specific risk component or subcomponent also apply to the other “… Risk Configurations” tables.
Following are 2 screenshots of the Facility Risk Configurations table
…（省略）


---
## Data Cleansing AI Agent
**URL:** https://optilogic.com/resources/help-center/docs/data-cleansing-ai-agent

The Data Cleansing Agent is one of Ada’s AI-powered assistants. It helps users profile, clean, and standardize their database data without writing code. Users describe what they want in plain English -- such as "find and fix postal code issues in the customers table" or "standardize date formats in the orders table to ISO" -- and the agent autonomously discovers issues, creates safe working copies of the data, applies the appropriate fixes, and verifies the results. The agent handles common supply chain data problems including mixed date formats, inconsistent country codes, Excel-corrupted postal codes, missing values, outliers, and messy text fields. It expects a connected database with one or more tables as input. The output is a set of cleaned copies of their tables in the database which users can immediately use for Cosmic Frog model building, reporting, or further analysis, while the original data is preserved untouched for comparison or rollback.
This documentation describes how this specific agent works and can be configured, including walking through multiple examples. Please see the “AI Agents: Architecture and Components” Help Center article if you are interested in understanding how the Optilogic AI Agents work at a detailed level.
Cleaning and standardizing data for supply chain modeling typically requires significant manual effort -- writing SQL queries, inspecting column values, fixing formatting issues one at a time, and verifying results. The Data Cleansing Agent streamlines this process by turning a single natural language prompt into a full profiling, cleaning, and verification workflow.
Key Capabilities:
Tools:
The agent can be accessed on the next generation Optilogic platform by chatting with Ada and through the Run AI Agent task in DataStar. Both ways will be explained, via Ada first, then the DataStar workflow, followed by an overview of the main differences between the 2 methods.
It is recommended to be somewhat familiar with Ada before diving into this content. Please see the Getting Started with Ada & Agentic AI article, and in particular its How to Use Ada section.
Once logged into the next-generation Optilogic platform at https://ai.optilogic.app, you can start chatting with Ada leveraging the Data Cleansing Agent right away from the central part of the Home page.
Regarding how to write good prompts, please note that the general Best Practices, Tips & Tricks, and Current Limitations and Known Behaviors included in the Getting Started with Ada documentation also apply to the Data Cleansing Agent.
After submitting a prompt, the Data Cleansing Agent will start processing and formulating a response:
The Data Cleansing Agent may ask for feedback before proceeding — for example, when:
When Ada finishes, the final response is presented:
For completeness, the cleaned data shows up in the connected database as clean_* table copies — for example, clean_customers, clean_orders — with the originals preserved untouched for comparis
…（省略）


---
## Data Profiler AI Agent
**URL:** https://optilogic.com/resources/help-center/docs/data-profiler-ai-agent

The Data Profiler AI Agent is one of Ada's AI-powered assistants, focused on assessing data. It automatically analyzes the quality, structure, and relationships of data stored in an Optilogic database. By profiling every table and column, the agent creates a comprehensive data-quality catalog that helps users understand their data, identify issues, discover relationships, and prioritize cleansing efforts.
The agent can be accessed by chatting with Ada in the next generation Optilogic platform and via Run AI Agent tasks in DataStar.
Understanding the quality and meaning of data is often one of the most time-consuming steps in any analytics, modeling, or optimization project. The Data Profiler AI Agent automates this process by:
The result is a queryable inventory of your data assets, complete with quality assessments and relationship insights.
The Data Profiler AI Agent performs several layers of analysis.
For every table and column, the agent calculates statistical characteristics such as:
For large datasets, the agent uses deterministic sampling to ensure consistent results across profiling runs.
Using LLM-assisted analysis, the agent generates:
These descriptions help users quickly understand the purpose and meaning of data assets.
Based on semantic classifications, the agent recommends appropriate database data types. Examples include:
These recommendations help improve data consistency and prevent issues such as loss of leading zeros in identifiers.
After semantic types are identified, the agent performs specialized validation checks against actual data values. Examples include:
The agent performs dozens of validation checks tailored to the detected semantic type.
Each detected issue is stored as a single row structured alert. Each alert contains:
Notable specialized checks include:
The agent can identify relationships even when keys are not formally defined in the schema.
The discovery process includes
The Data Profiler AI Agent assigns scores ranging from 0.0 to 1.0 across three dimensions:
The overall score is a weighted average, which is capped if data integrity drops too low. Tables without data receive a baseline minimum score, while tables that generate errors display an error stub so users are always aware of the issue.
Measures whether values are:
When the same column name appears in multiple tables with different semantic tags, a majority vote picks one and corrects the outliers.
The only required input is to point the agent to a database. There are several optional inputs which we will cover in the Using the Data Profiler Agent section below.
The output consists of tables written to the database that was profiled:
In addition to database outputs, the agent generates a timestamped execution log, which includes table processing times, alerts, and primary key/foreign key findings. Reviewing the log can help diagnose profiling issues and understand execution performance.
There are two ways to access the Data Profiler Agent:
Both ways w
…（省略）


---
## DataStar: Data Integration
**URL:** https://optilogic.com/resources/help-center/docs/datastar-data-integration

DataStar users typically will want to use data from a variety of sources in their projects. This data can be in different locations and systems and there are multiple methods available to get the required data into the DataStar application. In this documentation we will describe the main categories of data sources users may want to use and the possible ways of making these available in DataStar for usage.
If you would first like to learn more about DataStar before diving into data integration specifics, please see the Navigation DataStar articles on the Optilogic Help Center.
The following diagram shows different data sources and the data transfer pathways to make them available for use in DataStar:
We will dive a bit deeper into making local data available for use in DataStar building upon what was covered under bullets 5a-5c in the previous screenshot. First, we will familiarize ourselves with the layout of the Optilogic platform:
Next, we will cover the 3 steps to go from data sitting on a user’s computer locally to being able to use it in DataStar in detail through the next set of screenshots. At a high-level the steps are:
To get local data onto the Opitlogic platform, we can use the file / folder upload option:
Select either the file(s) or folder you want to upload by browsing to it/them. After clicking on Open, the File Upload form will be shown again:
Note that files in the upload list that will not cause name conflicts can also be renamed or removed from the list if so desired. This can for example be convenient when wanting to upload most files in a folder, except for a select few. In that case use the Add Folder option and in the list that will be shown, remove the few that should not be uploaded rather than using Add Files and then manually selecting almost all files in a folder.
Once the files are uploaded, you will be able to see them in the Explorer by expanding the folder they were uploaded to or searching for (part of) their name using the Search box.
The second step is to then make these files visible to DataStar by setting up Data Connections to them:
After setting up a Data Connection to a Cosmic Frog model and to a CSV file, we can see the source files in the Explorer, and the Data Connections pointing to these in DataStar side-by-side:
To start using the data in DataStar, we need to take the third step of importing the data from the data connections into a project. Typically, the data will be imported into the Project Sandbox, but this could also be into another Postgres database, including a Cosmic Frog model. Importing data is done using Import tasks; the Configuration tab of one is shown in this next screenshot:
The 3 steps described above are summarized in the following sequence of screenshots:
For a data workflow that is used repeatedly and needs to be re-run using the latest data regularly, users do not need to go through all 3 steps above of uploading data, creating/re-configuring data connections, and creating/re-con
…（省略）


---
## DataStar Quick Start: Cost to Serve Analysis & Visualization with Power BI
**URL:** https://optilogic.com/resources/help-center/docs/datastar-quick-start-cost-to-serve-analysis-visualization-with-power-bi

In this quick start guide we will show how users can seamlessly go from using the Resource Library, Cosmic Frog and DataStar applications on the Optilogic platform to creating visualizations in Power BI. The example covers cost to serve analysis using a global sourcing model. We will run 2 scenarios in this Cosmic Frog model with the goal to visualize the total cost difference between the scenarios by customer on a map. We do this by coloring the customers based on the cost difference.
The steps we will walk through are:
We will first copy the model named “Global Sourcing – Cost to Serve” from the Resource Library to our Optilogic account (learn more about the Resource Library in this help center article):
On the Optilogic platform, go to the Resource Library application by clicking on its icon in the list of applications on the left-hand side; note that you may need to scroll down. Should you not see the Resource Library icon here, then click on the icon with 3 horizontal dots which will then show all applications that were previously hidden too.
Now that the model is in the user’s account, it can be opened in the Cosmic Frog application:
We will only have a brief look at some high-level outputs in Cosmic Frog in this quick start guide, but feel free to explore additional outputs. You can learn more about Cosmic Frog through these help center articles. Let us have a quick look at the Optimization Network Summary output table and the map:
Our next step is to import the needed input table and output table of the Global Sourcing – Cost to Serve model into DataStar. Open the DataStar application on the Optilogic platform by clicking on its icon in the applications list on the left-hand side. In DataStar, we first create a new project named “Cost to Serve Analysis” and set up a data connection to the Global Sourcing – Cost to Serve model, which we will call “Global Sourcing C2S CF Model”. See the Creating Projects & Data Connections section in the Getting Started with DataStar help center article on how to create projects and data connections. Then, we want to create a macro which will calculate the increase/decrease in total cost by customer between the 2 scenarios. We build this macro as follows:
The configuration of the first import task, C2S Path Summary, is shown in this screenshot:
The configuration of the other import task, Customers, uses the same Source Data Connection, but instead of the optimizationcosttoservepathsummary table, we choose the customers table as the table to import. Again, the Project Sandbox is the Destination Data Connection, and the new table is simply called customers.
Instead of writing SQL queries ourselves to pivot the data in the cost to serve path summary table to create a new table where for each customer there is a row which has the customer name and the total cost for each scenario, we can use Leapfrog to do it for us. See the Leapfrog section in the Getting Started with DataStar help center article and this quic
…（省略）


---
## DataStar Quick Start: Creating a Task using Natural Language
**URL:** https://optilogic.com/resources/help-center/docs/datastar-quick-start-creating-a-task-using-natural-language

In this quick start guide we will show how Leapfrog AI can be used in DataStar to generate tasks from natural language prompts, no coding necessary!
This quick start guide builds upon the previous one where a CSV file was imported into the Project Sandbox, please follow the steps in there first if you want to follow along with the steps in this quick start. The starting point for this quick start is therefore a project named Import Historical Shipments that has a Historical Shipments data connection of type = CSV, and a table in the Project Sandbox named rawshipments, which contains 42,656 records.
The Shipments.csv file that was imported into the rawshipments table has following data structure (showing 5 of the 42,656 records):
Our goal in this quick start is to create a task using Leapfrog that will use this data (from the rawshipments table in the Project Sandbox) to create a list of unique customers, where the destination stores function as the customers. Ultimately, this list of customers will be used to populate the Customers input table of a Cosmic Frog model. A few things to consider when formulating the prompt are:
Within the Import Historical Shipments DataStar project, click on the Import Shipments macro to open it in the macro canvas, you should see the Start and Import Raw Shipments tasks on the canvas. Then open Leapfrog by clicking on the Ask Leapfrog AI button to the right in the toolbar at the top of DataStar. This will open the Leapfrog tab where a welcome message will be shown. Next, we can write our prompt in the “Write a message…” textbox.
Keeping in mind the 5 items mentioned above, the prompt we use is the following: “Use the @rawshipments table to create unique customers (use the @rawshipments.destination_store column); average the latitudes and longitudes. Only use records with the @rawshipments.ship_date between July 1 2024 and June 30 2025. Match to the anura schema of the Customers table”. Please note that:
After clicking on the send icon to submit the prompt, Leapfrog will take a few seconds to consider the prompt and formulate a response. The response will look similar to the following screenshot, where we see from top to bottom:
For copy-pasting purposes, the resulting SQL Script is repeated here:
DROP TABLE IF EXISTS customers;
CREATE TABLE customers AS 
SELECT 
  destination_store AS customername, 
  AVG(destination_latitude) AS latitude, 
  AVG(destination_longitude) AS longitude 
FROM rawshipments 
WHERE
  TO_DATE(ship_date, 'DD/MM/YYYY') >= '2024-07-01'::DATE
  AND TO_DATE(ship_date, 'DD/MM/YYYY') <= '2025-06-30'::DATE
GROUP BY destination_store;
Those who are familiar with SQL, will be able to tell that this will indeed achieve our goal. Since that is the case, we can click on the Add to Macro button at the bottom of Leapfrog’s response to add this as a Run SQL task to our Import Shipments macro. When hovering over this button, you will see Leapfrog suggests where to put it on the macro canvas and to connect i
…（省略）


---
## DataStar Quick Start: Export Data to a Cosmic Frog Model
**URL:** https://optilogic.com/resources/help-center/docs/datastar-quick-start-export-data-to-a-cosmic-frog-model

In this quick start guide we will walk through the steps of exporting data from a table in the Project Sandbox to a table in a Cosmic Frog model.
This quick start guide builds upon a previous one where unique customers were created from historical shipments using a Leapfrog-generated Run SQL task. Please follow the steps in that quick start guide first if you want to follow along with the steps in this one. The starting point for this quick start is therefore a project named Import Historical Shipments, which contains a macro called Import Shipments. This macro has an Import task and a Run SQL task. The project has a Historical Shipments data connection of type = CSV, and the Project Sandbox contains 2 tables named rawshipments (42,656 records) and customers (1,333 records).
The steps we will walk through in this quick start guide are:
First, we will create a new Cosmic Frog model which does not have any data in it. We want to use this model to receive the data we export from the Project Sandbox.
As shown with the numbered steps in the screenshot below: while on the start page of Cosmic Frog, click on the Create Model button at the top of the screen. In the Create Frog Model form that comes up, type the model name, optionally add a description, and select the Empty Model option. Click on the Create Model button to complete the creation of the new model:
Next, we want to create a connection to the just created empty Cosmic Frog model in DataStar. To do so: open your DataStar application, then click on the Create Data Connection button at the top of the screen. In the Create Data Connection form that comes up, type the name of the connection (we are using the same name as the model, i.e. “Empty CF Model for DataStar Export”),optionally add a description, select Cosmic Frog Models in the Connection Type drop-down list, click on the name of the newly created empty model in the list of models, and click on Add Connection. The new data connection will now be shown in the list of connections on the Data Connections tab (shown in list format here):
Now, go to the Projects tab, and click on the “Import Historical Shipments” project to open it. We will first have a look at the Project Sandbox and the empty Cosmic Frog model connections, so click on the Data Connections tab:
The next step is to add and configure an Export Task to the Import Shipments macro. Click on the Macros tab in the panel on the left-hand side, and then on the Import Shipments macro to open it. Click on the Export task in the Tasks panel on the right-hand side and drag it onto the Macro Canvas. If you drag it close to the Run SQL task, it will automatically connect to it once you drop the Export task:
The Configuration panel on the right has now become the active panel:
Click on the AutoMap button, and in the message that comes up, select either Replace Mappings or Add New Mappings. Since we have not mapped anything yet, the result will be the same in this case. After using the AutoMap
…（省略）


---
## DataStar Quick Start: Importing a CSV File
**URL:** https://optilogic.com/resources/help-center/docs/datastar-quick-start-importing-a-csv-file

In this quick start guide we will walk-through importing a CSV file into the Project Sandbox of a DataStar project. The steps involved are:
Our example CSV file is one that contains historical shipments from May 2024 through August 2025. There are 42,656 records in this Shipments.csv file, and if you want to follow along with the steps below you can download a zip-file containing it here (please note that the long character string at the beginning of the zip's file name is expected).
Open the DataStar application on the Optilogic platform and click on the Create Data Connection button in the toolbar at the top:
In the Create Data Connection form that comes up, enter the name for the data connection, optionally add a description, and select CSV Files from the Connection Type drop-down list:
If your CSV file is not yet on the Optilogic platform, you can drag and drop it onto the “Drag and drop” area of the form to upload it to the /My Files/DataStar folder. If it is already on the Optilogic platform or after uploading it through the drag and drop option, you can select it in the list of CSV files. Once selected it becomes greyed out in the list to indicate it is the file being used; it is also pinned at the top of the list with darker background shade so users know without scrolling which file is selected. Note that you can filter this list by typing in the Search box to quickly find the desired file. Once the file is selected, users can optionally configure additional settings available on the right-hand side of the form, see the CSV File Data Connection help center article for details on these configuration options. Finally, clicking on the Add Connection button will create the CSV connection:
After creating the connection, the Data Connections tab on the DataStar start page will be active, and it shows the newly added CSV connection at the top of the list (note the connections list is shown in list view here; the other option is card view):
You can either go into an existing DataStar project or create a new one to set up a Macro that will import the data from the Historical Shipments CSV connection we just set up. For this example, we create a new project by clicking on the Create Project button in the toolbar at the top when on the start page of DataStar. Enter the name for the project, optionally add a description, change the appearance of the project if desired by clicking on the Edit button, and then click on the Add Project button:
After the project is created, the Projects tab will be shown on the DataStar start page. Click on the newly created project to open it in DataStar. Inside DataStar, you can either click on the Create Macro button in the toolbar at the top or the Create a Macro button in the center part of the application (the Macro Canvas) to create a new macro which will then be listed in the Macros tab in the left-hand side panel. Type the name for the macro into the textbox:
When a macro is created, it automatically gets a Sta
…（省略）


---
## DataStar Quick Start: Updating Data
**URL:** https://optilogic.com/resources/help-center/docs/datastar-quick-start-updating-data

In this quick start guide we will walk through the steps of modifying data in a table in the Project Sandbox using Update tasks. These changes can either be made to all records in a table or a subset based on a filtering condition. Any PostgreSQL function can be used when configuring the update statements and conditions of Update tasks.
This quick start guide builds upon a previous one where unique customers were created from historical shipments using a Leapfrog-generated Run SQL task. Please follow the steps in that quick start guide first if you want to follow along with the steps in this one. The starting point for this quick start is therefore a project named “Import Historical Shipments”, which contains a macro called Import Shipments. This macro has an Import task and a Run SQL task. The project has a Historical Shipments data connection of type = CSV, and the Project Sandbox contains 2 tables named rawshipments (42,656 records) and customers (1,333 records). Note that if you also followed one of the other quick start guides on exporting data to a Cosmic Frog model (see here), your project will also contain an Export task, and a Cosmic Frog data connection; you can still follow along with this quick start guide too.
The steps we will walk through in this quick start guide are:
We have a look at the customers table which was created from the historical shipment data in the previous 2 quick start guides, see the screenshot below. Sorting on the customername column, we see that they are ordered in alphabetical order. This is because the customer name column is of type text as it starts with the string “CZ”. This leads to them not being ordered based on the number part that follows the “CZ” prefix.
If we want ordering customer names alphabetically to result in an order that is the same as sorting the number part of the customer name, we need to make sure each customer name has the same number of digits. We will use Update tasks to change the format of the number part of the customer names so that they are all 4 digits by adding leading 0’s to those that have less than 4 digits. While we are at it, we will also replace the “CZ” prefix with “Cust_” to make the data consistent with other data sources that contain customer names. We will break the updates to the customer name column up into 3 steps using 3 Update tasks initially. At the end, we will see how they can be combined into a single Update task. The 3 steps are:
Let us add the first Update task to our Import Shipments macro:
After dropping the Update task onto the macro canvas, its configuration tab will be opened automatically on the right-hand side:
If you have not already, click on the plus button to add your first update statement:
Next, we will write the expression for which we can use the Expression Builder area just below the update statements table. What we type there will also be added to the Expression column of the selected Update Statement. These expressions can use any Postgr
…（省略）


---
## Deleting Scenario Output Data
**URL:** https://optilogic.com/resources/help-center/docs/deleting-scenario-output-data

You can clear output data from all model output tables in one quick action. Navigate to the Scenarios tab and from the scenario drop-down menu select the Delete Scenario Results option. This can also be accessed by right-clicking on any scenario name. Next, from the window on the right-hand side of the screen you can select the scenario(s) that you want to delete output data for. Once selected, click the Delete button and all output data will be cleared for the selected scenarios.
You can clear output data from all model output tables in one quick action. Navigate to the Scenarios tab and from the scenario drop-down menu select the Delete Scenario Results option. This can also be accessed by right-clicking on any scenario name. Next, from the window on the right-hand side of the screen you can select the scenario(s) that you want to delete output data for. Once selected, click the Delete button and all output data will be cleared for the selected scenarios.


---
## Dendro: Genetic Algorithm Guide
**URL:** https://optilogic.com/resources/help-center/docs/dendro-genetic-algorithm-guide

Dendro, Optilogic’s simulation-optimization engine, uses a sophisticated Genetic Algorithm (GA) to, for example, optimize inventory policies across your supply chain network. This guide explains how the algorithm works in business-friendly terms, helping you understand what happens when you run Dendro and how to get the best results.
The Big Picture: Dendro's Genetic Algorithm explores thousands of different inventory policy combinations, simulates each one to see how it performs, and gradually evolves toward the best possible solution - much like natural evolution produces better-adapted organisms over time.
Recommended reading prior to diving into this guide: Getting Started with Dendro, which is a higher-level overview of how Dendro works.
Genetic Algorithms are inspired by biological evolution. Just as species evolve to become better adapted to their environment through:
Dendro evolves inventory policies to become better adapted to your business objectives through:
Traditional optimization methods struggle with inventory networks due to:
Genetic Algorithms excel at this type of problem because they:
Dendro's implementation uses three fundamental elements: chromosomes, genes, and fitness score.
A chromosome represents one complete set of inventory policies for your entire supply chain.
Example Chromosome:
Each chromosome is essentially a complete "proposal" for how to manage inventory across your network.
Each gene within a chromosome represents the policy for one facility-product combination.
Example Gene:
Genes can mutate (change their values) to explore different policy settings.
The fitness score measures how good a chromosome is - combining costs, service levels, and other objectives.
Higher scores are better - Dendro displays scores where better solutions have higher values.
A fitness score might combine:
Whenever the below refers to an option, this is a model run option that can be set in the Dendro section of the Technology Parameters on the right-hand side of the Run Settings screen that comes up after a user clicks on the green Run button in Cosmic Frog.
What happens: Dendro creates the initial population of chromosomes (policy combinations).
Implementation details:
Business perspective: Think of this as Dendro assembling a diverse team of proposals. The first proposal is "keep doing what we are doing", while the others explore variations like "increase safety stock by 10%", "reduce order quantities", etc.
Each generation follows the same four-step cycle:
What happens: Each chromosome is evaluated by:
Implementation details:
Business perspective: Dendro tests each proposal by running it through a realistic simulation of your supply chain over time. It is like running a pilot program for each policy combination to see what would actually happen - but virtually, so you can test thousands of options without risk.
Typical duration:
What happens: Dendro ranks all chromosomes by fitness score and selects the best ones to continue to the ne
…（省略）


---
## Dendro: Input Factors Guide
**URL:** https://optilogic.com/resources/help-center/docs/dendro-input-factors-guide

Input factors are at the heart of Dendro optimization - they define what Dendro can change to improve your supply chain performance. Think of input factors as the "knobs" Dendro can turn to find better inventory policies.
Key concepts:
This guide explains how to configure input factors to give Dendro the right level of control over your inventory policies. These can be specified in the Input Factors input table in Cosmic Frog.
Recommended reading prior to diving into this guide: Getting Started with Dendro, a high-level overview of how Dendro works, and Dendro: Genetic Algorithm Guide which explains the inner workings of Dendro in more detail.
An input factor tells Dendro's Genetic Algorithm:
Dendro explores these decisions systematically across your entire network to find the optimal combination.
Dendro supports three types of input factors, each suited for different kinds of optimization variables. These are all specified on the Input Factors input table, see also "The Input Factors Table" section further below.
What they are: Numeric values that can vary within a minimum and maximum range.
Best for:
Configuration fields:
InputFactorName:  WH_A_Prod_1_ReorderPoint TableName:        InventoryPolicies ColumnName:       SimulationPolicyValue1 Filter:           FacilityName='Warehouse A' AND ProductName='Product 1' MinValue:         100 MaxValue:         1000 StepSize:         10 BaseValue:        500 How it works:
Example:
Chromosome 1 (baseline):       500 Chromosome 2 (random):         730 Chromosome 3 (random):         220 Chromosome 4 (mutated from 2): 740 (increased by one step) What they are: Values selected from a predefined list of discrete options.
Best for:
Configuration fields:
InputFactorName:  DC_Policy_Type TableName:        InventoryPolicies ColumnName:       SimulationPolicy Filter:           FacilityName='Distribution Center' Enumerate:        (s,S)|(R,Q)|(T,S) BaseValue:        (s,S) How it works:
Example:
Chromosome 1 (baseline):       (s,S) Chromosome 2 (random):         (R,Q) Chromosome 3 (random):         (T,S) Chromosome 4 (mutated from 2): (s,S) (switched from R,Q) What they are: Grouped input factors that manage related inventory policy parameters together as a coordinated set.
Best for:
How they work:
Example configuration:
Factor 1: InputFactorName:  WH_A_Prod_1_PolicyType TableName:        InventoryPolicies ColumnName:       SimulationPolicy Filter:           FacilityName='Warehouse A' AND ProductName='Product 1' Enumerate:        (s,S)|(R,Q) Factor 2: InputFactorName:  WH_A_Prod_1_Value1 TableName:        InventoryPolicies ColumnName:       SimulationPolicyValue1 Filter:           FacilityName='Warehouse A' AND ProductName='Product 1' MinValue:         0 MaxValue:         1000 StepSize:         10 Factor 3: InputFactorName:  WH_A_Prod_1_Value2 TableName:        InventoryPolicies ColumnName:       SimulationPolicyValue2 Filter:           FacilityName='Warehouse A' AND ProductName='Product 1' MinValue:         0 MaxValue
…（省略）


---
## Dendro: Output Factors Guide
**URL:** https://optilogic.com/resources/help-center/docs/dendro-output-factors-guide

Output factors define what Dendro tries to optimize - they are your business objectives translated into measurable metrics. While input factors control what can change, output factors determine what "better" means.
Key concepts:
This guide explains how to configure output factors to align Dendro's optimization with your business goals. These can be specified in the Output Factors input table in Cosmic Frog models.
Recommended reading prior to diving into this guide: Getting Started with Dendro, a high-level overview of how Dendro works, and Dendro: Genetic Algorithm Guide which explains the inner workings of Dendro in more detail.
An output factor tells Dendro's genetic algorithm:
Imagine you are evaluating employee performance:
Dendro uses the same approach to evaluate inventory policy combinations across your supply chain.
Output factors are configured in the Output Factors input table with the following columns:
Minimize overall supply chain costs:
OutputFactorName:    TotalCost TableName:           SimulationNetworkSummaryReplicationDetail ColumnName:          TotalSupplyChainCost Filter:              (leave empty for all data)UtilityCurve:        [1500000,100],[2000000,0]OutputFactorWeight:  0.40 Status:              Include Interpretation:
Maximize service level performance:
OutputFactorName:    ServiceLevel TableName:           SimulationNetworkServiceSummaryReplicationDetailColumnName:          TotalPlacedCustomerOrderQuantityOnTimeInFullRate Filter:              (leave empty) UtilityCurve:        [0,0],[85,10],[95,99],[100,100]OutputFactorWeight:  0.35 Status:              Include Interpretation:
Focus on inventory costs at distribution centers only:
OutputFactorName:    DC_HoldingCost TableName:           SimulationFacilityCostSummaryReplicationDetail ColumnName:          InventoryHoldingCost Filter:              FacilityType='DC' UtilityCurve:        [50000,100],[150000,0]OutputFactorWeight:  0.25 Status:              Include Interpretation:
The following 2 screenshots show the Output Factors input table in Cosmic Frog; it contains 3 rows which represent the 3 examples above:
A utility curve translates raw metric values (like dollars or percentages) into standardized quality scores (0-100 points). It answers the question: "How good is this value?".
Format:[value1,score1],[value2,score2],[value3,score3],...
Each [value,score] pair defines a point on the curve:
Dendro connects these points with straight lines to create a piecewise linear curve.
[1000,100],[2000,0] 
Meaning:
Visualization:
Best for:
[50,0],[100,50],[150,100] 
Meaning:
Visualization:
Best for:
[0,0],[85,10],[95,99],[100,100] 
Meaning:
Characteristics:
Visualization:
Best for:
The challenge: Early in optimization, Dendro does not know what the best and worst possible values are.
The solution: Utility curves automatically expand when new extremes are discovered.
Example scenario:
Generation 1:
[1800000,100],[2200000,0]Generation 5:
[1600000,100],[2200000,0]Why it matters:
Wh
…（省略）


---
## Detailed Production Modelling in Cosmic Frog (Network Optimization)
**URL:** https://optilogic.com/resources/help-center/docs/detailed-production-modelling-in-cosmic-frog-network-optimization

Depending on the type of supply chain one is modelling in Cosmic Frog and the questions being asked of it, it may be necessary to utilize some or all the features that enable detailed production modelling. A few business case examples that will often include some level of detailed production modelling include:
In comparison, modelling a retailer who buys all its products from suppliers as finished goods, does not require any production details to be added to its Cosmic Frog model. Hybrid models are also possible, think for example of a supermarket chain which manufactures its own branded products and buys other brands from its suppliers. Depending on the modelling scope, the production of the own branded products may require using some of the detailed production features.
The following diagram shows a generalized example of production related activities at a manufacturing plant, all of which can be modelled in Cosmic Frog:
In this help article we will cover the inputs & outputs of Cosmic Frog’s production modelling features, while also giving some examples of how to model certain business questions. The model in Optilogic’s Resource Library that is used mainly for the screenshots in this article is the Multi-Year Capacity Planning. There is a 20-minute video available with this model in the Resource Library, which covers the business case that is modelled and some detail of the production setup too.
To not make this document too repetitive we will cover some general Cosmic Frog functionality here that applies to all Cosmic Frog technologies and is used extensively for production modelling in Neo too.
To only show tables and fields in them that can be used by the Neo network optimization algorithm, select Optimization in the Technologies Filter from the toolbar at the top in Cosmic Frog. This will hide any tables and fields that are not used by Neo and therefore simplifies the user interface.
Quite a few Neo related fields in the input and output tables will be discussed in this document. Keep in mind however that a lot of this information can also be found in the tooltips that are shown when you hover over the column name in a table, see following screenshot for an example. The column name, technology/technologies that use this field, a description of how this field is used by those algorithm(s), its default value, and whether it is part of the table’s primary key are listed in the tooltip.
There are a lot of fields with names that end in “…UOM” throughout the input tables. How they work will be explained here so that individual UOM fields across the tables do not need to be explained further in this documentation as they all work similarly. These UOM fields are unit of measure fields and often appear to the immediate right of the field that they apply to, like for example Unit Value and Unit Value UOM in the screenshot above. In these UOM fields you can type the Symbol of a unit of measure that is of the required Type from the ones specified in 
…（省略）


---
## Downloadable Anura Data Structure – Inputs
**URL:** https://optilogic.com/resources/help-center/docs/downloadable-anura-data-structure---inputs

The best way to understand modeling in Cosmic Frog is to understand the data model and structure. The following link provides a downloadable (Excel) template with the documentation and explanation for every input table and field in the modeling schema.
A downloadable template describing the fields in the output tables can be downloaded from the Downloadable Anura Data Structure - Outputs Help Center article.
For a brief review of how to use the template file, please watch the following video.
The best way to understand modeling in Cosmic Frog is to understand the data model and structure. The following link provides a downloadable (Excel) template with the documentation and explanation for every input table and field in the modeling schema.
A downloadable template describing the fields in the output tables can be downloaded from the Downloadable Anura Data Structure - Outputs Help Center article.
For a brief review of how to use the template file, please watch the following video.


---
## Downloadable Anura Data Structure – Outputs
**URL:** https://optilogic.com/resources/help-center/docs/downloadable-anura-data-structure---outputs

The following link provides a downloadable (excel) template describing the fields included in the output tables for Neo (Optimization), Throg (Simulation), Triad (Greenfield), and Hopper (Routing).
Anura 2.8 is the current schema.
A downloadable template describing the fields in the input tables can be downloaded from the Downloadable Anura Data Structure - Inputs Help Center article.
The following link provides a downloadable (excel) template describing the fields included in the output tables for Neo (Optimization), Throg (Simulation), Triad (Greenfield), and Hopper (Routing).
Anura 2.8 is the current schema.
A downloadable template describing the fields in the input tables can be downloaded from the Downloadable Anura Data Structure - Inputs Help Center article.


---
## Downloading Data from a Cosmic Frog Database in Alteryx
**URL:** https://optilogic.com/resources/help-center/docs/downloading-data-from-a-cosmic-frog-database-in-alteryx

These instructions assume you have already made a connection to your database as described in Connecting to Optilogic with Alteryx.
Once connected you will see the schemas and tables in the Cosmic Frog database. In this case we will select some columns from the Customers table. Drag and drop the tables required to the left hand “Main” pane. Click the columns required. Click OK.
At this point you can run your workflow and it will be populated with the data from the connected database.
These instructions assume you have already made a connection to your database as described in Connecting to Optilogic with Alteryx.
Once connected you will see the schemas and tables in the Cosmic Frog database. In this case we will select some columns from the Customers table. Drag and drop the tables required to the left hand “Main” pane. Click the columns required. Click OK.
At this point you can run your workflow and it will be populated with the data from the connected database.


---
## Editing Dashboards and Visualizations
**URL:** https://optilogic.com/resources/help-center/docs/editing-dashboards-and-visualizations

You can customize existing dashboards to fit your needs.
Inside of a dashboard, add a new visualization:
or edit an existing visualization:
The most common elements of visualizations are values and labels.
Values represent the data you want to be presented in the visualization. Typically, values are aggregated representations of your data (e.g. sum, average, etc.).
Labels refer to the labels on the visualization axes and consequently the groups by which you want to aggregate your values.
To build a visualization, we drag fields (i.e. database columns) into these elements.
Other elements include categories which allow for additional grouping and filters which allow users to adjust inclusion and exclusion criteria while viewing the dashboard.
You can use the Analytics dropdown button to create a new dashboard.
You can use the “+” button to add your first visualization to the dashboard.
You can customize existing dashboards to fit your needs.
Inside of a dashboard, add a new visualization:
or edit an existing visualization:
The most common elements of visualizations are values and labels.
Values represent the data you want to be presented in the visualization. Typically, values are aggregated representations of your data (e.g. sum, average, etc.).
Labels refer to the labels on the visualization axes and consequently the groups by which you want to aggregate your values.
To build a visualization, we drag fields (i.e. database columns) into these elements.
Other elements include categories which allow for additional grouping and filters which allow users to adjust inclusion and exclusion criteria while viewing the dashboard.
You can use the Analytics dropdown button to create a new dashboard.
You can use the “+” button to add your first visualization to the dashboard.


---
## Editing Map Data
**URL:** https://optilogic.com/resources/help-center/docs/editing-map-data

For a detailed walk-through of all map features, please see the "Getting Started with Maps" Help Center article.
You can edit and filter the base data located with a map using the Map Filter menu. This menu opens when the map name is highlighted or selected. From here you are able to select the following items to be shown in the map:
Note: leaving the product filter blank will include all products in the model
For a detailed walk-through of all map features, please see the "Getting Started with Maps" Help Center article.
You can edit and filter the base data located with a map using the Map Filter menu. This menu opens when the map name is highlighted or selected. From here you are able to select the following items to be shown in the map:
Note: leaving the product filter blank will include all products in the model


---
## Editing Map Layers
**URL:** https://optilogic.com/resources/help-center/docs/editing-map-layers

For a detailed walk-through of all map features, please see the "Getting Started with Maps" Help Center article.
You can edit and filter the information shown in a map layer by utilizing the Layer Menu on the right hand side of your map screen. This menu opens when a layer is selected and contains the following tabs:
From the layer style menu we can modify how the layer will appear on the map
From the layer label menu we can add text descriptors the map layer.
The “Labels” dropdown menu allow you to add a text descriptor next to a layer item. Only one item may be selected in the label dropdown.
The “Tooltip” is a floating box that appears when hovering over a layer element. We can add/remove items displayed in the tooltip by selecting in the “Tooltips” menu.
The Condition Builder menu allows you to edit the data included in your layer. The most important item is to select the Table Name using the drop down menu that you wish to show on the map. This can include point items like Customers or Facilities or transportation arcs like OptimizationFlowSummary.
Within the Condition Builder you can use conditions to filter the table further to a subset of the data in the table. The filter syntax is similar to the syntax used when creating scenarios.
For a detailed walk-through of all map features, please see the "Getting Started with Maps" Help Center article.
You can edit and filter the information shown in a map layer by utilizing the Layer Menu on the right hand side of your map screen. This menu opens when a layer is selected and contains the following tabs:
From the layer style menu we can modify how the layer will appear on the map
From the layer label menu we can add text descriptors the map layer.
The “Labels” dropdown menu allow you to add a text descriptor next to a layer item. Only one item may be selected in the label dropdown.
The “Tooltip” is a floating box that appears when hovering over a layer element. We can add/remove items displayed in the tooltip by selecting in the “Tooltips” menu.
The Condition Builder menu allows you to edit the data included in your layer. The most important item is to select the Table Name using the drop down menu that you wish to show on the map. This can include point items like Customers or Facilities or transportation arcs like OptimizationFlowSummary.
Within the Condition Builder you can use conditions to filter the table further to a subset of the data in the table. The filter syntax is similar to the syntax used when creating scenarios.


---
## Frogger Pond Community
**URL:** https://optilogic.com/resources/help-center/docs/frogger-pond-community

We love for our users to connect, keep up to date, learn from and share with other Cosmic Frog users & experts through the Frogger Pond Community! If you have an Optilogic account (see this page on how to create your free account if you do not have one yet), you can use that same account to log into the Frogger Pond Community.
Here, we will describe what the Frogger Pond Community consists of, how to interact with, search, sort, and contribute to Topics, and how to manage your account. Recommended reads for new users are included in the last section too.
1. Frogger Pond Community Homepage
When you login to the Frogger Pond Community, the homepage you see will look similar to the screenshot below:
Clicking on the Frogger Pond Community button at the left top of the screen will take you back to this homepage if you are on any other page within the community.
You can choose how the Topics list is shown to you: you will see all 5 categories if you click on Categories and you can then choose the one you want to explore. The topics will be ordered by most active posts if you click on Top; if you click on Latest, they will be ordered by most recent activity. By default, the Top option is used, which you can also see as the one highlighted in blue in box 5 and is described in bullet 5 further below.
There are 5 categories of Topics in the Frogger Pond Community:
Product Feedback – we love to hear your feedback on the software here, both good and bad! Feature requests can be posted here too.
Modeling Best Practices – if you are new to supply chain design, you can learn from experienced designers and ask your questions here. If you are very experienced and can share your insights on how to model certain aspects of a supply chain, please do so here!
Marketplace – have a look here if you are looking for the next step in your supply chain design career. Or, in case you have an interesting opportunity to offer, you can post that here too. You can create new topics in the Marketplace category if you are part of the Professional user group.
Tips and Tricks – share your best shortcuts, videos, and insights on how you use Cosmic Frog, Atlas and the overall Optilogic platform here.
General – for questions or posts that do not fit into the other 4 categories. You are also encouraged to link to interesting articles or posts in this category.
At the right top there are a few buttons as follows:
The arrow button takes you to the Optilogic platform.
The magnifying glass button opens a search box where you can type your search term to find topics of interest. You can also click on the icon on the right side in the search box that takes you to an advanced search form where you can for example filter for certain tags, a certain date range, etc.
The button with 3 horizontal bars opens a menu where you can quickly go to different parts of the Frogger Pond Community. We will discuss the options here in section “4. Options from the Menu” further below.
The 4th button is your p
…（省略）


---
## Full Truckload Costing Utility
**URL:** https://optilogic.com/resources/help-center/docs/full-truckload-costing-utility

The Full Truckload Costing utility solves the common problem of missing transportation cost data when building supply chain models. Rather than requiring users to manually research rates for every lane, this workflow automatically derives costs from a company's existing shipment history. The utility expects two input tables: a lanes-to-cost table containing the origin-destination pairs that need pricing, and an optional historical shipments table containing preprocessed cost data. After running the utility, users receive a fully costed lanes table with confidence levels for each estimate.
Each combination of (origin_id, destination_id, mode, product, cost_type) must be unique
Historical data must be preprocessed: outliers removed, costs aggregated to one value per unique lane
No NULL values allowed in join columns
Output Description
The utility produces an output table containing all lanes from the input with the following additional columns populated:
Costing Pipeline
The utility processes lanes through a sequential pipeline, with each step only processing lanes that still have NULL costs:
Validation - Verifies input data meets all requirements
Copy & Enrich - Creates working copies and adds distance bands and DAT regions
Exact Match - Matches on (origin_id, destination_id, mode, product, cost_type) - Confidence: Very High
Approximate Match - Progressive geographic relaxation:
Full Postal Code Match - Confidence: High
ZIP-3 Match - Confidence: Med
State Match - Confidence: Med-Low
DAT Region Match - Confidence: Low
Fallback Costing - For lanes without historical matches:
Segmented average by cost_type/distance_band/mode - Confidence: Med
DAT Region benchmark rates - Confidence: Med-Low
Overall average $/mile - Confidence: Low
Default rate ($1.60/mile) - Confidence: Very Low
Copy to Output - Writes final results to output table
Tips & Notes
If no historical shipments table is provided, the utility will skip exact and approximate matching and only apply fallback costing using default benchmark rates.
The workflow is fully deterministic - given the same inputs, it will always produce the same outputs.
Original input tables are never modified. The utility creates working copies for all processing.
For best results, ensure your historical shipments table has good coverage of the geographic regions and product types in your lanes to cost.
Lanes with "Very Low" confidence (default rate) indicate gaps in your historical data. Consider collecting actual rate quotes for these lanes.
The DAT Region mapping covers the continental US, Canada, and Mexico. US states are mapped to 10 freight regions (Z0-Z9) based on typical freight market patterns.
Distance bands help match lanes with similar characteristics: <25 miles (short haul), 25-250 miles (regional), >250 miles (long haul).
The Full Truckload Costing utility solves the common problem of missing transportation cost data when building supply chain models. Rather than requiring users to manually research ra
…（省略）


---
## Generating App and API Keys
**URL:** https://optilogic.com/resources/help-center/docs/generating-app-and-api-keys

There are two methods for establishing a secure connection to the Optilogic platform:
An App key is a code that can be linked to your account and will not expire. API keys are generated with code and only last for one hour before they expire. Both keys can be useful depending on how you wish to access the platform. Without either an App Key or an API Key you will not be able to run any API endpoints.
Login to the Optilogic website and click on your name in the top right corner, then click on “Account.”
Click on the “App Key Management” tab from their name your app key and click on the “Create Key” button.
At this point you may copy your App Key to be used for authentication purposes.
To generate an API key you will need to leverage python and the following instructions.
In a python file copy and paste this code and replace the USERNAME and PASSWORD with your own. Make sure to remove both sets of {{}} curly brackets so that it looks like this: headers = {‘X-USER-ID’: ‘CMorrell’ }
import requests
url = ‘https://api.optilogic.app/v0/r…’
headers = {
‘X-USER-ID’: ‘{{user_id}}’,
‘X-USER-PASSWORD’: ‘{{user_password}}’
}
response = requests.request(‘POST’, url, headers=headers)
print(response.text)
The result of this code will be an API key that can be used for authentication.
There are two methods for establishing a secure connection to the Optilogic platform:
An App key is a code that can be linked to your account and will not expire. API keys are generated with code and only last for one hour before they expire. Both keys can be useful depending on how you wish to access the platform. Without either an App Key or an API Key you will not be able to run any API endpoints.
Login to the Optilogic website and click on your name in the top right corner, then click on “Account.”
Click on the “App Key Management” tab from their name your app key and click on the “Create Key” button.
At this point you may copy your App Key to be used for authentication purposes.
To generate an API key you will need to leverage python and the following instructions.
In a python file copy and paste this code and replace the USERNAME and PASSWORD with your own. Make sure to remove both sets of {{}} curly brackets so that it looks like this: headers = {‘X-USER-ID’: ‘CMorrell’ }
import requests
url = ‘https://api.optilogic.app/v0/r…’
headers = {
‘X-USER-ID’: ‘{{user_id}}’,
‘X-USER-PASSWORD’: ‘{{user_password}}’
}
response = requests.request(‘POST’, url, headers=headers)
print(response.text)
The result of this code will be an API key that can be used for authentication.


---
## Geo Providers for Geocoding and Distance and Time Calculations
**URL:** https://optilogic.com/resources/help-center/docs/geo-providers-for-geocoding-and-distance-and-time-calculations

This documentation covers which geo providers one can use with Cosmic Frog, and how they can be used for geocoding and distance and time calculations.
Currently, there are 5 geo providers that can be used for geocoding locations in Cosmic Frog: MapBox, Bing, Google, PTV, and PC*Miler. MapBox is the default provider and comes free of cost with Cosmic Frog. To use any of the other 4 providers, you will need to obtain a license key from the company and add this to Cosmic Frog through your Account. The steps to do so are described in this help article “Using Alternate Geocoding Providers”.
Different geocoding providers may specialize in different geographies; refer to your provider for guidelines.
Geocoding a location (e.g. a customer, facility or supplier) means finding the latitude and longitude for it. Once a location is geocoded it can be shown on a map in the correct location which helps with visualizing the network itself and building a visual story using model inputs and outputs that are shown on maps.
To geocode a location:
For costs and capacities to be calculated correctly, it may be needed to add transport distances and transport times to Cosmic Frog models. There are defaults that will be used if nothing is entered into the model, or users can populate these fields, either themselves or by using a Distance Lookup Utility. Here the tables where distances and times can be entered, what happens if nothing has been entered, and how users can utilize the Distance Lookup Utility will be explained.
There are multiple Cosmic Frog input tables that have input fields related to Transport Distance, and Transport Time, including Speed which can also be used to calculate transport time from a Transport Distance (time = distance / speed). These all have their own accompanying UOM (unit of measure) field. Here is an overview of the tables which contain Distance, Time and/or Speed fields:
For Optimization (Neo), this is the order of precedence that is applied when multiple tables and fields are used:
For Transportation (Hopper) models, this is the order of precedence when multiple tables and fields are being used:
To populate these input tables and their pertinent fields, user has following options:
Cosmic Frog users can find multiple handy utilities in the Utilities section of Cosmic Frog - here we will cover the Distance Lookup utility. This utility looks up transportation distances and times for origin-destination pairs and populates the Transit Matrix table. As Geo Providers, Bing, PC Miler and Azure can be used if the user has a license key for these. In addition, there is a free PC Miler-UltraFast option which can look up accurate road distances within the EU and North America without needing a license key. This is also a very fast way to lookup distances. A new free provider OLRouting has been added. This provider leverages valhalla, an open source routing engine for OpenStreetMap. It has global coverage and performs the lookups very fast as well.
…（省略）


---
## Geocoding Accuracy Issues
**URL:** https://optilogic.com/resources/help-center/docs/geocoding-accuracy-issues

When running geocoding through the default Mapbox provider, all of the available location data from the Customers, Facilities and Suppliers table will be used to try and determine the latitude and longitude coordinates. Mapbox will use all of these components and perform the best mapping possible and will return a latitude / longitude coordinate along with a confidence score. By default, Cosmic Frog will only accept scores with a confidence score of 100. You can optionally turn this option off and the top confidence score will then be returned by Mapbox.
More information on how Mapbox calculates latitude and longitude coordinates can be found here: Mapbox Geocoding Documentation.
If you’d like to use an alternate provider instead of Mapbox, setup instructions can be found here: Using Alternate Geocoding Providers.
When running geocoding through the default Mapbox provider, all of the available location data from the Customers, Facilities and Suppliers table will be used to try and determine the latitude and longitude coordinates. Mapbox will use all of these components and perform the best mapping possible and will return a latitude / longitude coordinate along with a confidence score. By default, Cosmic Frog will only accept scores with a confidence score of 100. You can optionally turn this option off and the top confidence score will then be returned by Mapbox.
More information on how Mapbox calculates latitude and longitude coordinates can be found here: Mapbox Geocoding Documentation.
If you’d like to use an alternate provider instead of Mapbox, setup instructions can be found here: Using Alternate Geocoding Providers.


---
## Getting Started with Ada & Agentic AI
**URL:** https://optilogic.com/resources/help-center/docs/getting-started-with-ada-agentic-ai

Ada is Optilogic’s next-generation agentic AI, enabling supply chain teams to work faster and with greater confidence across the full modeling lifecycle — from raw data preparation to optimization runs to executive reporting — all through natural language interactions.
Unlike traditional UI chat assistants, it deploys purpose-built agents that can pursue multi-step goals, use specialized skills, maintain conversational context, and coordinate with each other to complete workflows that previously required significant manual effort. This dramatically reduces the time required to move from raw data to recommendations.
As a core part of Optilogic’s Next Generation User InterfacePlatform, Ada provides a more intelligent and conversational approach to supply chain design work.
Ada is named after Ada Lovelace, widely regarded as the world’s first computer programmer and one of the earliest visionaries to recognize the potential of computational systems beyond pure calculation. The name reflects Optilogic’s goal of building intelligent systems that help people solve complex problems through collaboration between human expertise and advanced computing.
Ada is your AI-first supply chain modeling partner, designed specifically for the Optilogic platform. Through a conversational interface, Ada helps users build, validate, analyze, and improve supply chain models.
You can think of Ada as a chat agent like for example Claude and ChatGPT. But, unlike general-purpose AI chat tools, Ada is trained around supply chain modelling workflows and has access to Optilogic-specific tools, applications, databases, schemas, and platform capabilities.
Today, Ada includes three specialized AI Agents:
The Select the AI Agent part of the Create Your First Prompt section further below includes guidance on which agent to use for what type of question/task.
For a deeper technical explanation of how AI agents, tools, and skills work together, see the AI Agents: Architecture and Components help center article.
Teams commonly use Ada for:
Ada works best for:
Ada is less suited for:
Ada is best thought of as:
Ada does not automatically understand:
The clearer the context you provide, the better the results typically become.
Ada can connect to:
Ada operates entirely within the Optilogic platform and your connected databases. It does not access the internet or any data or systems outside of the Optilogic environment. It does not send your data to third parties beyond what is required by the underlying GPT family model API (see AI Data Security & Privacy).
Ada may:
To start using Ada, log into the next generation Optilogic platform at https://ai.optilogic.app or navigate there by clicking on the Ada icon in the navigation sidebar while on the current Optilogic platform (https://optilogic.app):
Besides this documentation, you can also get a guided tour on how to use Ada from within the platform itself. In the sidebar on the left, click on the Apps Launcher icon:
Then search for “Start Ad
…（省略）


---
## Getting Started with Analytics
**URL:** https://optilogic.com/resources/help-center/docs/getting-started-with-analytics

Once you have run a model, you can visualize your results using the Analytics tab.
In Analytics, a dashboard is a collection of visualizations. Visualizations can take on many forms, such as charts, tables or maps.
In Cosmic Frog, there are default dashboards available to help you analyze your model results.
The default dashboards highlight some common analytics and metrics. They are designed to be interacted with through a set of filters.
We can hover over visualization elements to get more information. This floating card of information is called a “Tooltip”.
We can customize existing dashboards to fit our needs. For more information see Editing Dashboards and Visualizations.
Once you have run a model, you can visualize your results using the Analytics tab.
In Analytics, a dashboard is a collection of visualizations. Visualizations can take on many forms, such as charts, tables or maps.
In Cosmic Frog, there are default dashboards available to help you analyze your model results.
The default dashboards highlight some common analytics and metrics. They are designed to be interacted with through a set of filters.
We can hover over visualization elements to get more information. This floating card of information is called a “Tooltip”.
We can customize existing dashboards to fit our needs. For more information see Editing Dashboards and Visualizations.


---
## Getting Started with Cosmic Frog
**URL:** https://optilogic.com/resources/help-center/docs/getting-started-with-cosmic-frog

This video guides you though creating your free account and the features of the Optilogic Cosmic Frog supply chain design platform.
If you are running into issues receiving your account confirmation email, please see the troubleshooting article linked here.
This video guides you though creating your free account and the features of the Optilogic Cosmic Frog supply chain design platform.
If you are running into issues receiving your account confirmation email, please see the troubleshooting article linked here.


---
## Getting Started with Cosmic Frog for Excel Applications
**URL:** https://optilogic.com/resources/help-center/docs/getting-started-with-cosmic-frog-for-excel-applications

Cosmic Frog for Excel Applications provide alternative interfaces for specific use cases as companion applications to the full Cosmic Frog Supply chain design product. For example, they can be used to access a subset of the Cosmic Frog functionality in a simplified manner or provide specific users who are not experienced in working with Cosmic Frog models access to a subset of inputs and/or outputs of a full-blown Cosmic Frog model that are relevant to their position.
Several example use cases are:
It is recommended to review the Cosmic Frog for Excel App Builder before diving into this documentation, as basic applications can quickly and easily be built with it rather than having to edit/write code, which is what will be explained in this help article. The Cosmic Frog for Excel App Builder can be found in the Resource Library and is also explained in the “Getting Started with the Cosmic Frog for Excel App Builder” help article.
Here we will discuss how one can set up and use a Cosmic Frog for Excel Application, which will include steps that use VBA (Visual Basic for Applications) in Excel and scripting using the programming language Python. This may sound daunting at first if you have little or no experience using these. However, by following along with this resource and the ones referenced in this document, most users will be able to set up their own App in about a day or 2 by copy-pasting from these resources and updating the parts that are specific to their use case. Generative AI engines like Chat GPT and perplexity can be very helpful as well to get a start on VBA and Python code. Cosmic Frog functionality will not be explained much in this documentation, the assumption is that users are familiar with the basics of building, running, and analyzing outputs of Cosmic Frog models.
In this documentation we are mainly following along with the Greenfield App that is part of the Resource Library resource “Building a Cosmic Frog for Excel Application”. Once we have gone through this Greenfield app in detail, we will discuss how other common functionality that the Greenfield App does not use can be added to your own Apps.
There are several Cosmic Frog for Excel Applications that have been developed by Optilogic available in the Resource Library. Links to these and a short description of each of them can be found in the penultimate section “Apps Available in the Resource Library” of this documentation.
Throughout the documentation links to other resources are included; in the last section “List of All Resources” a complete list of all resources mentioned is provided.
The following screenshot shows at a high-level what happens when a typical Cosmic Frog for Excel App is used. The left side represents what happens in Excel, and on the right side what happens on the Optilogic platform.
A typical Cosmic Frog for Excel Application will contain at least several worksheets that each serve a specific purpose. As mentioned before, we are using the MicroAPP_Gr
…（省略）


---
## Getting Started with Cyclo (Multi Echelon Inventory Optimization)
**URL:** https://optilogic.com/resources/help-center/docs/getting-started-with-cyclo-multi-echelon-inventory-optimization

Cyclo is Optilogic’s new Multi Echelon Inventory Optimization (MEIO) engine within Cosmic Frog. It helps supply chain teams determine where safety stock should be held across a network, how much is needed at each stage, and how service levels impact total safety stock cost and responsiveness.
If you just want to get going with Cyclo as quick as possible, follow these steps:
Multi Echelon Inventory Optimization (MEIO) is a planning approach used to optimize safety stock across an entire supply chain network.
Cyclo, the MEIO engine, is designed to optimize safety stock placement across multi-stage supply chains that may include suppliers, manufacturing plants, distribution centers, and customer-facing locations. Instead of optimizing each node independently, Cyclo evaluates the entire network simultaneously so organizations can reduce total safety stock while maintaining desired service levels.
Cyclo uses a Guaranteed Service Model (GSM) approach to optimize service-time relationships between facilities and derive recommended safety stock levels.
Cyclo helps organizations answer key supply chain questions such as:
By optimizing safety stock placement across the entire network, Cyclo can help organizations:
Cyclo is especially valuable for:
Both Cyclo and Dendro support inventory optimization workflows in Cosmic Frog, but they are designed for different planning problems.
In practice both can be used together:
Cyclo uses a Guaranteed Service Model (GSM) approach. Rather than directly optimizing safety stock quantities, Cyclo optimizes service-time commitments between facilities. Those service-time decisions are then translated into safety stock requirements.
Represents your risk tolerance – balancing the cost of holding extra buffer inventory against the risk and cost of lost sales. This is a user input. Two risk measures are available:
Service Type 1 is a stricter measure than Type 2 and will in most cases lead to more safety stock.
Time a facility expects upstream suppliers to deliver material. This is a decision variable in the optimization
Time a facility needs to replenish – typically transport time from the upstream location to the facility and/or production/processing time at the facility. These are model inputs.
Time a facility promises to deliver to downstream customers. This is a decision variable in the optimization.
The effective time window over which demand uncertainty accumulates.
In a Guaranteed Service Model (GSM), each facility commits to serving downstream nodes within a defined service time. The effective exposure to uncertainty is the Net Replenishment Time (NRT):
NRT = Incoming Service Time + Fixed Lead Times − Outgoing Service Time
As NRT increases, more uncertainty accumulates and more safety stock is typically required.
Cyclo evaluates many combinations of incoming and outgoing service times across the network to find the lowest total safety stock holding cost, while reaching the target service level. The optimization is not
…（省略）


---
## DataStar Overview
**URL:** https://optilogic.com/resources/help-center/docs/getting-started-with-datastar

DataStar is Optilogic’s new AI-powered data product designed to help supply chain teams build and update models & scenarios and power apps faster & easier than ever before. It enables users to create flexible, accessible, and repeatable workflows with zero learning curve—combining drag-and-drop simplicity, natural language AI, and deep supply chain context.
Today, up to an estimated 80% of a modeler's time is spent on data—connecting, cleaning, transforming, validating, and integrating it to build or refresh models. DataStar drastically shrinks that time, enabling teams to:
Answer more questions faster
Unlock repeatable value across business review
Focus on strategic decisions, not data wrangling
The 2 main goals of DataStar are 1) ease of use, and 2) effortless collaboration, these are achieved by:
Providing AI-powered, no-code automation with deep supply chain context
Supporting drag-and-drop workflows, natural language commands, and advanced scripting (SQL/Python)
Full integration into the Optilogic platform: users can prep data, trigger model & scenario runs, and push insights to apps or dashboards
Enabling scalable, collaborative, cloud-native modeling for repeatable decision-making at speed
In this documentation, we will start with a high-level overview of the DataStar building blocks. Next, creating projects and data connections will be covered before diving into the details of adding tasks and chaining them together into macros, which can then be run to accomplish the data goals of your project.
Before diving into more details in later sections, this section will describe the main building blocks of DataStar, which include Data Connections, Projects, Macros, and Tasks.
Data Connections
Since DataStar is all about working with data, Data Connections are an important part of DataStar. These enable users to quickly connect to and pull in data from a range of data sources. Data Connections in DataStar:
Are global to the DataStar application – meaning each project within DataStar can use any of the data sources that have been set up as Data Connections.
Can also be set up from within a DataStar project – they then become available for use in other DataStar projects too.
Can be of the following types currently:
Postgres – an open-source relational database management system that supports both SQL and JSON querying
CSV Files – files containing data in the comma separated values format, which can be created by and opened in Excel
Cosmic Frog Models – a Cosmic Frog model which is a Postgres database using a specific data schema called Anura. Often the projects in DataStar will populate Cosmic Frog model input tables to build complete models that are ready to be run by one of the Cosmic Frog engines and/or read in Cosmic Frog output tables for output analysis
Excel – spreadsheet editor developed by Microsoft for Windows (beta version)
Connections to other common data resources such as MySQL, OneDrive, SAP, and Snowflake will become available as bui
…（省略）


---
## Getting Started with DataStar: Application Overview
**URL:** https://optilogic.com/resources/help-center/docs/getting-started-with-datastar-application-overview

Please watch this 5-minute video for an overview of DataStar, Optilogic’s new AI-powered data application designed to help supply chain teams build and update models & scenarios and power apps faster & easier than ever before!
For detailed DataStar documentation, please see Navigating DataStar on the Help Center.
Please watch this 5-minute video for an overview of DataStar, Optilogic’s new AI-powered data application designed to help supply chain teams build and update models & scenarios and power apps faster & easier than ever before!
For detailed DataStar documentation, please see Navigating DataStar on the Help Center.


---
## Getting Started with Dendro
**URL:** https://optilogic.com/resources/help-center/docs/getting-started-with-dendro

Dendro is Optilogic's simulation-optimization engine. A prime use case for Dendro is inventory policy optimization.
Simulation-optimization is a method in which simulation is leveraged to intelligently explore alternative configurations of a system. Dendro accomplishes this data-driven search by layering a genetic algorithm on top of simulation; simulation is the core of a Dendro model. Before a Dendro study can begin, a simulation model (run with the Throg engine) must be built, verified, and validated.
Simulation-optimization enables us to ask and answer questions that we cannot address in traditional network optimization or simulation alone.
In this article, we will explore:
The modeling methods of network optimization (Neo), discrete event simulation (Throg), and simulation-optimization (Dendro) address different supply chain design use cases.
A prime use case for Dendro is inventory policy optimization: right-sizing inventory levels by changing inventory policy parameters (reorder points, reorder quantities, etc.) with the goal of balancing cost and service. Dendro's foundation in simulation minimizes the abstraction of cost accounting, service metrics, and the business rules surrounding inventory management. Dendro provides actionable inventory policy recommendations and data-driven evidence to support those changes.
Primary Focus: Determining where inventory should be positioned across the network.
Use Case: Network design decisions that include high-level inventory considerations -- such as stocking locations, target turns, and working capital trade-offs.
How It Handles Inventory:
Primary Focus: Testing and observing how specific inventory policies perform under realistic operational dynamics.
Use Case: Evaluate inventory control logic (e.g., reorder point, order quantity, order-up-to level) in a time-based simulation environment.
How It Handles Inventory:
Primary Focus: Finding better inventory policies that balance cost and service, combining Throg's simulation accuracy with an optimization engine.
Use Case: Adjust inventory policy parameters (e.g., reorder point, reorder quantity, policy type) to find configurations that deliver the best cost-service trade-offs.
How It Handles Inventory:
While this comparison highlights how each engine contributes to inventory management decisions, the specific use case covered in this article is inventory policy optimization -- using Dendro to balance total inventory carrying cost and network-level customer service (measured as quantity fill rate).
That said, Dendro's capabilities extend far beyond inventory. The same framework of input factors, output factors, and utility functions can be applied to a wide range of optimization problems -- and its utility components are not limited to just cost and service. Dendro can optimize for any measurable performance metric that matters to your business.
As stated above, a Dendro study cannot be initiated without first establishing a Throg simulation model; a 
…（省略）


---
## Getting Started with Hopper
**URL:** https://optilogic.com/resources/help-center/docs/getting-started-with-hopper

Hopper is the Transportation Optimization algorithm within Cosmic Frog. It designs optimal multi-stop routes to deliver/pickup a given set of shipments to/from customer locations at the lowest cost. Fleet sizing and balancing weekly demand can be achieved with Hopper too. Example business questions Hopper can answer are:
Hopper’s transportation optimization capabilities can be used in combination with network design to test out what a new network design means in terms of the last-mile delivery configuration. For example, questions that can be looked at are:
With ever increasing transportation costs, getting the last-mile delivery part of your supply chain right can make a big impact on the overall supply chain costs!
It is recommended to watch this short Getting Started with Hopper video before diving into the details of this documentation. The video gives a nice, concise overview of the basic inputs, process, and outputs of a Hopper model.
In this documentation we will first cover some general Cosmic Frog functionality that is used extensively in Hopper, next we go through how to build a Hopper model which discusses required and optional inputs, how to run a Hopper model is explained, Hopper outputs in tables, on maps and analytics are covered as well, and finally references to a few additional Hopper resources are listed. Note that additional more advanced Hopper features are covered in separate articles:
To not make this document too repetitive we will cover some general Cosmic Frog functionality here that applies to all Cosmic Frog technologies and is used extensively for Hopper too.
To only show tables and fields in them that can be used by the Hopper transportation optimization algorithm, disable all icons except the 4th (“Transportation”) in the Technologies Selector from the toolbar at the top in Cosmic Frog. This will hide any tables and fields that are not used by Hopper and therefore simplifies the user interface:
Many Hopper related fields in the input and output tables will be discussed in this document. Keep in mind however that a lot of this information can also be found in the tooltips that are shown when you hover over the column name in a table, see following screenshot for an example. The column name, technology/technologies that use this field, a description of how this field is used by those algorithm(s), its default value, and whether it is part of the table’s primary key are listed in the tooltip.
There are a lot of fields with names that end in “…UOM” throughout the input tables. How they work will be explained here so that individual UOM fields across the tables do not need to be explained further in this documentation as they all work similarly. These UOM fields are unit of measure fields and often appear to the immediate right of the field that they apply to, like for example Distance Cost and Distance Cost UOM in the screenshot above. In these UOM fields you can type the Symbol of a unit of measure that is of the requi
…（省略）


---
## Getting Started with Intelligent Greenfield Analysis
**URL:** https://optilogic.com/resources/help-center/docs/getting-started-with-intelligent-greenfield-analysis

Greenfield analysis (GF) is a method for determining the optimal location of facilities in a supply chain network. The Greenfield engine in Cosmic Frog is called Triad and this name comes from the oldest known species of frogs – Triadobatrachus. You can think of it as the starting point for the evolution of all frogs, and it serves as a great starting point for modeling projects too! We can use Triad to identify 3 key parameters: 
GF is a great starting point for network design—it solves quickly and can reduce the number of candidate site locations in complicated design problems. However, a standard GF requires some assumptions to solve (e.g. single time period, single product). As a result, the output of a Triad model is best suited as initial information for building a more robust Cosmic Frog optimization (Neo) or simulation (Throg) model.
You can run GF in any Cosmic Frog model. Running a GF model only requires two input tables to be populated: 
A third important table for running GF is the Greenfield Settings table in the Functional Tables section of the input tables. We call our GF approach “Intelligent Greenfield” because of the different parameters available by configuring this settings table. The Greenfield Settings table is always populated with defaults and users can change these as needed. See the Greenfield Setting Explained help article for an explanation of the fields in this table.
A greenfield analysis starts with clicking the “Run” button at the right top of the Cosmic Frog application, just like a Neo or Throg model.
After clicking on the Run button, the Run screen comes up:
Besides making changes to values in the Customers and/or Customer Demand tables, GF scenarios often make changes to 1 or multiple settings on the Greenfield Settings table. The next screenshot shows an example of this:
To improve the solve speed of a Triad model, we can use customer clustering. Customer clustering reduces the size of the supply chain by grouping customers within a given geometric range into a single customer. We can set the clustering radius (in miles) in the Greenfield Settings table in the Customer Cluster Radius column.
Clustering is optional, and leaving this column blank is the same as turning off clustering.
While grouping customers can significantly improve the run time of the model, clustering may result in a loss of optimality. However, Greenfield is typically used as a starting point for a future Neo optimization model, so small losses in optimality at this phase are typically manageable.
Greenfield analysis (GF) is a method for determining the optimal location of facilities in a supply chain network. The Greenfield engine in Cosmic Frog is called Triad and this name comes from the oldest known species of frogs – Triadobatrachus. You can think of it as the starting point for the evolution of all frogs, and it serves as a great starting point for modeling projects too! We can use Triad to identify 3 key parameters: 
GF is a great st
…（省略）


---
## Getting Started with Leapfrog AI
**URL:** https://optilogic.com/resources/help-center/docs/getting-started-with-leapfrog-ai

Leapfrog helps Cosmic Frog users explore and use their model data via natural language. View data, make changes, create & run scenarios, analyze outputs, learn all about the Anura schema that underlies Cosmic Frog models, and a whole lot more!
Leapfrog combines an extensive knowledge of PostgreSQL with the complete knowledge of Optilogic’s Anura data schema, and all the natural language capabilities of today’s advanced general purpose LLMs.
For a high-level overview and short video introducing Leapfrog, please see the Leapfrog landing page on Optilogic’s website.
In this documentation, we will first get users oriented on where to find Leapfrog and how to interact with it. In the section after, Leapfrog’s capabilities will be listed out with examples of each. Next, the Tips & Tricks section will give users helpful pointers so they can get the most out of Leapfrog. Finally, we will step through the process of building, running, and analyzing a Cosmic Frog model start to finish by only using Leapfrog!
Dive in if you’re ready to take the leap!
Start using Leapfrog by opening the module within Cosmic Frog:
Once the Leapfrog module is open, users’ screens will look similar to the following screenshot:
The example prompts when using the Anura Help LLM are shown here:
When first starting to use Leapfrog, users will also see the Privacy and Data Security statement, which reads as follows:
“Leapfrog AI Training: Optilogic does not use your model data to train Leapfrog. We do collect and store conversational data so it can be accessed again by the user, as well as to understand usage patterns and areas of strength/weakness for the LLM. Included in this data: natural language input prompts, text and SQL responses, as well as feedback from users. This information is maintained by Optilogic, not shared with third parties, and all of the conversation data is subject to the data security and privacy terms of the Optilogic platform.”
This message will stay visible within Leapfrog whenever it is being used, unless user clicks on the grey cross button on the right to close the message. Once closed, the message will not be shown again while using Leapfrog.
Conversation history is stored on the platform at the user level - not in the model database - so it does not get shared when a model is shared. Note that if you are working in a Team rather than in your My Account (see documentation on Teams on the Optilogic platform here), the Leapfrog conversations you are creating will be available to the other team members when they are working with the same model.
As mentioned in the previous section, Leapfrog currently makes use of 2 large language models (LLMs): Text2SQL and Anura Help (also referred to as Anura Aficionado or A2). They will be explained in some more detail here. There is also an appendix to this documentation where for a few example personas Leapfrog questions and responses are listed, which showcases how some users may predominantly use one model, while o
…（省略）


---
## Getting Started with Maps
**URL:** https://optilogic.com/resources/help-center/docs/getting-started-with-maps

Showing supply chains on maps is a great way to visualize them, to understand differences between scenarios, and to show how they evolve over time. Cosmic Frog offers users many configuration options to customize maps to their exact needs and compare them side-by-side. In this documentation we will cover how to create and configure maps in Cosmic Frog.
Maps Basics
In Cosmic Frog, a map represents a single geographic visualization composed of different layers. A layer is an individual supply chain element such as a customer, product flow, or facility. To show locations on a map, these need to exist in the master tables (e.g. Customers, Facilities, and Suppliers) and they need to have been geocoded (see also the How to Geocode Locations section in this help center article). Flow based layers are based on output tables, such as the OptimizationFlowSummary or SimulationFlowSummary and to draw these, the model needs to have been run so outputs are present in these output tables.
Maps can be accessed through the Maps module in Cosmic Frog:
Click on the Module menu at the top left in Cosmic Frog.
Choose Maps from the drop-down menu.
The Maps module opens and shows the first map in the Maps list; this will be the default pre-configured “Supply Chain” map for maps the user created and most models copied from the Resource Library:
The list of pre-configured maps and their layers is located on the left-hand side of the map, the next screenshot will cover this list in more detail.
The pre-configured Supply Chain map is showing by default when first opening the Maps module. Here, Customers are shown as small green circles (there are around 1.3k customers in this model), 7 Distribution Centers (DCs) are shown using a blue truck icon, 2 Factories are depicted with a blue building icon, and 2 Ports with an orange ship icon.
At the right top of a map, user will find following 4 map controls, from top to bottom:
Enter fullscreen: clicking on this icon will maximize the map on the whole computer screen. Clicking on this icon again, which at that point will have the arrows pointing inwards, will exit fullscreen mode.
Zoom in: clicking on this icon will zoom the map in. The map area will be used to show a smaller part of the world, and the features will become more detailed (e.g. smaller roads and smaller localities will become visible) as user zooms in more. Note that users can also zoom in using the scroll button on a mouse or putting two fingers on a mouse trackpad and moving them away from each other.
Zoom out: clicking on this icon will zoom the map out. The map area will be used to show a larger part of the world and features will become less detailed. Note that users can also zoom out using the scroll button on a mouse or putting two fingers on a mouse trackpad and moving them closer to each other.
Reset bearing to north: when working with a map, they may get moved so that the orientation is not the standard of top being north, right being east, etc. Click on 
…（省略）


---
## Getting Started with Optilogic Teams
**URL:** https://optilogic.com/resources/help-center/docs/getting-started-with-optilogic-teams

Teams is an exciting new feature set designed to enhance collaboration within Supply Chain Design, enabling companies to foster a more connected and efficient working environment. With Teams, users can join a shared workspace where all team members have seamless access to collective models and files. This ensures that every piece of work remains synchronized, providing a single source of truth for your data. When one team member updates a file, those changes instantly reflect for all other members, eliminating inconsistencies and ensuring that everyone stays aligned.
Beyond simply improving collaboration, Teams offers a structured and flexible way to organize your projects. Instead of keeping all your files and models confined to a personal account, you can now create distinct teams tailored to different projects, departments, or business functions. This means greater clarity and easier navigation between workspaces, ensuring that the right content is always at your fingertips.
Consider the possibilities:
Teams introduces a more intuitive and structured way to collaborate, organize, and access your work—ensuring that your team members always have the latest updates and a streamlined experience. Get started today and transform the way you work together!
This documentation contains a high-level overview of the Teams feature set, details the steps to get started, gives examples of how Teams can be structured, and covers best practices. More detailed documentation for Organization Administrators and Teams Users is available in the following help center articles:
The diagram below highlights the main building blocks of the Teams feature set:
At a high-level, these are the steps to start using the Teams feature set:
Here follow 5 examples of how teams can be structured, including an example for each and an explanation of why such a setup works well.
Please keep following best practices in mind to ensure optimal use of the Teams feature set:
Once you have set up your teams and added content, you are ready to start collaborating and unlocking the full potential of Teams within Optilogic!
Let us know if you need help along the way—our support team (support@optilogic.com) has your back.
Teams is an exciting new feature set designed to enhance collaboration within Supply Chain Design, enabling companies to foster a more connected and efficient working environment. With Teams, users can join a shared workspace where all team members have seamless access to collective models and files. This ensures that every piece of work remains synchronized, providing a single source of truth for your data. When one team member updates a file, those changes instantly reflect for all other members, eliminating inconsistencies and ensuring that everyone stays aligned.
Beyond simply improving collaboration, Teams offers a structured and flexible way to organize your projects. Instead of keeping all your files and models confined to a personal account, you can now create disti
…（省略）


---
## Getting Started with Scenarios
**URL:** https://optilogic.com/resources/help-center/docs/getting-started-with-scenarios

Scenarios let you rapidly explore "what-if" questions against an existing Cosmic Frog model. Define one or more data changes (scenario items), run the scenarios, then compare outputs - all without altering your baseline input data.
Follow these five steps to run your first scenario:
💡 Tip: Use Leapfrog (Cosmic Frog's AI assistant) to create scenarios and items from plain-language prompts - no manual configuration needed.
A scenario defines one or more input-table changes to apply before running a solve. Common examples include:
In the context of this documentation, we mean the following with scenario and scenario item:
In other words: a scenario without any scenario items uses all the data in the input tables as is (often called Baseline); most scenarios will contain 1 or more scenario items to test certain changes as compared to a baseline.
Open the Scenarios module from the Module menu. A freshly opened module looks like this:
The Scenario drop-down (top of module) provides quick access to common actions:
Each scenario is associated with one engine. To change it, select the scenario and use the radio buttons in the central panel:
📝 Note: Running with multiple technologies
You can solve the same scenario with more than one engine sequentially: assign the first technology → run → change technology → run again. Be aware that any scenario edits between runs may cause results to differ for subsequent runs.
💡 Tip: Dendro workflow
To optimize inventory policies with Dendro: first build and validate a Throg (simulation) scenario, then switch its technology to Dendro and run.
Right-click an existing scenario or the Scenarios folder and choose New Scenario, or use the New Scenario option from the Scenario drop-down menu. Enter a name when prompted:
Select the target scenario, then right-click → New Item (or use the Scenario drop-down). Name the item - its configuration panel opens automatically:
After selecting the table, specify the change in the Actions field. Intelli-type suggests column names as you type:
Once the column to change has been typed in, we can set its new value. In our example we want to set the value of the status column to Exclude:
Intelli-type also validates syntax. Incorrect quote style (need to use single quotes, not double quotes):
Unrecognized column name:
📝 Note: For full Actions syntax, see the Writing Syntax for Actions Help Center article.
By default, a scenario item's action applies to every record in the selected table. Add a filter to restrict which records are changed. Two methods are available:
If Named Filters exist for the selected table, you can apply one directly to the scenario item:
After selecting a filter, the Filter Grid Preview updates to show exactly which records will be affected:
💡 Tip: Why prefer Named Filters?
Named Filters are pre-validated - you have already confirmed they select the right records when creating the filter. The Condition Builder requires you to write syntax manually, which is more error-pr
…（省略）


---
## Getting Started with the Cosmic Frog for Excel App Builder
**URL:** https://optilogic.com/resources/help-center/docs/getting-started-with-the-cosmic-frog-for-excel-app-builder

To enable users to build basic Cosmic Frog for Excel Applications to interact directly with Cosmic Frog from within Excel without needing to write any code, Optilogic has developed the Cosmic Frog for Excel Application Builder (also referred to as App Builder in this documentation). In this App Builder, users can build their own workflows using common actions like creating a new model, connecting to an existing model, importing & exporting data, creating & running scenarios, and reviewing outputs. Once a workflow has been established, the App can be deployed so it can be shared with other users. These other users do not need to build the workflow of the App again, they can just use the App as is. In this documentation we will take a user through the steps of a complete workflow build, including App deployment.
You can download the Cosmic Frog for Excel – App Builder from the Resource Library. A video showing how the App Builder is used in a nutshell is included; this video is recommended viewing before reading further. After downloading the .zip file from the Resource Library and unzipping it on your local computer, you will find there are 2 folders included: 1) Cosmic_Frog_For_Excel_App_Builder, which contains the App Builder itself and this is what this documentation will focus on, and 2) Cosmic_Frog_For_Excel_Examples, which contains 3 examples of how the App Builder can be used. This documentation will not discuss these examples in detail; users are however encouraged to browse through them to get an idea of the types of workflows one can build with the App Builder.
The Cosmic_Frog_For_Excel_App_Builder folder contains 1 subfolder and 1 Macro-enabled Excel file (.xlsm):
When ready to start building your first own basic App, open the Cosmic_Frog_For_Excel_Builder_v1.xlsm file; the next section will describe the steps a user needs to take to start building.
When you open the Cosmic_Frog_For_Excel_App_Builder_v1.xlsm file in Excel, you will find there are 2 worksheets present in the workbook, Start and Workflow. The top of the Start worksheet looks like this:
Going to the Workflow worksheet and clicking on the Cosmic Frog tab in the ribbon, we can see the actions that are available to us to create our basic Cosmic Frog for Excel Applications:
We will now walk through building and deploying a simple App to illustrate the different Actions and their configurations. This workflow will: connect to a Greenfield model in my Optilogic account, add records to the Customer and CustomerDemand tables, create a new scenario with 2 new scenario items in it, run this new scenario, and then export the Greenfield Facility Summary output table from the Cosmic Frog model into a worksheet of the App. As a last step we will also deploy the App.
On the Workflow worksheet, we will start building the workflow by first connecting to an existing model in my Optilogic account:
The following screenshot shows the Help tab of the “Connect To Or Create Model Action”:
In the 
…（省略）


---
## Getting Started with the Explorer
**URL:** https://optilogic.com/resources/help-center/docs/getting-started-with-the-explorer

Users of the Optilogic platform can easily access all files they have in their Optilogic account and perform common tasks like opening, copying, and sharing them by using the built-in Explorer application. This application sits across all other applications on the Optilogic platform.
This documentation will walk users through how to access the Explorer, explain its folder and file structure, how to quickly find files of interest, and how to perform common actions.
By default, the Explorer is closed when users are logged into the Optilogic platform, they can open it at the top of the applications list:
Once the Explorer is open, your screen will look similar to the following screenshot:
This next screenshot shows the Explorer when it is open while the user is working inside the workspace of one of the teams they are part of, and not in their My Account workspace:
When a new user logs into their Optilogic account and opens the Explorer, they will find there are quite a few folders and files present in their account already. The next screenshot shows the expanded top-level folders:
As you may have noticed already, different file types can be recognized by the different icons to the left of the file’s name. The following table summarizes some of the common file types users may have in their accounts, shows the icon used for these in the Explorer, and indicates which application the file will be opened in when (left-)clicking on the file:
*When clicking on files of these types, the Lightning Editor application will be opened and a message stating that the file is potentially unsupported will be displayed. Users can click on a “Load Anyway” button to attempt to load the file in the Lightning Editor. If the user chooses to do so, the file will be loaded, but the result will usually be unintelligible for these file types.
Some file types can be opened in other applications on the Optilogic platform too. These options are available from the right-click context menus, see the “Right-click Context Menus” section further below.
Icons to the right of names of Cosmic Frog models in the Explorer indicate if the model is a shared one and if so, what type of access the user / team has to it. Hovering over these icons will show text describing the type of share too.
Learn more about sharing models and the details of read-write vs read-only access in the “Model Sharing & Backups for Multi-user Collaboration in Cosmic Frog” help center article.
While working on the Optilogic platform, additional files and folders can be created in / added to a user’s account. In this section we will discuss which applications create what types of files and where in the folder structure they can be found in the Explorer.
The Resource Library on the Optilogic platform contains example Cosmic Frog models, DataStar template projects, Cosmic Frog for Excel Apps, Python scripts, reference data, utilities, and additional tools to help make Optilogic platform users successful. Users can bro
…（省略）


---
## Getting Started with the Optilogic Risk Engine
**URL:** https://optilogic.com/resources/help-center/docs/getting-started-with-the-optilogic-risk-engine

The only constant is change. When building our supply chains, the “optimal” design doesn’t only mean lowest cost. What happens if (or perhaps when) a disruption occurs? Fragile, low-cost supply chains can end up costing more in the long run if they aren’t resilient to the dynamic nature of today’s world.
We believe that optimality includes resilience. That’s why every Cosmic Frog run includes a risk rating from our DART risk engine.
Every Cosmic Frog run outputs an Opti Risk score. The Opti Risk score is an aggregate measure of the overall supply chain risk. It includes the following sub-categories:
After running a model, you can find the Opti Risk score (as well as the scores for each of the sub-categories) in the output risk tables. The Opti Risk score can also be found in the OptimizationNetworkSummary table.
The overall Customer Risk score is an aggregation of each individual customer’s risk described in the OptimizationCustomerRiskMetrics or SimulationCustomerRiskMetrics tables. In each scenario, there is one risk score per customer per period.
Each customer risk score includes:
For each sub-category, the geographic risk score is also an aggregation of several risk factors:
Like the customer risk score, the overall facility risk score is an aggregation of risk across all facilities in your supply chain. In the FacilityRiskMetric tables, there is an individual risk score per facility per period.
The facility risk score includes:
The capacity risk has three sub-components:
The facility geographic risk has the same components as the customer geographic risk.
The supplier risk is calculated per supplier per period and includes:
Both the concentration and geographic risks include the same elements as described previously.
Network risk differs from the other risk scores in that it is not tied to a specific supply chain element. There is only one network risk score per scenario, and it includes:
The transport and import/export time risks are aggregated across individual origin/destination pairs for every product and transport mode. The individual risk scores can be found in the OptimizationFlowSummary table.
The stocking point count and supply make count risks are aggregations across every product and period. The individual risk scores can be found in the ProductRiskMetrics tables.
We can use our visualization tools to get a better sense of how risk varies across design scenarios.
The only constant is change. When building our supply chains, the “optimal” design doesn’t only mean lowest cost. What happens if (or perhaps when) a disruption occurs? Fragile, low-cost supply chains can end up costing more in the long run if they aren’t resilient to the dynamic nature of today’s world.
We believe that optimality includes resilience. That’s why every Cosmic Frog run includes a risk rating from our DART risk engine.
Every Cosmic Frog run outputs an Opti Risk score. The Opti Risk score is an aggregate measure of the overall supply chain risk. It includes t
…（省略）


---
## Getting Started with Troubleshooting
**URL:** https://optilogic.com/resources/help-center/docs/getting-started-with-troubleshooting

In this section, we outline some techniques for debugging models in Cosmic Frog. In general, there’s no one “right” approach to debugging, but knowing where you can get information on what went wrong can be helpful.
An error state in the run manager is the most obvious sign that something is wrong with our model setup.
After reaching an error state, the first place to check is the Job Records section of the Run Manager. Here you will find a summary of events from the model solve, and if an error is thrown you can potentially see the cause directly from here:
Next, you can check the Job Error Log. The Job Error Log will contain more detailed messaging on errors that are thrown during a model solve. While there are a number of possible errors, the most common cause of an error state is an infeasible model. You can check if your model is infeasible by scrolling down to the bottom of the Job Error Log, or by searching for “infeasible” in the search bar.
If your model is infeasible, you can use the following toolkit to help understand why:
Sometimes even a model that finishes running can give results that we do not expect. It a good habit to check your Output Summary Tables after each run to make sure the results look like you expect.
In some cases, the output tables might not populate even if the model runs successfully. Even if these values do not populate, you can find the Gurobi optimization results in the job log. One useful tip is to search for “objective value” in the job log and make sure the value is in the range you expect.
If your model is running, but seems incorrect, you can use the following toolkit to help understand why:
If you are still having trouble, you can also reach out to us directly at support@optilogic.com.
In this section, we outline some techniques for debugging models in Cosmic Frog. In general, there’s no one “right” approach to debugging, but knowing where you can get information on what went wrong can be helpful.
An error state in the run manager is the most obvious sign that something is wrong with our model setup.
After reaching an error state, the first place to check is the Job Records section of the Run Manager. Here you will find a summary of events from the model solve, and if an error is thrown you can potentially see the cause directly from here:
Next, you can check the Job Error Log. The Job Error Log will contain more detailed messaging on errors that are thrown during a model solve. While there are a number of possible errors, the most common cause of an error state is an infeasible model. You can check if your model is infeasible by scrolling down to the bottom of the Job Error Log, or by searching for “infeasible” in the search bar.
If your model is infeasible, you can use the following toolkit to help understand why:
Sometimes even a model that finishes running can give results that we do not expect. It a good habit to check your Output Summary Tables after each run to make sure the results look like you e
…（省略）


---
## Global Supply Chain Strategy Demo Model Review
**URL:** https://optilogic.com/resources/help-center/docs/global-supply-chain-strategy-demo-model-review

Every account holder has access to create the Global Supply Chain Strategy demo model. Following is an overview of the features of the model (and of Cosmic Frog).
If you wish to build the model instead, please follow the instructions located here: Build Your First Cosmic Frog Model
Every account holder has access to create the Global Supply Chain Strategy demo model. Following is an overview of the features of the model (and of Cosmic Frog).
If you wish to build the model instead, please follow the instructions located here: Build Your First Cosmic Frog Model


---
## Greenfield Settings Explained
**URL:** https://optilogic.com/resources/help-center/docs/greenfield-settings-explained

With Intelligent Greenfield Analysis (the Triad engine in Cosmic Frog), you have control over several different solve settings. For ease of use with scenario modeling, these have been placed in a dedicated table called Greenfield Settings. This allows for quick scenario building that leverages the column names. We will cover the settings which can be configured on the Greenfield Settings table and show an example of how scenarios can be used to change these settings.
Following screenshot shows the Greenfield Settings table:
In Cosmic Frog’s Module menu, choose Data to go to the Data module.
The Input Tables are showing in the Data module as the square grid icon has been selected. Output and Custom tables can be shown by clicking on the other 2 icons, the round grid icon for Output tables, and the square icon with solid top rows for Custom tables.
The Greenfield Settings table can be found in the Functional Tables section of the input tables list. When it is clicked it is also opened and made the active table.
The Greenfield Settings table has 1 record and this record is pre-populated with defaults in all Cosmic Frog models. Users can change the values of this record, either in the table itself so the setting apply to all scenarios that are being run, or through scenarios, so that the change only applies to a specific scenario. We will see an example of changing a Greenfield setting through a scenario further below.
An explanation of each setting is as follows:
Min Number Of New Facilities – The minimum number of new facility locations to be opened during solve. This will include any Candidate Facilities that are selected as well as any Greenfield Facilities. This value is ignored if Minimize Total Facilities is set to True.
Max Number Of New Facilities – The maximum number of new facility locations to be opened during solve. This will include any Candidate Facilities that are selected as well as any Greenfield Facilities. This value is ignored if Minimize Total Facilities is set to True.
Minimize Total Facilities – If True, the number of new facility locations to be opened will be minimized (Greenfield Facilities and Candidate Facilities). If False, the total cost (Facility Fixed Cost and Transportation Cost) will be minimized.
Exclude Facilities – If True, all Facilities in the model will be ignored during the Greenfield run. This value is set to False if Only Use Facilities As Candidate Locations is set to True.
Exclude Suppliers -If True, all Suppliers in the model will be ignored during the Greenfield run.
Only Use Facilities As Candidate Locations – If True, the selection pool for Greenfield locations will be restricted to Facilities that are Included. Facilities with a Facility Status of ‘Open’ will be forced to open and have their fixed operating cost charged in the Greenfield solve. Facilities with a Facility Status of ‘Consider’ will have the option to be opened as a Candidate Facility location and if selected, their fixed operating cost
…（省略）


---
## Hour Usage Tracking
**URL:** https://optilogic.com/resources/help-center/docs/hour-usage-tracking

When running Cosmic Frog models and other jobs on the Optilogic platform, cloud resources are used. Usage of these resources is billed based on the billing factor of the resource used for the job. Each Optilogic customer has an amount of cloud compute hours included in their Master License Agreement (MLA). Users may want to check how many of these hours have been used up and in this documentation 2 ways to do so will be covered. In the last section we will touch on how to best track hours at the team/company level.
The first option for hours tracking that will be covered is through the Usage tab in the user’s Account:
If a user is asked by their manager to report the hours they have used on the Optilogic platform, they can go here and use the Custom Time Window Preset option to align the start and end date of the reporting period with the dates of the MLA. They can then report back the number shown as the Total Billed Compute Time (box 4 in the above screenshot).
Through the Run Manager application on the Optilogic platform, user can also analyze their jobs run, including retrieving the Total Billed Compute Time:
After clicking on the View Charts icon, a screen similar to the following screenshot will be shown:
If a user needs to report their hours used on the Optilogic platform, they can download this jobs.csv file and:
Currently, only tracking of usage hours at the individual user level is available as described above. To get total team or company usage, a manager can ask their users to use 1 of the above 2 methods to report their Total Billed Compute Time and the manager can then add these up to get the total used hours so far. Tracking at the team/company level is planned to be made available on the Optilogic platform later in 2024.
When running Cosmic Frog models and other jobs on the Optilogic platform, cloud resources are used. Usage of these resources is billed based on the billing factor of the resource used for the job. Each Optilogic customer has an amount of cloud compute hours included in their Master License Agreement (MLA). Users may want to check how many of these hours have been used up and in this documentation 2 ways to do so will be covered. In the last section we will touch on how to best track hours at the team/company level.
The first option for hours tracking that will be covered is through the Usage tab in the user’s Account:
If a user is asked by their manager to report the hours they have used on the Optilogic platform, they can go here and use the Custom Time Window Preset option to align the start and end date of the reporting period with the dates of the MLA. They can then report back the number shown as the Total Billed Compute Time (box 4 in the above screenshot).
Through the Run Manager application on the Optilogic platform, user can also analyze their jobs run, including retrieving the Total Billed Compute Time:
After clicking on the View Charts icon, a screen similar to the following screenshot will be shown:
If
…（省略）


---
## How to Create an Optilogic Account
**URL:** https://optilogic.com/resources/help-center/docs/how-to-create-an-optilogic-account

In just a few clicks, you can create a free account on the Optilogic platform, which includes Cosmic Frog and DataStar among other applications. This document walks you through the steps.
If you just want the fastest way to get started:
You will go through 3 main stages:
To start, go to the Create a Free Account page on Optilogic's website. You will see the following form on the right-hand side:
After clicking on the Next Step button, the form changes to the following message. In addition, a new browser tab has been opened and has automatically become the active tab (see screenshot below this one):
The new active tab shows the following Create An Account form:
We will first go through the Single Sign-On steps using Google as the example in the next section. In the section after, Email and Password Steps, we will cover the email and password sign-up option.
We will illustrate the single sign-on process by going through the steps using a Google account. These steps are similar when using a Microsoft or LinkedIn account.
First, you will be prompted which Google account you want to use. The one you are currently logged into will be listed and you can click on it to select it. If you want to use another Google account, click on the "Use another account" option.
After selecting the Google account to use, the following form will appear:
If you have clicked on the Continue button, the following form with user account information will come up. If any details are missing, please fill them out and then click on the Submit button.
You have now signed up for an Optilogic account. The next step is to verify your email address, see the Verify Email and Configure Account section further below (link).
If you have chosen the option to sign-up using your email address and a password, the bottom part of the sign-up form will now look as follows:
Regardless of if you used an SSO method or the username & password option to sign-up for an Optilogic account, the next steps are the same. After clicking on the Submit button, the following message will appear:
Go into your email account and find the email from Optilogic Support with the subject Verify Your Optilogic Email. In there, click on the Verify Email button:
This will take you into the Optilogic platform, where you will be walked through a few quick questions to finalize your details and set up your account. Step 1 is pre-populated from your previous entries; if any are missing, please add them and then click on the Next button:
The next steps gather a bit more information:
When completed, the Cosmic Frog application will be opened, and you can start exploring any of the 3 example models shown on the start page:
🎉 You're ready to start using Optilogic!
Note that you can also sign up for an Optilogic account from the platform's login page (https://optilogic.app) by clicking on the Sign-Up link at the bottom. The options and steps are the same as documented above.
Did not receive verification email?
Wrong SSO account
…（省略）


---
## How to use & create Cosmic Frog Model Utilities
**URL:** https://optilogic.com/resources/help-center/docs/how-to-use-create-cosmic-frog-model-utilities

Utilities enable powerful modelling capabilities for use cases like integration to other services or data sources, repeatable data transformation or anything that can be supported by Python! System Utilities are available as a core capability in Cosmic Frog for use cases like LTL rate lookups, TransitMatrix time & distance generation, and copying items like Maps and Dashboards from one model to another. More useful System Utilities will become available in Cosmic Frog over time. Some of these System Utilities are also available in the Resource Library where they can be downloaded from, and then customized and made available to modelers for specific projects or models. In this Help Article we will cover both how to use use System Utilities as well as how to customize and deploy Custom Utilities.
The “Using and Customizing Utilities” resource in the Resource Library includes a helpful 15-minute video on Cosmic Frog Model Utilities and users are encouraged to watch this.
In this Help Article, System Utilities will be covered first, before discussing the specifics of creating one’s own Utilities. Finally, how to use and share Custom Utilities will be explained as well.
Users can access utilities within Cosmic Frog by going to the Utilities section via the Module Menu drop-down:
Once in the Utilities section, user will see the list of available utilities:
The appendix of this Help Article contains a table of all System Utilities and their descriptions.
Utilities vary in complexity by how many input parameters a user can configure and range from those where no parameters need to be set at all to those where many can be set. Following screenshot shows the Orders to Demand utility which does not require any input parameters to be set by the user:
The Copy map to a model utility shown in the next screenshot does require several parameters to be set by the user:
When the Run Utility button has been clicked, a message appears beneath it briefly:
Clicking on this message will open the Model Activity pane to the right of the tab(s) with open utilities:
Users will not only see activities related to running utilities in the Model Activity list. Other actions that are executed within Cosmic Frog will be listed here too, like for example when user has geocoded locations by using the Geocode tool on the Customers / Facilities / Suppliers tables or when user makes a change in a master table and chooses to cascade these changes to other tables.
Please note that the following System Utilities have separate Help Articles where they are explained in more detail:
The utilities that are available in the Resource Library can be downloaded by users and then customized to fit the user’s specific needs. Examples are to change the logic of a data transformation, apply similar logic but to a different table, etc. Or users may even build their own utilities entirely. If a user updates a utility or creates a new one, they can share these back with other users so they can benefit
…（省略）


---
## How to use Debug Mode
**URL:** https://optilogic.com/resources/help-center/docs/how-to-use-debug-mode

Running a model in debug mode can be a helpful troubleshooting tool as it will print more detailed reports of model issues.
The run option for Debug Mode is not included as a default in models but it can be added via the SQL Editor. Please copy and paste the following SQL query and run it against the model database you wish to add the option to.
Copy SQL Query Here: Add Debug Mode Model Run Option SQL Statement
Now, if you open the model again in Cosmic Frog you will see that Debug Mode is an available option in the run screen.
When set to True, Debug Mode will show all instances of validation errors instead of displaying an example of an error and the count of occurrences. You can see the difference in the following screenshot, where 1 row with 61 instances of the same error is turned into 61 individual rows.
Debug Mode will also print and save the input files that are passed to the solver – these will be saved in your File Explorer at My Files > debug_data > ModelName > ScenarioName. For each scenario run with debug mode enabled you will have the following:
Please note that this data is saved to your File Explorer and for larger models can take up quite a bit of disk space. If you reach 100% disk space utilization you will be unable to run any new jobs as they won’t have any space to write their required data to. The debug_data folder is almost always the cause of this disk space utilization issue, clearing its contents will allow jobs to start again.
If you have any questions or concerns about how this might impact your models, please don’t hesitate to reach out to support@optilogic.com.
Running a model in debug mode can be a helpful troubleshooting tool as it will print more detailed reports of model issues.
The run option for Debug Mode is not included as a default in models but it can be added via the SQL Editor. Please copy and paste the following SQL query and run it against the model database you wish to add the option to.
Copy SQL Query Here: Add Debug Mode Model Run Option SQL Statement
Now, if you open the model again in Cosmic Frog you will see that Debug Mode is an available option in the run screen.
When set to True, Debug Mode will show all instances of validation errors instead of displaying an example of an error and the count of occurrences. You can see the difference in the following screenshot, where 1 row with 61 instances of the same error is turned into 61 individual rows.
Debug Mode will also print and save the input files that are passed to the solver – these will be saved in your File Explorer at My Files > debug_data > ModelName > ScenarioName. For each scenario run with debug mode enabled you will have the following:
Please note that this data is saved to your File Explorer and for larger models can take up quite a bit of disk space. If you reach 100% disk space utilization you will be unable to run any new jobs as they won’t have any space to write their required data to. The debug_data folder is almost always the ca
…（省略）


---
## How to use Sequential Objectives
**URL:** https://optilogic.com/resources/help-center/docs/how-to-use-sequential-objectives

Sequential Objectives allow for you to set multiple tiers of objectives for the optimization solve to consider, where each tier of objectives can be relaxed by a defined percentage when solving for the next tier.
Here is a basic example of how Sequential Objectives can be used.
100 units of demand for P1 at CZ.
Available pathways for flow are as follows:
Find a solution that will first minimize total costs, but then will work to minimize the total amount of travel time in the solution while only relaxing the Total Cost solution by 20%.
When just solving with the standard objective of Profit Maximization, the cheapest path will be utilized. All flows will come from MFG > DC1 > CZ and the total cost will be $500.
We’ve built the Sequential Objectives so that we will first optimize over the Total Supply Chain Cost as Priority 1. We have also set the Tolerance to be 20 which will allow for a 20% relaxation in the solution to solve for the secondary objective – Total Weighted Flow Time.
We’ll now see that the more expensive pathway of MFG > DC2 > CZ is used as it requires less travel time. Because the initial cost was $500, we will send as many units as possible through DC2 up until the total cost reaches $600 – a 20% deviation from the initial cost. This results is 5 units flowing via DC2, while 95 units remain through DC1 for a total cost of $600.
This example model can be found in the Resource Library listed under the name of Sequential Objectives Demo.
Sequential Objectives allow for you to set multiple tiers of objectives for the optimization solve to consider, where each tier of objectives can be relaxed by a defined percentage when solving for the next tier.
Here is a basic example of how Sequential Objectives can be used.
100 units of demand for P1 at CZ.
Available pathways for flow are as follows:
Find a solution that will first minimize total costs, but then will work to minimize the total amount of travel time in the solution while only relaxing the Total Cost solution by 20%.
When just solving with the standard objective of Profit Maximization, the cheapest path will be utilized. All flows will come from MFG > DC1 > CZ and the total cost will be $500.
We’ve built the Sequential Objectives so that we will first optimize over the Total Supply Chain Cost as Priority 1. We have also set the Tolerance to be 20 which will allow for a 20% relaxation in the solution to solve for the secondary objective – Total Weighted Flow Time.
We’ll now see that the more expensive pathway of MFG > DC2 > CZ is used as it requires less travel time. Because the initial cost was $500, we will send as many units as possible through DC2 up until the total cost reaches $600 – a 20% deviation from the initial cost. This results is 5 units flowing via DC2, while 95 units remain through DC1 for a total cost of $600.
This example model can be found in the Resource Library listed under the name of Sequential Objectives Demo.


---
## How to use SMC3 RateWare XL in Cosmic Frog
**URL:** https://optilogic.com/resources/help-center/docs/how-to-use-smc3-rateware-xl-in-cosmic-frog

The nature of LTL freight rating is complex and multi-faceted. The RateWare® XL LTL rating engine of SMC3 enables customers to manage parcel pricing and LTL rating complexity, for both class and density rates, with comprehensive rating solutions.
Cosmic Frog users that hold a license to the RateWare XL LTL Rating Engine of SMC3 can easily use it within Cosmic Frog to lookup LTL rates and use them in their models. In this documentation we will explain where to find the SMC3 RateWare utility within Cosmic Frog and how to use it. First, we will cover the basic inputs needed in Cosmic Frog models, then how to configure and run the SMC3 RateWare Utility to look up LTL rates, and finally how to add those rates for usage in the model.
Before running the SMC3 RateWare Utility to retrieve LTL rates, we need to set up our model, including the origin-destination pairs for which we want to look up the LTL rates. Here, we will cover the inputs of a basic demo model showing how to use the SMC3 RateWare Utility. Of course, models using this utility may be much more complex in setup as compared to what is shown here.
The next 3 screenshots show:
To facilitate model building, this model uses groups for Customer and DCs, as shown in the next screenshot. All DCs are members of the DCs group and all CZs are members of the Customers group:
Using these groups, the Transportation Policies table is easily set up with 1 record from the DCs group to the CZs group as shown in the next screenshot. At runtime this 1 record is expanded into all possible OriginName-DestinationName combinations of the group members. So, this is an all DCs to all Customers policy that covers 9 possible origin-destination combinations.
Besides these tables, this simple model also has several other tables that are populated:
The SMC3 RateWare Utility is available by default from the Utilities module in Cosmic Frog, see next screenshot. Click on the Module Menu icon with 3 horizontal bars at the top left in Cosmic Frog, then click on Utilities in the menu that pops up:
You will now see a list of Utilities, similar to the one shown in this next screenshot (your Utilities are likely all expanded, whereas most are collapsed in this screenshot):
The rest of the inputs that can be configured are specific to the RateWare XL LTL Rating Engine and we refer user to SMC3’s documentation for the configuration of these settings.
When the utility is finished running, we can have a look at the smc3_inputs and smc3_outputs tables (if the option of All was used for Select Operation). First, here is a screenshot of the smc3_inputs table:
The next screenshot shows the smc3_outputs table in Optilogic’s SQL Editor. This is also a table with many columns as it contains origin and destination information, repeats the inputs of the utility, and contains details of the retrieved rates. Here, we are only showing the 3 most relevant columns: originname (the source DC), destinationname (the customer), and detailrate_1 which 
…（省略）


---
## How to use the Resource Library
**URL:** https://optilogic.com/resources/help-center/docs/how-to-use-the-resource-library

The Resource Library is the application within the Optilogic platform where you can find files that will help facilitate, accelerate, and customize your model building and running. These include Cosmic Frog template models, Python scripts, Reference Data and more.
What files are contained in the Resource Library?
One can access the Resource Library by clicking on the icon with 3 books on the left-hand side of the Optilogic platform.
Files with the purple outline and the tools icon are files that extend the platform's usage whether that be via Cosmic Frog for Excel Apps, Python Utilities, or 3rd party data connectors.
Files with a light-green outline and dark blue frog icon are Cosmic Frog related resources. These are mostly Cosmic Frog template models, which can be used to understand what inputs are needed to model certain business problems and what tools are available to examine outputs. The Cosmic Frog resources also include several other items like videos on specific Cosmic Frog features, 3rd party connectors to Cosmic Frog model databases (e.g. from / to Alteryx), and a Python scripting library to update and transform data within a Cosmic Frog model.
Files with a blue outline and blue beaker icon are Python scripts that use MIP (Mixed Integer Programming) optimization algorithms or simulation algorithms.
Files with a yellow outline and yellow cog icon contain Reference Data. These files contain demographic, location, and cost data which can be used to more quickly complete model data and fill in data gaps.
There are several ways to search, sort and filter the list of resources:
In the Search box one can free type to filter the list down to any resources that contain the search text.
Clicking on the Tags icon (horizontal bars of decreasing size) will bring up a list of Tags. One or multiple tags can be selected to filter down to those resources that have been tagged with these. This way you can quickly find all resources related to a specific technology, business problem or topic, like for example “Network Optimization”, “CapEx Planning” or “Bioinformatics”.
One can use the Sort By drop-down to change the sort order. The options include alphabetical ascending, alphabetical descending, by file type, newest to oldest, and oldest to newest.
One can filter by category by clicking on the Cosmic Frog, Atlas Tools and Apps, Reference Data, and O.R. Examples buttons. Once a category is selected, it can be unselected by clicking on it again. Multiple categories can be selected at the same time. If none of the specific categories are selected, then it defaults to showing all files.
If you have selected the Cosmic Frog category, we will render in a sub-category filter which will allow you to narrow down the Cosmic Frog templates by engine type making it easier to find the template that matches your use case.
When a file in the list is selected by clicking on it, a Preview is shown on the right-hand side of the screen. This preview contains a short descri
…（省略）


---
## How to use User Defined Variables
**URL:** https://optilogic.com/resources/help-center/docs/how-to-use-user-defined-variables

If you find that the standard constraints or costs in a model don’t quite capture your specific needs, you can create and define your own variables to use with costs and constraints.
To help in framing this discussion, let’s start with a simple example that fits into the standard input tables.
We wouldn’t need to do anything special in this instance, just create policies as normal and attach a Unit Cost of 5 to the MFG > DC transportation policy. To apply the constraint, we would create a Flow Constraint that sets a Max flow of 1000 units. While the input requirements are straightforward in this instance, let’s define both objectives in terms of variables as the solver would see them.
Flow Variable: MFG_CZ_Product_1_Flow
This example is simple, but it is important to think about costs and constraints in terms of the variables that they are applied over. This becomes even more important when we want to craft our own variables.
Let’s modify the constraint in the example above to now restrict the flow of Product_1 between MFG and DC to be no more than the flow of Product_2. Again, we will represent this in terms of variables as the solver will see them.
Flow Variables: MFG_CZ_Product_1_Flow, MFG_CZ_Product_2_Flow
We no longer have a constant on the right-hand side of our constraint – this is an issue as we have no way to input this type of a constraint requirement into the Flow Constraints table. Whenever we find ourselves expressing constraints or costs in terms of other variables that will be determined based on the model solve, we will need to make use of User Defined Variables.
Continuing with the constraint above, let’s modify the inequality statement so that we do in fact have a constant on the right-hand side. We can do this by subtracting one of the variables from both sides of the statement – this will then leave the right-hand side as 0.
We now have a constraint that can be modelled but we need to be able to define the left-hand side through the User Defined Variables table. User Defined Variables are defined as a series of Terms which are all linked to the same Variable Name. Each Term can be thought of as a solver variable as we have defined them in the examples above. For each Term, we will also need to enter a Coefficient, the Type of behavior we want to be capturing, and all of the needed information in the columns that follow depending on the Type that was just selected. All of these columns are based off of the individual constraint tables, so it is helpful to think about data as if you were entering a row in the specific constraint table.
Here is how the inputs for our example would look set up as a User Defined Variable:
We can see that by using the coefficients of 1 and -1, we have now accurately built the left-hand side of our inequality statement. All that’s left is to link this to a User Defined Constraint.
User Defined Constraints can be used to add restrictions to the values captured by the User Defined Variables. All that i
…（省略）


---
## How We Safeguard Your Data: Backups & Retention Explained
**URL:** https://optilogic.com/resources/help-center/docs/how-we-safeguard-your-data-backups-retention-explained

We take data protection seriously. Below is an overview of how backups work within our platform, including what’s included, how often backups occur, and how long they’re kept.
Every backup—whether created automatically or manually—contains a complete snapshot of your database at the time of the backup. This includes everything needed to fully restore your data.
We support two types of backups at the database level:
Often called “snapshots,” “checkpoints,” or “versions” by users:
We use a rolling retention policy that balances data protection with storage efficiency. Here’s how it works:
Retention Tier - Time Period - What’s Retained
Short-Term - Days 1–4 - Always keep the 4 most recent backups
Weekly - Days 5–7 - Keep 1 additional backup
Bi-Weekly - Days 8–14 - Keep the newest and oldest backups
Monthly - Days 15–30 - Keep the newest and oldest backups
Long-Term - Day 31+ - Keep the newest and oldest backups
This approach ensures both recent and historical backups are available, while preventing excessive storage use.
In addition to per-database backups, we also perform server-level backups:
These backups are designed for full-server recovery in extreme scenarios, while database-level backups offer more precise restore options.
To help you get the most from your backup options, we recommend the following:
If you have additional questions about backups or retention policies, please contact our support team at support@optilogic.com.
We take data protection seriously. Below is an overview of how backups work within our platform, including what’s included, how often backups occur, and how long they’re kept.
Every backup—whether created automatically or manually—contains a complete snapshot of your database at the time of the backup. This includes everything needed to fully restore your data.
We support two types of backups at the database level:
Often called “snapshots,” “checkpoints,” or “versions” by users:
We use a rolling retention policy that balances data protection with storage efficiency. Here’s how it works:
Retention Tier - Time Period - What’s Retained
Short-Term - Days 1–4 - Always keep the 4 most recent backups
Weekly - Days 5–7 - Keep 1 additional backup
Bi-Weekly - Days 8–14 - Keep the newest and oldest backups
Monthly - Days 15–30 - Keep the newest and oldest backups
Long-Term - Day 31+ - Keep the newest and oldest backups
This approach ensures both recent and historical backups are available, while preventing excessive storage use.
In addition to per-database backups, we also perform server-level backups:
These backups are designed for full-server recovery in extreme scenarios, while database-level backups offer more precise restore options.
To help you get the most from your backup options, we recommend the following:
If you have additional questions about backups or retention policies, please contact our support team at support@optilogic.com.


---
## Importing Data to Atlas
**URL:** https://optilogic.com/resources/help-center/docs/importing-data-to-atlas

Fast, AI-driven supply chain decision orchestration for every individual and team —from strategic design to tactical planning.
Model, optimize, and simulate even the most complex supply chains at scale and trade off cost, service, risk, and sustainability.
Eliminate data challenges with AI-automated cleansing and workflow orchestration for decision-ready intelligence instantly.
Optilogic's breakthrough agentic AI system for supply chain design — compresses months of supply chain design work into a single day.
Purpose-built apps for every stakeholder — Deploy across your entire organization today. Act on insights from day one.
Stay updated on the latest from Optilogic.
Enhance your skills with our hands-on training sessions and courses.
Dive into expert insights, industry trends, and practical tips for success.
Discover Optilogic's partner network empowering transformation and supply chain success.
Discover on-demand interviews, demos, and customer sessions.
Find step-by-step guides, FAQs, and support.
Access our full library of guides, case studies, and tools to help you succeed.
Connect with Optilogic peers, exchange insights, and accelerate supply chain success.
There are four main methods for adding data to Atlas:
1. Drag/Drop
2. Upload tool
3. OneDrive
4. Leverage API code


---
## Importing Data to Cosmic Frog
**URL:** https://optilogic.com/resources/help-center/docs/importing-data-to-cosmic-frog

Cosmic Frog supports importing and exporting both CSV and Excel files directly through the application. This enables users to for example:
In this documentation we will cover how users can import and export data into and out of Cosmic Frog, and illustrate this with multiple examples.
There are 2 methods of importing Excel/CSV data into Cosmic Frog’s input tables available to users:
Pointers on how data to be imported needs to be formatted will be covered first, including some tips and call outs of specifics to keep in mind when using the upsert import method. Next, the steps to import a CSV/Excel file will be walked through step by step.
Data is mapped from CSV/Excel files based on matching column names and table names matching to the file name (CSV) or worksheet name (Excel):
Data preparation tips:
CSV vs Excel: CSV files only have 1 “worksheet”, so it can only contain data to be imported into 1 table, whereas Excel files can have multiple worksheets with data to be imported to different tables in Cosmic Frog.
Please take note of how existing records are treated when using the upsert import method to import to a table which already has some data in it:
We will illustrate these behaviors through several examples too.
Users can import 1 or multiple CSV or Excel files simultaneously, please take note of how the import will work for following situations:
Once ready to import the prepared CSV/Excel file(s), user has 2 ways of accessing the import and export methods: from the File menu in the toolbar and from the right-click context menu of an input table. It looks like this from the File menu to import a file:
And when using the right-click context menu the steps to import a file are as follows:
When using the replace import method, a confirmation message will now be shown on which user can click Import to continue the import or Cancel to abort.
Next, a file explorer window opens in which user can browse to and select the CSV/Excel file(s) to import:
Once the import starts, a status message shows at the top of the active table:
The Model Activity log will also have an entry for each import action:
User can see the results of the import by opening and inspecting the affected input table(s), and by looking at the row counts for the tables in the input tables list, outlined in green in this screenshot:
A common way to start building a new model in Cosmic Frog is to make use of the replace import method to populate multiple tables simultaneously with data from Excel or CSV files. These files have typically been prepared from ERP extracts which have been manipulated to match the Cosmic Frog table and column names. This way, users do not need to enter data manually into the Cosmic Frog input tables, which would be very laborious. Note that it can be helpful to first export empty tables from a new, empty Cosmic Frog model to have a template to start filling out (see the “Exporting to CSV/Excel Files” section further below on how to do this).
Starting with a
…（省略）


---
## Incremental Change (Network Optimization)
**URL:** https://optilogic.com/resources/help-center/docs/incremental-change-network-optimization

Incremental Change is a powerful new capability in Cosmic Frog’s NEO engine (Network Optimization) that helps you manage the transition between two network states – such as moving from your current baseline network to an optimized future state. Rather than implementing all changes at once, Incremental Change allows you to control the pace and sequence of changes over time, making network transformations more practical and manageable.
This feature bridges the gap between theoretical optimization results and realistic implementation plans by generating a sequenced roadmap of network changes.
In this documentation, we will discuss the impact of Incremental Change, explain how to use it, and then walk through 2 demo models showing examples of the new capabilities. These models can be copied to your own Optilogic account from the Resource Library:
Please also see the following brief video for an introduction to Incremental Change and an overview of the second demo model, Incremental Change - Supplier Base Transition:
Supply chain networks rarely change overnight. Whether you are opening new distribution centers, shifting supplier bases, or adapting to seasonal demand fluctuations, real-world constraints limit how quickly you can implement changes. Organizations face practical limitations including:
Incremental Change addresses these realities by helping you answer critical questions: What is the best order of changes? What is the optimal rate of change? What tolerance levels are appropriate for different types of modifications?
Understand which network modifications deliver the greatest value earliest in your transition. Incremental Change provides clear visibility into expected savings versus the number of changes required, along with detailed change checklists for each scenario.
Create realistic, step-by-step roadmaps for moving from your current network to your target network. You will receive:
Manage network evolution in response to changing business conditions while respecting operational constraints. Balance total cost optimization against your tolerance for change, with detailed monthly implementation plans.
Cosmic Frog's Incremental Change currently supports the following network changes:
Progressive Facility Expansion: When opening a new distribution center, specify that you want to reassign up to 10 customers per month, and the system determines which customers to transition each month to maximize savings.
Seasonal Production Smoothing: For products with seasonal demand patterns, set constraints to ensure facility production never varies by more than 10% month-over-month, maintaining operational stability.
Multi-Year Facility Rollouts: Plan the optimal sequence for opening 10 facilities over five years including a detailed 2-year implementation roadmap.
Strategic Supplier Transitions: Systematically shift your supplier base. For example, progressively move sourcing out of or into a particular region – with Incremental Change determining the 
…（省略）


---
## Introduction to TRIAD – Intelligent Greenfield
**URL:** https://optilogic.com/resources/help-center/docs/introduction-to-triad---intelligent-greenfield

Fast, AI-driven supply chain decision orchestration for every individual and team —from strategic design to tactical planning.
Model, optimize, and simulate even the most complex supply chains at scale and trade off cost, service, risk, and sustainability.
Eliminate data challenges with AI-automated cleansing and workflow orchestration for decision-ready intelligence instantly.
Optilogic's breakthrough agentic AI system for supply chain design — compresses months of supply chain design work into a single day.
Purpose-built apps for every stakeholder — Deploy across your entire organization today. Act on insights from day one.
Stay updated on the latest from Optilogic.
Enhance your skills with our hands-on training sessions and courses.
Dive into expert insights, industry trends, and practical tips for success.
Discover Optilogic's partner network empowering transformation and supply chain success.
Discover on-demand interviews, demos, and customer sessions.
Find step-by-step guides, FAQs, and support.
Access our full library of guides, case studies, and tools to help you succeed.
Connect with Optilogic peers, exchange insights, and accelerate supply chain success.
Watch the video for an introduction to the features and functions of the Optilogic Intelligent Greenfield (Triad) engine.


---
## Inventory – Days of Supply (Simulation)
**URL:** https://optilogic.com/resources/help-center/docs/inventory-days-of-supply-simulation

When demand fluctuates due to for example seasonality, it can be beneficial to manage inventory dynamically. This means that when the demand (or forecasted demand) goes up or down, the inventory levels go up or down accordingly. To support this in Cosmic Frog models, inventory policies can be set up in terms of days of supply (DOS): for example for the (s,S) inventory policy, the Simulation Policy Value 1 UOM and Simulation Policy Value 2 UOM fields can be set to DOS. Say for example that reorder point s and order up to quantity S are set to 5 DOS and 10 DOS, respectively. This means that if the inventory falls to or below the level that is the equivalent of 5 days of supply, a replenishment order is placed that will order the amount of inventory to bring the level up to the equivalent of 10 days of supply. In this documentation we will cover the DOS-specific inputs on the Inventory Policies table, how a day of supply equivalent in units is calculated from these and walk through a numbers example.
In short, using DOS lets users be flexible with policy parameters; it is a good starting point for estimating/making assumptions about how inventory is managed in practice.
The following screenshot shows the fields that set the simulation inventory policy and its parameters:
This inventory policy for product P1 at facility DC_1 is set to (s,S) which is often referred to as a minimum/maximum policy. When the inventory falls to the value of reorder point s or below, a replenishment order is placed to bring the inventory back up to the order up to value of S.
The reorder point s is set to 5 days of supply by setting the Simulation Policy Value 1 field to 5 and its UOM field to DOS.
The order up to quantity S is set to 10 days of supply by setting the Simulation Policy Value 2 field to 10 and its UOM field to DOS.
For the same inventory policy, the next screenshot shows the DOS-related fields on the Inventory Policies table; note that the UOM fields are omitted in this screenshot:
DOS Window and its UOM field – the number of days of (forecasted) demand that are used to calculate the 1 day of supply equivalent in units. Note that the default for the UOM field is hours, so it needs to be set to DAY if wanting to fill out a number in the DOS Window field that means days. In this example, the DOS Window is set to 10 days (the UOM field that is not shown is set to DAY). In practice, a DOS Window needs to be short enough to capture changes in order trends, but also long enough so that replenishments can keep up with customer orders.
DOS Leadtime and its UOM field – when using forecasted demand to calculate the 1 DOS equivalent, a lead-time can be set using these fields, so that the calculation of 1 DOS will not use the forecasted demand for the current day and immediately following days but is offset by this lead-time. This can account for the time it takes to get a replenishment order in, so the amount to reorder depends on future demand that will occur from whe
…（省略）


---
## Keyboard Shortcuts in Cosmic Frog
**URL:** https://optilogic.com/resources/help-center/docs/keyboard-shortcuts-in-cosmic-frog

Fast, AI-driven supply chain decision orchestration for every individual and team —from strategic design to tactical planning.
Model, optimize, and simulate even the most complex supply chains at scale and trade off cost, service, risk, and sustainability.
Eliminate data challenges with AI-automated cleansing and workflow orchestration for decision-ready intelligence instantly.
Optilogic's breakthrough agentic AI system for supply chain design — compresses months of supply chain design work into a single day.
Purpose-built apps for every stakeholder — Deploy across your entire organization today. Act on insights from day one.
Stay updated on the latest from Optilogic.
Enhance your skills with our hands-on training sessions and courses.
Dive into expert insights, industry trends, and practical tips for success.
Discover Optilogic's partner network empowering transformation and supply chain success.
Discover on-demand interviews, demos, and customer sessions.
Find step-by-step guides, FAQs, and support.
Access our full library of guides, case studies, and tools to help you succeed.
Connect with Optilogic peers, exchange insights, and accelerate supply chain success.


---
## Less-Than-Truckload Costing Utility
**URL:** https://optilogic.com/resources/help-center/docs/less-than-truckload-costing-utility

The Less Than Truckload Costing utility solves the challenge of pricing less-than-truckload (LTL) shipments when carrier rate data is complex and varies by service level, distance, and weight. Rather than manually looking up rates in carrier tariff tables, this workflow automates the entire process using FedEx Express Freight standard list rates. The utility expects a lanes-to-cost table containing shipment details including origin, destination, distance, weight, and desired service level. After running the utility, users receive a fully costed table with calculated transportation costs.
The Less Than Truckload Costing Utility is available on the Resource Library, from which you can download it or copy it to your Optilogic account. Learn more about the Resource Library in this How to use the Resource Library help center article.
Sample Data
System Utility
The steps to use this utility are as follows. These are illustrated with screenshots below.
Screenshots of the steps:
Key Constraints:
The utility produces an output table containing all lanes from the input with the following additional columns populated:
LTL costs are calculated as a three-component sum:
Each component is calculated independently using the formula:
Where:
FedEx Freight zones (101–150) represent the transit distance and pricing tier between an origin and destination. Zones are assigned by FedEx based on origin and destination ZIP codes. You can determine the correct zone for a lane using the FedEx Freight zone chart or a zone lookup tool.
Higher zone numbers generally correspond to longer distances and higher rates.
The utility supports the following standard NMFC freight classes:
Freight class values are case-insensitive and will be normalized automatically. Common formats such as "60", "60.0", and "60.00" are all accepted and treated as equivalent.
Service level values are normalized to lowercase automatically, so "Economy", "ECONOMY", and "economy" are all accepted.
If a lane cannot be costed, the failure_reasons column will contain one or more of the following:
The Less Than Truckload Costing utility solves the challenge of pricing less-than-truckload (LTL) shipments when carrier rate data is complex and varies by service level, distance, and weight. Rather than manually looking up rates in carrier tariff tables, this workflow automates the entire process using FedEx Express Freight standard list rates. The utility expects a lanes-to-cost table containing shipment details including origin, destination, distance, weight, and desired service level. After running the utility, users receive a fully costed table with calculated transportation costs.
The Less Than Truckload Costing Utility is available on the Resource Library, from which you can download it or copy it to your Optilogic account. Learn more about the Resource Library in this How to use the Resource Library help center article.
Sample Data
System Utility
The steps to use this utility are as follows. These are illust
…（省略）


---
## Lumina Tariff Optimizer – Modeling Tariff Strategies
**URL:** https://optilogic.com/resources/help-center/docs/lumina-tariff-optimizer-modeling-tariff-strategies

Optilogic introduces the Lumina Tariff Optimizer – a powerful optimization engine that empowers companies to reoptimize supply chains in real-time to reduce the effects of tariffs. It provides instant clarity on today’s evolving tariff landscape, uncovers supply chain impacts, and recommends actions to stay ahead – now and into the future.
Manufacturers, distributors, and retailers around the world are faced with an enormous task trying to keep up with changing tariff policies and their supply chain impact. With Optilogic’s Lumina Tariff Optimizer, companies can illuminate their path forward by proactively designing tariff mitigation strategies that automatically consider the latest tariff rates.
With Lumina Tariff Optimizer, Optilogic users can stay ahead of tariff policy and answer critical questions to take swift action:
The following 7-minute video gives a great overview of the Lumina Tariff Optimizer tools:
Optilogic’s Lumina Tariff Optimization engine can be leveraged by modelers within Cosmic Frog or be leveraged within a Cosmic Frog for Excel app for other stakeholders across the business to evaluate the tariff impact to their end-to-end supply chain. Optilogic enables users to get started quickly with Lumina with several items in the Resource Library that include:
This documentation will cover each of these Lumina Tariff Optimizer tools, in the same order as listed above.
The first tool in the Lumina Tariff Optimizer toolset is the Tariffs example model which users can copy to their own account from the Resource Library. We will walk through this model, covering inputs and outputs, with emphasis on how to specify tariffs and their impact on the optimal solution when running network optimization (using the Neo engine) on the scenarios in the model.
Let us start by looking at the map of the Tariffs model, which is showing the model locations and flows for the Baseline scenario:
This model consists of the following sites:
Next, we will have a look at the Products table:
As mentioned above, raw materials RM1, RM2, and RM3 are supplied by Chinese suppliers and the others 6 raw materials by European suppliers, which we can confirm by looking at the Supplier Capabilities input table:
The Bills Of Materials input table shows that each finished good takes 3 of the Raw Materials to be manufactured; the Quantity field indicates how much of each is needed to create 1 unit of finished good:
Looking at the Production Policies input table, we see that both the US and Mexico factory can produce Consumables, but Rockets are only manufactured in Mexico and Space Suits only in the US:
To understand the outputs later, we also need to briefly cover the Flow Constraints input table, which shows that the El Bajio Factory in Mexico can at a maximum ship out 3.5M units of finished goods (over all products and the model horizon together):
To enter tariffs and take them into account in a network optimization (Neo) run, users need to populate the new Tariffs input 
…（省略）


---
## Maps – Styling Points & Flows based on Breakpoints
**URL:** https://optilogic.com/resources/help-center/docs/maps-styling-points-flows-based-on-breakpoints

Cosmic Frog’s new breakpoints feature enables users to create maps which relay even more supply chain data in just one glance. Lines and points can now be styled based on field values from the underlying input or output table the lines/points are drawn from.
In this Help Center article, we will cover where to find the breakpoints feature for both point and line layers and how to configure them. A basic knowledge of how to configure maps and their layers in Cosmic Frog is assumed; users unfamiliar with maps in Cosmic Frog are encouraged to first read the “Getting Started with Maps” Help Center article.
Using Breakpoints on Line Layers
First, we will walk through how to apply breakpoints to map layers of type = line, which are often used to show flows between locations. With breakpoints we can style the lines between origins and destinations for example based on how much is flowing in terms of quantity, volume or weight. It is also possible to style the lines on other numeric fields, like costs, distances or time.
Consider the following map showing flows (dark green lines) to customers (light green circles):
A map layer is selected in the maps & layers list on the left-hand side of the map (not shown in the screenshot). To the right of the map, the Condition Builder pane is open, which is also indicated by the darker blue color of the left icon of the three icons at the right top.
The name of the Layer is Customer Flows.
Under Table Name, user has chosen the Optimization Flow Summary output table from the drop-down list of input and output tables which can be used to draw a map layer from.
In the area where user can apply filters to the table data, the Condition Builder option is selected. The condition that is used (FlowType = ‘CustomerFulfillment’), means that only flows going to customers will be drawn for this layer.
Next, we will go to the Layer Style pane on which breakpoints can be turned on and configured:
We are now on the Layer Style pane of this same Customer Flows layer. While on this pane, the second of the three icons at the top right is a darker blue than the other two, which also indicates the Layer Style pane is the active one.
In the top part of this pane, the style of layer can be configured, including characteristics like color, size, border, and showing line direction. For complete details on what can be configured here, please see the “Layer Style” section in the “Getting Started with Maps” Help Center article. Currently, the lines are styled as a solid dark green line of size 4 and 100% opacity. The lines have no border and line direction (arrowheads indicating the direction of flow from origin to destination) is turned off too.
For this layer, tooltips showing the Flow Quantity when hovering over a flow line have been configured on the Layer Labels pane, the pane that comes up when clicking on the third icon at the top right and described in more detail in the “Layer Labels” section of the Getting Started with Maps article.

…（省略）


---
## Model Output Insights AI Agent
**URL:** https://optilogic.com/resources/help-center/docs/model-output-insights-ai-agent

The Model Output Insights Agent helps users investigate and analyze Cosmic Frog model outputs by turning analytical questions into structured, data-backed strategic reports. It breaks down complex questions into a step-by-step exploration plan, executes targeted queries, synthesizes findings, and produces a professional report - complete with visualizations and actionable recommendations.
This documentation describes how this specific agent works and can be configured. Please see the “AI Agents: Architecture and Components” Help Center article if you are interested in understanding how the Optilogic AI Agents work at a detailed level.
Extracting meaningful insights from large databases typically requires exploring and analyzing many output tables which can take a lot of time and effort. The Model Output Insights Agent streamlines the process, helping users get to the insights quicker than ever before.
Main skills the Model Output Insights Agent uses:
Supporting capabilities:
The agent can be accessed through the Run AI Agent task in DataStar. Once a Run AI Agent task is added to the macro, first the Model Output Insights Agent needs to be selected from the list of available agents and utilities in the "Select Utility" section:
Next, the inputs and settings for the task can be specified in the Configure Utility, Run Configuration, and Notes sections:
This next screenshot shows how to get a Folder Path while in the Explorer application: 1) right-click on the folder in the Explorer, 2) hover over Copy in the context menu, and 3) click on Folder Path:
After the run, a report in both markdown (.md) and pdf (.pdf) format and charts (if any) are created and can be found in the Explorer with the specified file name and folder. Once clicked, the file is opened in the Lightning Editor application for review.
Note that currently the charts are only included in the markdown file as a file name. Users can look for the charts in the Charts folder in the targeted output directory.
The Model Output Insights Agent helps users investigate and analyze Cosmic Frog model outputs by turning analytical questions into structured, data-backed strategic reports. It breaks down complex questions into a step-by-step exploration plan, executes targeted queries, synthesizes findings, and produces a professional report - complete with visualizations and actionable recommendations.
This documentation describes how this specific agent works and can be configured. Please see the “AI Agents: Architecture and Components” Help Center article if you are interested in understanding how the Optilogic AI Agents work at a detailed level.
Extracting meaningful insights from large databases typically requires exploring and analyzing many output tables which can take a lot of time and effort. The Model Output Insights Agent streamlines the process, helping users get to the insights quicker than ever before.
Main skills the Model Output Insights Agent uses:
Supporting capabilities:
The agent
…（省略）


---
## Model Sharing & Backups for Multi-User Collaboration in Cosmic Frog
**URL:** https://optilogic.com/resources/help-center/docs/model-sharing-backups-for-multi-user-collaboration-in-cosmic-frog

With Optilogic’s new Teams feature set (see the "Getting Started with Optilogic Teams" help center article) working collaboratively on Cosmic Frog models has never been easier: all members of a team have access to all contents added to that team’s workspace. Centralizing data using Teams ensures there is a single source of truth for files/models which prevents version conflicts. It also enables real-time collaboration where files/models are seamlessly shared across all team members, and updates to any files/models are instantaneous for all team members.
However, whether your organization uses Teams or not, there can be a need to share Cosmic Frog models, for example to:
In this documentation we will cover how to share models, and the different options for sharing. Sharing models can be from an individual user or a team to an individual user or a team. As the risk of something undesirable happening with the model when multiple people work on it increases, it is important to be able to go back to a previous version of the model. Therefore, it is best practice to make a backup of a model prior to sharing it. Continue making backups when important/major changes are going to be made or when wanting to try out something new. How to make a backup of a model will be explained in this documentation too and will be covered first.
A backup of a model is a snapshot of its exact state at a certain point in time. Once a backup has been made, users can use them to revert to if needed. Initiating the creation of a backup of a Cosmic Frog model can be done from 3 locations within the Optilogic platform: 1) from the Models module within Cosmic Frog, 2) through the Explorer and 3) from within the Cloud Storage application on the Optilogic platform. The option from within Cosmic Frog will be covered first:
When in the Models module of Cosmic Frog (aka the Model Manager), hover over the model you want to create a backup for, and click on the icon with 3 horizontal dots that comes up at the bottom right of the model card (1). This brings up the model management options context menu, from which you can choose the Backup option (2). If only 1 model is selected, the Backup option can also be accessed from the toolbar at the top of the model list/grid (3).
From the Cloud Storage application it works as follows:
Through the Explorer, the process is similar:
Whether from the Models module within Cosmic Frog, through the Cloud Storage application or via the Explorer, in all 3 cases the Create Backup form comes up:
After clicking on Confirm, a notification at the top of the user’s screen will pop up saying that the creation of a backup has been started:
At the same time, a locked database icon with hover over text of “Backup in progress…” appears in the Status field of the model database (this is in the Cloud Storage application’s list of databases):
This locked database icon will disappear again once the backup is complete.
Users can check progress of the backup by going to 
…（省略）


---
## Modeler AI Agent
**URL:** https://optilogic.com/resources/help-center/docs/modeler-ai-agent

The Modeler Agent is one of Ada’s AI-powered supply chain modeling specialists. It helps users build, validate, troubleshoot, run, analyze, and automate Cosmic Frog network optimization (Neo) and transportation optimization (Hopper) models. The Modeler Agent accelerates the entire modeling lifecycle – from raw operational data to optimization-ready model construction and scenario analysis – while improving model quality, traceability, and reproducibility. By combining supply chain domain knowledge with direct platform capabilities, it helps teams move from messy source data to solver-ready models faster and with fewer manual hand-offs.
The agent can be accessed by chatting with Ada in the next generation Optilogic platform and via Run AI Agent tasks in DataStar.
Users get leverage in these main areas:
Data → Model mapping
Validation & feasibility checks
Scenario & policy authoring (conceptual + implementation guidance)
Engine execution support
Workflow automation (DataStar)
Reporting and documentation
There are two ways to access the Modeler Agent:
Both ways will be explained: via chat first, then the DataStar workflow, followed by an overview of the main differences between the 2 methods.
It is recommended to be somewhat familiar with Ada and how to talk to her in the chat UI before diving into this content. Please see the Getting Started with Ada & Agentic AI article, and in particular its How to Use Ada section.
Once logged into the next generation Optilogic platform at https://ai.optilogic.app, you can start chatting with Ada leveraging the Modeler Agent right away from the central part of the Home page.
Here, our example is of a new modeler who inherited a work in progress model to evaluate and optimize their company's manufacturing footprint. They have the Cosmic Frog model which is partially built and a DataStar project with both raw historical and master data, and a set of previously cleaned tables.
Our 2 connected databases are shown in this screenshot:
After submitting a prompt, the Modeler Agent will start processing and formulating a response; the following 3 screenshots show the full response:
We now understand there are several issues that need to be addressed before we can attempt a first model run. First, the user decides to focus on the product name problem identified in the Customer Demand table. To understand the problem, we first have a look at the Customer Demand table in the Cosmic Frog model and notice that whereas all finished goods should follow the naming convention of FGXXX, many do not:
Since we are not familiar with the data in the DataStar project, we ask the Modeler Agent if there are tables that can help resolve the product naming problem:
We then have a look at the mentioned tables in the DataStar project and identify the 2 we think can be used as lookups to fix the incorrect product names:
The response does not yet make any changes, but summarizes what they will be and asks us to confirm before making the changes
…（省略）


---
## Modeling Brazilian Taxes using User Defined Variables & Costs
**URL:** https://optilogic.com/resources/help-center/docs/modeling-brazilian-taxes-using-user-defined-variables-costs

Tax systems can be complex, like for example those in Greece, Colombia, Italy, Turkey, and Brazil are considered to be among the most complex ones. It can however be important to include taxes, whether as a cost or benefit or both, in supply chain modeling as they can have a big impact on sourcing decisions and therefore overall costs. Here we will showcase an example of how Cosmic Frog’s User Defined Variables and User Defined Costs can be used to model Brazilian ICMS tax benefits and take these into account when optimizing a supply chain.
The model that is covered in this documentation is the “Brazil Tax Model Example” which was put together by Optilogic’s partner 7D Analytics. It can be downloaded from the the Resource Library. Besides the Cosmic Frog model, the Resource Library content also links to this “Cosmic Frog – BR Tax Model Video” which was also put together by 7D Analytics.
A helpful additional resource for those unfamiliar with Cosmic Frog’s user defined variables, costs, and constraints is this “How to use user defined variables” help article.
In this documentation the setup of the example model will first be briefly explained. Next, the ICMS tax in Brazil will be discussed at a high level, including a simplified example calculation. In the third section, we will cover how ICMS tax benefits can be modelled in Cosmic Frog. And finally, we will look at the impact of including these ICMS tax benefits on the flows and overall network costs.
One quick note upfront is that the screenshots of Cosmic Frog tables used throughout this help article may look different when comparing to the same model in user’s account after taking it from the Resource Library. This is due to columns having been moved or hidden and grids being filtered/sorted in specific ways to show only the most relevant information in these screenshots.
In this example model, 2 products are included: Prod_National to represent products that are made within Brazil at the MK_PousoAlegre_MG factory and Prod_Imported to represent products that are imported, which is supplied from SUP_Itajai_SC within the model, representing the seaport where imported products would arrive. There are 6 customer locations which are in the biggest cities in Brazil; their names start with CLI_. There are also 3 distribution centers (DCs): DC_Barueri_SP, DC_Contagem_MG, and DC_FeiraDeSantana_BA. Note that the 2 letter postfixes in the location names are the abbreviations of the states these locations are in. Please see the next screenshot where all model locations are shown on a map of Brazil:
The model’s horizon is all of 2024 and the 6 customers each have demand for both products, ranging from 100 to 600 units. The SUP_ location (for Prod_Imported) and MK_ location (for Prod_National) replenish the DCs with the products. Between the DCs, some transfers are allowed too. The demand at the customer locations can be fulfilled by 1, 2 or all 3 DCs, depending on the customer. The next screenshot of the T
…（省略）


---
## Modelling Returns (Network Optimization)
**URL:** https://optilogic.com/resources/help-center/docs/modelling-returns-network-optimization

For various reasons, many supply chains need to deal with returns. This can for example be due to packaging materials coming back to be reused at plants or DCs, retail customers returning finished goods that they are not happy with, defective products, etc. Previously, these returns could mostly be modelled within Cosmic Frog NEO (Network Optimization) models by using some tricks and workarounds. But with the latest Cosmic Frog release, returns are now supported natively, so that the reuse, repurposing, or recycling of these retuned products to help companies reduce costs, minimize waste, and improve overall supply chain efficiency can be taken into account easily.
This documentation will first provide an overview of how returns work in a Cosmic Frog model and then walk through an example model of a retailer which includes modelling the returns of finished goods. The appendix details all the new returns-related fields in several new tables and some of the existing tables.
When modelling returns in Cosmic Frog:
Users need to use 2 new input tables to set up returns:
The Return Ratios table contains the information on how much return-product is returned for a certain amount of product delivered to a certain destination:
The Return Policies table is used to indicate where returned products need to go to and the rules around multiple possible destinations. Optionally, costs can be associated with the returns here and a maximum distance allowed for returns can be entered on this table too.
Note that both these tables have Status and Notes fields (not shown in the screenshots), like most Cosmic Frog input tables have. These are often used for scenario creation where the Status is set to Exclude in the table itself and changed to Include in select scenarios based on text in the Notes field.
All columns on these 2 returns-related input table are explained in more detail in the appendix.
In addition to populating the Return Policies and Return Ratios tables, users need to be aware that additional model structure needed for the returned products may need to be put in place:
The Optimization Return Summary output table is a new output table that will be generated for Neo runs if returns are included in the modelling:
This table and all its fields are explained in detail in the appendix.
The Optimization Flow Summary output table will contain additional records for models that include returns; they can be identified by filtering the Flow Type field for “Return”:
These 2 records show the return flows and associated transportation costs for the Bag_1 and Bag_2 products from CZ_001, going to DC_Cincinnati, that we saw in the Optimization Return Summary table screenshot above.
In addition to the new Optimization Return Summary output table, and new records of Flow Type = Return in the Optimization Flow Summary output table, following existing output tables now contain additional fields related to returns:
The example Returns model can be copied from the Resource
…（省略）


---
## Multiple Compartments (Transportation Optimization)
**URL:** https://optilogic.com/resources/help-center/docs/multiple-compartments-transportation-optimization

The Multiple Compartments (MC) feature allows a single transportation asset (e.g., truck, trailer) to be divided into independent compartments, each with its own capacity and compatibility constraints. This enables Hopper to produce more accurate, feasible, and operationally realistic transportation plans.
Get up and running in 4 steps:
Use this feature when one or more of your transportation assets have physically separate sections that must be loaded independently. Common examples:
Without Multiple Compartments, Hopper checks only that the total shipment fits the total asset capacity. This can produce plans that look valid in the optimizer but cannot be executed operationally because individual compartments are overloaded or contain incompatible products.
Three changes have been made to Hopper's data model: one new input table, one new field on an existing input table, and one new field on an existing output table.
This table defines the structure and rules of the compartments that make up each configuration. Add one row per compartment; rows with the same Compartment Configuration Name form a single configuration.
A new Compartment Configuration Name field has been added to the Transportation Assets table. Populate it with the name of a configuration defined in the Compartment Configurations table to enable compartment-level modeling for that asset.
Effect on Hopper's solver:
The Transportation Optimization Shipment Summary output table now includes a Compartment Name column. For any shipment transported on a multi-compartment asset, this column shows which compartment it was assigned to.
This field enables:
The following example runs two scenarios with the same "MK Artic Multi Temp" asset to illustrate the difference:
Both scenarios have other single-compartment assets available. In each scenario, the MK Artic Multi Temp asset is used for one route. The charts below show how much of each product is on board at each stop along that route (stops are ordered by route sequence on the x-axis; the asset is loaded at Milton Keynes and Chelmsford depots and delivers to the CZ locations).
Key observations:
Multiple Compartments moves Hopper from aggregate capacity modeling to granular compartment-level modeling. This means:
Questions? Contact the Optilogic support team at support@optilogic.com.
The Multiple Compartments (MC) feature allows a single transportation asset (e.g., truck, trailer) to be divided into independent compartments, each with its own capacity and compatibility constraints. This enables Hopper to produce more accurate, feasible, and operationally realistic transportation plans.
Get up and running in 4 steps:
Use this feature when one or more of your transportation assets have physically separate sections that must be loaded independently. Common examples:
Without Multiple Compartments, Hopper checks only that the total shipment fits the total asset capacity. This can produce plans that look valid in the optimizer but cannot be execu
…（省略）


---
## Named Filters in Cosmic Frog
**URL:** https://optilogic.com/resources/help-center/docs/named-filters-in-cosmic-frog

Named Filters are an exciting new feature which allows users to create and save specific filters directly on grid views, to then be utilized seamlessly across all policies tables, scenario items and map layers. For example, if you create a filter named “DCs” in the Facilities table to capture all entries with “DC” in their designation, this Named Filter can then be applied in a policy table, providing a dynamic alternative to the traditional Group function.
Unlike Groups, named filters automatically update: adding or removing a DC record in the Facilities table will instantly reflect in the Named Filter, streamlining the workflow and eliminating the need for manual updates. Additionally, when creating Scenario Items or defining Map Layers, users can easily select Named Filters to represent specific conditions, easily previewing the data, making the process much quicker and simpler.
In this help article, how Named Filters are created will be covered first. In the sections after, we will discuss how Named Filters can be used on input tables, in scenario items, and on map layers, while the final section contains a few notes on deleting Named Filters.
Named Filters can be set up and saved on any Cosmic Frog table: input tables, output tables, and custom tables. These tables are found in the Data module of a Cosmic Frog model:
A quick description of each of the options available in the Filter drop-down menu follows here, we will cover most of these in more detail in the remainder of this Help Article:
Note that an additional Save Filter option becomes available in this menu in case a filter has been created (added) and next changes have been made to the table's filter conditions. The Save Filter option can then be used to update the existing named filter to reflect these changes.
Let’s walk through setting up a filter on the Facilities table that filters out records where the Facility Name ends in “DC” and save it as a named filter called “DCs”:
There are 3 buttons below the list of filters as follows (these were obscured by the hover text in the previous screenshot):
There is a right-click context menu available for filters listed in the Named Filters pane, which allows the user to perform some of the same actions as those in the main Filter menu shown above:
Named Filters can use filtering conditions that are applied to multiple fields in a table. The next example shows a Named Filter called “CZ2* Space Suit demand >6k” on the Customer Demand input table which uses filtering conditions on three fields:
Conditions were applied to 3 fields in the Customer Demand table, as follows: 1) Customer Name Begins With “CZ2”, 2) Product Name Contains “Space”, and 3) Quantity Greater Than “6000”. The resulting filter was saved as a Named Filter with the name “CZ2* Space Suit demand >6k” which is applied in the screenshot above. When hovering over this Named Filter, we indeed see the 3 fields and that they each have a single condition on them.
Besides being able 
…（省略）


---
## Navigating the Cosmic Frog Interface
**URL:** https://optilogic.com/resources/help-center/docs/navigating-the-cosmic-frog-interface

Fast, AI-driven supply chain decision orchestration for every individual and team —from strategic design to tactical planning.
Model, optimize, and simulate even the most complex supply chains at scale and trade off cost, service, risk, and sustainability.
Eliminate data challenges with AI-automated cleansing and workflow orchestration for decision-ready intelligence instantly.
Optilogic's breakthrough agentic AI system for supply chain design — compresses months of supply chain design work into a single day.
Purpose-built apps for every stakeholder — Deploy across your entire organization today. Act on insights from day one.
Stay updated on the latest from Optilogic.
Enhance your skills with our hands-on training sessions and courses.
Dive into expert insights, industry trends, and practical tips for success.
Discover Optilogic's partner network empowering transformation and supply chain success.
Discover on-demand interviews, demos, and customer sessions.
Find step-by-step guides, FAQs, and support.
Access our full library of guides, case studies, and tools to help you succeed.
Connect with Optilogic peers, exchange insights, and accelerate supply chain success.
Before you get started in Cosmic Frog watch this short video to learn how to navigate the software.


---
## Navigating the Optilogic Platform
**URL:** https://optilogic.com/resources/help-center/docs/navigating-the-optilogic-platform

Fast, AI-driven supply chain decision orchestration for every individual and team —from strategic design to tactical planning.
Model, optimize, and simulate even the most complex supply chains at scale and trade off cost, service, risk, and sustainability.
Eliminate data challenges with AI-automated cleansing and workflow orchestration for decision-ready intelligence instantly.
Optilogic's breakthrough agentic AI system for supply chain design — compresses months of supply chain design work into a single day.
Purpose-built apps for every stakeholder — Deploy across your entire organization today. Act on insights from day one.
Stay updated on the latest from Optilogic.
Enhance your skills with our hands-on training sessions and courses.
Dive into expert insights, industry trends, and practical tips for success.
Discover Optilogic's partner network empowering transformation and supply chain success.
Discover on-demand interviews, demos, and customer sessions.
Find step-by-step guides, FAQs, and support.
Access our full library of guides, case studies, and tools to help you succeed.
Connect with Optilogic peers, exchange insights, and accelerate supply chain success.


---
## Navigating the Platform
**URL:** https://optilogic.com/resources/help-center/docs/navigating-the-platform

Fast, AI-driven supply chain decision orchestration for every individual and team —from strategic design to tactical planning.
Model, optimize, and simulate even the most complex supply chains at scale and trade off cost, service, risk, and sustainability.
Eliminate data challenges with AI-automated cleansing and workflow orchestration for decision-ready intelligence instantly.
Optilogic's breakthrough agentic AI system for supply chain design — compresses months of supply chain design work into a single day.
Purpose-built apps for every stakeholder — Deploy across your entire organization today. Act on insights from day one.
Stay updated on the latest from Optilogic.
Enhance your skills with our hands-on training sessions and courses.
Dive into expert insights, industry trends, and practical tips for success.
Discover Optilogic's partner network empowering transformation and supply chain success.
Discover on-demand interviews, demos, and customer sessions.
Find step-by-step guides, FAQs, and support.
Access our full library of guides, case studies, and tools to help you succeed.
Connect with Optilogic peers, exchange insights, and accelerate supply chain success.
To help familiarize you with our product we have created the following video.


---
## Network Transportation Optimization (Neo & Hopper)
**URL:** https://optilogic.com/resources/help-center/docs/network-transportation-optimization-neo-hopper

Exciting new features which enable users to solve both network and transportation optimization in one solve have been added to Cosmic Frog. By optimizing multi-stop route optimization as part of Network Optimization, it enables users to streamline their analysis and make their Network Optimization more accurate. This is possible because the single optimization solve calculates multi-stop route costs by shipment/customer combination, uses this cost as part of another possible transportation mode in addition to OTR, Rail, Air, etc. and will result in more accurate answers by including better transportation costs in a single solve.
In addition to this documentation, these 2 videos cover the new Network Transportation Optimization (NTO) features too:
Network Transportation Optimization is particularly useful for two classic network design problems (both will be described in more detail in the next section):
This feature set includes 2 ways of running the Transportation Optimization (Hopper) and Network Optimization (Neo) engines together:
Following will be covered in this documentation for both the Hopper within Neo and Hopper after Neo NTO algorithms: example use cases, model inputs, how to use the new features, basics of the model used to show the NTO features, and walk through 2 example models, including their setup (input tables, scenarios), and analysis of the outputs using tables and maps.
With this feature, users can consider routes as inputs in a Neo model, meaning that the model will optimize product flow sources based on all costs, including the cost of routes. Costs and asset capacities are taken into account for the routes.
Two example use cases which can be addressed using Hopper within Neo are customer consolidation and hub optimization, which will be illustrated with the images that follow.
Consider a network where 2 distribution centers (DCs) are available to serve the customers. Two of these customers are in between the DCs and can either be serviced by the DCs directly (the blue dashed point to point lines) or product can be delivered to both of them as part of a multi-stop route from either DC (the red solid lines):
Running Neo without Hopper, not taking any route inputs into account, can lead to a solution where each DC serves 1 customer:
Whereas when taking route costs and capacities into account during a Hopper within Neo solve, it may be found that the overall cost solution is lower if one of the DCs (DC 1 in this example) serves both customers using a multi-stop route:
As a second example, consider a network where Suppliers can either deliver product to a Hub, either direct or on a multi-stop route from multiple suppliers, or direct/on multi-stop routes from multiple suppliers to a Distribution Center. Again, blue dashed lines indicate direct point to point deliveries and red lines indicate multi-stop route options:
Not taking route options into account when running Neo without Hopper can lead to a solution where each Supplier
…（省略）


---
## Next Generation Optilogic Platform Overview
**URL:** https://optilogic.com/resources/help-center/docs/next-generation-optilogic-platform-overview

At Optilogic, we have built the next generation (next-gen) platform to complement our AI. It is a modern, unified workspace where users:
Never lose their place: switch between applications like SQL Editor or Run manager without losing context
Engage in a way that is natural to them, whether this is fully AI guided, using AI-as-copilot, or working heads-down in familiar tools
Work in an environment that reduces clutter and only surfaces what matters: the platform grows with your session and persists where you left off
Experience a cohesive framework that handles artifacts and iterative workflows seamlessly
While the next-gen platform is still in development, there is plenty available already for users to start working with it. Especially the AI-first approach will be a gamechanger for many. This documentation gives a high-level overview of the new platform. Please see the separate Getting Started with Ada & Agentic AI documentation for in-depth documentation on Ada, your supply chain modeling partner.
Logging in and First Time Configuration
Optilogic users can log into the next-gen platform at https://ai.optilogic.app, using the same credentials as those used to log into the current platform (on https://optilogic.app).
Once logged in, you are walked through 3 setup windows, shown in the following screenshots.
It is recommended to take the quick tour to learn about the platform. After it completes, you can follow another walkthrough, this one centered around using Ada through the chat UI. If you want to return to either of these tours later, you can find these in the Actions results part of Global Search (Ctrl + Space) after typing “introduction tour” or “Ada tour” in the search textbox.
Home Page and Sidebar
Your Home page will look similar to this:
In the top central part of the platform, Ada is available to immediately dive into any questions and tasks.
Further below, there are additional widgets, in this case a Recent Work one showing all recent DataStar and Cosmic Frog work and a Goals one for users to jump straight back in from where they left off.
The sidebar on the left provides quick access to all features.
Clicking anywhere in the sidebar will expand it:
Click on Home to return to the home page as shown in the previous screenshot.
Click on Chat to open the chat UI full screen, including historical conversations with Ada.
In this area, applications that have been opened will be added to the rail, like a taskbar with open applications. Note that:
Cosmic Frog and DataStar are by default pinned here as these are the most used Optilogic applications. They are greyed out when not open; click on them to open the application.
Use the Apps launcher (next bullet) to open other applications.
Applications can be active multiple times, e.g. 2 instances of Lightning Editor can be active showing 2 different files, see also the next section.
Right-clicking on an application brings up a context menu, see also the next section.
The Apps Launcher can be use
…（省略）


---
## Optilogic Engine Names Explained
**URL:** https://optilogic.com/resources/help-center/docs/optilogic-engine-names-explained

As you continue to work with the tool you might find yourself asking, what do these engine names mean and how the heck did they come up with them?
Anura, the name of our data schema, comes from the biological root where Anura is the order that all frogs and toads fall into.
NEO, our optimization engine, takes its name from a suborder of Anura – Neobatrachia. Frogs in this suborder are known to be the most advanced of any other suborder.
THROG, our simulation engine, takes its name from a superhero hybrid that crosses Thor with a frog (yes, this actually exists)
Triad, our greenfield engine, takes its name from the oldest known species of frogs – Triadobatrachus. You can think of it as the starting point for the evolution of all frogs, and it serves as a great starting point for modeling projects too!
Dart, our risk engine, takes its name from the infamous poison dart frog. Just as you would want to be aware of a poisonous frog’s presence, you’ll also want to be sure to evaluate any opportunities for risks to present themselves.
Dendro, our simulation evolutionary algorithm, takes its name from what is known to be the smartest species of frog – Dendrobates auratus. These frogs have the ability to create complex mental maps to evaluate and better navigate their surroundings.
Hopper, our transportation routing engine, doesn’t have a name rooted in frog-related biology but rather a visual of a frog hopping along from stop to stop just as you might see with a multi-drop transportation route.
As you continue to work with the tool you might find yourself asking, what do these engine names mean and how the heck did they come up with them?
Anura, the name of our data schema, comes from the biological root where Anura is the order that all frogs and toads fall into.
NEO, our optimization engine, takes its name from a suborder of Anura – Neobatrachia. Frogs in this suborder are known to be the most advanced of any other suborder.
THROG, our simulation engine, takes its name from a superhero hybrid that crosses Thor with a frog (yes, this actually exists)
Triad, our greenfield engine, takes its name from the oldest known species of frogs – Triadobatrachus. You can think of it as the starting point for the evolution of all frogs, and it serves as a great starting point for modeling projects too!
Dart, our risk engine, takes its name from the infamous poison dart frog. Just as you would want to be aware of a poisonous frog’s presence, you’ll also want to be sure to evaluate any opportunities for risks to present themselves.
Dendro, our simulation evolutionary algorithm, takes its name from what is known to be the smartest species of frog – Dendrobates auratus. These frogs have the ability to create complex mental maps to evaluate and better navigate their surroundings.
Hopper, our transportation routing engine, doesn’t have a name rooted in frog-related biology but rather a visual of a frog hopping along from stop to stop just as you might see with a multi-dro
…（省略）


---
## Optilogic Platform Overview
**URL:** https://optilogic.com/resources/help-center/docs/optilogic-platform-overview

Thank you for using the most powerful supply chain design software in the galaxy (I mean, as far as we know).
To see the highlights of the software please watch the following video.
Thank you for using the most powerful supply chain design software in the galaxy (I mean, as far as we know).
To see the highlights of the software please watch the following video.


---
## Optilogic Teams – Administrator Guide
**URL:** https://optilogic.com/resources/help-center/docs/optilogic-teams---administrator-guide

Teams is an exciting new feature set on the Optilogic platform designed to enhance collaboration within Supply Chain Design, enabling companies to foster a more connected and efficient working environment. With Teams, users can join a shared workspace where all team members have seamless access to collective models and files. For a more elaborate introduction to and high-level overview of the Teams feature set, please see this “Getting Started with Optilogic Teams” help center article.
This guide will walk Administrators through the steps to set up their organization and create Teams within the Optilogic platform. For non-administrator users, there is also an “Optilogic Teams – User Guide” help center article available.
Step 1: Establishing Your Organization
To begin, reach out to Optilogic Support at support@optilogic.com and let them know you would like to create your company’s Organization. Once they respond, they will ask you two key questions:
Which Optilogic accounts should be designated as Organization Administrators?
Which email domains should be associated with your organization?
These questions help us determine who should have access to the Organization Dashboard, where organization administrators (“Org Admins”) can manage users, create Teams, invite Members, and more. Specifying your company’s domains also enables us to pre-populate a list of potential users—saving you time by not having to invite each colleague individually.
Once this information is confirmed, our development team will create your organization. When complete, you will be able to log in and begin using the Teams functionality.
Step 2: Overview of the Organization Dashboard
If you have been assigned as an Organization Administrator, you can access the Organization Dashboard from the dropdown menu under your username in the top-right corner of the Optilogic platform. Click your name, then select Teams Admin from the list:
This will take you to your Organization Dashboard, where you can manage Teams and their Members.
Teams Application for Org Admins
We will first look at the Teams application within the Organization Dashboard. Here, all the organization’s teams are listed and can be managed. It will look similar to the following screenshot:
The Toolbar shows that we are in the Organization Dashboard of the organization called “Optilogic Tech Preview”.
There are 2 applications available, Teams and Members, we will first cover the Teams application, which is selected currently.
Admins can quickly search for teams with certain text in their team names in the search box at the top of the Teams application.
New teams can be created here by clicking on the Create Team button. Creating new teams will be covered in detail in the “Creating a New Team” section further below.
Teams can be viewed in Card View format, like shown here, or List View format, which we will see an example of further down in this section too.
The 2 teams that were filtered out by the “cf” search, CF Test 
…（省略）


---
## Optilogic Teams – User Guide
**URL:** https://optilogic.com/resources/help-center/docs/optilogic-teams---user-guide

Teams is an exciting new feature set on the Optilogic platform designed to enhance collaboration within Supply Chain Design, enabling companies to foster a more connected and efficient working environment. With Teams, users can join a shared workspace where all team members have seamless access to collective models and files. For a more elaborate introduction to and high-level overview of the Teams feature set, please see this “Getting Started with Teams” help center article.
This guide will cover how to use and take advantage of the Teams functionality on the Optilogic Platform.
For organization administrators (Org Admins), there is an “Optilogic Teams – Administrator Guide” help center article available. The Admin guide details how Org Admins can create new Teams & change existing ones, and how they can add new Members and update existing ones.
When your organization decides to start using the Teams functionality on the Optilogic platform, they will appoint one or multiple users to be the organizations’s administrators (Org Admin) who will create the Teams and add Members to these teams. Once an Org Admin has added you to a team, you will see a new application called Team Hub when logged in on the Optilogic platform. You will also receive a notification on the Optilogic platform about having been added to a team:
Note that it is possible to invite people from outside an organization to join one of your organization’s teams. Think for example of granting access to a contractor who is temporarily working on a specific project that involves modelling in Cosmic Frog. An Org Admin can invite this person to a specific team, see the “Optilogic Teams – Administrator Guide” help center article on how to do this. If someone is invited to join a team, and they are not part of that organization, they will receive an email invitation to the team. The following screenshots show this from the perspective of the user who is being invited to join a team of an organization they are not part of.
The user will receive an email similar to the one shown below. In this case the user is invited to the “Onboarding” team.
Clicking on the “Click here” link will open a new browser tab where user can confirm to join the team they are invited to by clicking on the Join Team button:
After clicking on the Join Team button, user will be prompted to login to the Optilogic platform or to create an account if they do not have one already. Once logged in, they are part of the team they were invited to and they will see the Team Hub application (see next section).
They will also see a notification in their Optilogic account:
Clicking on the notifications bell icon at the top right of the Optilogic platform will open the notifications list. There will be an entry for the invite the user received to join the Onboarding team.
Should an Org Admin have deleted the invitation before the user accepts the invite, they will get the message “Failed to activate the invite” when clicking on th
…（省略）


---
## Optimization Sourcing Policies Explained
**URL:** https://optilogic.com/resources/help-center/docs/optimization-sourcing-policies-explained

Optimization (NEO) will read from all 5 of input tables in the Sourcing section of Cosmic Frog.
We are able to use these tables to define the sourcing logic that describes costs and where a product can be introduced into the network through production at a Facility (Production Policies) or by way of a Supplier (Supplier Capabilities). We can also define additional rules around how a product must be sourced using the Max Sourcing Range and Optimization Policy fields in the Customer Fulfillment, Replenishment, and Procurement Policies tables.
The Max Sourcing Range field can be used to specify the maximum flow distance allowed for a listed location / product combination. If flow distances are not specified in the Distance field of the Transportation Policies table, a straight-line distance will be calculated based on the Origin / Destination geocoordinates. This will take into account the Circuity Factor specified in the Model Settings as a multiplication factor to estimate real road distances. Any transportation distances that exceed the Max Sourcing Range will result in the arcs being dropped from consideration.
There are 4 allowable entries for Optimization Policy. For any given Destination / Product combination, only a single Optimization Policy entry will be supported meaning you can not have one source listed with a policy of Single Source and another as By Ratio (Auto Scale).
This is the default entry that will be used if nothing is specified. To Optimize places no additional logic onto the sourcing requirement and will use the least cost option available.
For the listed destination / product combination, only one of the possible sources can be selected.
This option allows for sources to be split by the defined ratios that are entered into the Optimization Policy Value field. All of the entries into this Policy Value field will be automatically scaled, and the flow ratios will be followed for all inbound flow to the listed destination / product combination.
For example, there are 3 potential sources for a single Customer location. There is a flow split enforced of 50-30-20 from DC_1, DC_2, DC_3 respectively. This can be entered as Policy Values of 50, 30, and 20:
The same sourcing logic could be achieved by entering values of 5, 3, 2 or even 15, 9, 6. All values will be automatically scaled for each valid source that has been defined for a destination / product combination.
Similar to the Auto Scale option, By Ratio (No Scale) allows for sources to be split by the defined ratios entered into the Optimization Policy Value field. However, no scaling will be performed and the Optimization Policy Value fields will be treated as absolute sourcing percentages where an entry of 50 means that exactly 50% of the inbound flow will come from the listed source.
For example, there are 3 possible sources for a single Customer location and we want to enforce that DC_1 will account for exactly 50% of the flow while the remainder can come from any valid loca
…（省略）


---
## Resolving ODBC Connection Errors
**URL:** https://optilogic.com/resources/help-center/docs/resolving-odbc-connection-errors

There can be many different causes for an ODBC connection error, this article contains a couple of specific error messages along with resolution steps.
Resolution: Please make sure that the updated PSQL driver has been installed. This can be checked through your ODBC Data Sources Administrator
Latest versions of the drivers are located here: https://www.postgresql.org/ftp/odbc/releases/ from here, click on the latest parent folder, which as of June 20, 2024 will be REL-16_00_0005. Select and download the psqlodbc_x64.msi file. When installing, use the default settings from the installation wizard.
Resolution: Please confirm the PSQL drivers are updated as shown in the previous resolution. If this error is being thrown while running an Alteryx workflow specifically, please disable the AMP Engine for the Alteryx workflow.
There can be many different causes for an ODBC connection error, this article contains a couple of specific error messages along with resolution steps.
Resolution: Please make sure that the updated PSQL driver has been installed. This can be checked through your ODBC Data Sources Administrator
Latest versions of the drivers are located here: https://www.postgresql.org/ftp/odbc/releases/ from here, click on the latest parent folder, which as of June 20, 2024 will be REL-16_00_0005. Select and download the psqlodbc_x64.msi file. When installing, use the default settings from the installation wizard.
Resolution: Please confirm the PSQL drivers are updated as shown in the previous resolution. If this error is being thrown while running an Alteryx workflow specifically, please disable the AMP Engine for the Alteryx workflow.


---
## Resource Size Selection Guidance
**URL:** https://optilogic.com/resources/help-center/docs/resource-size-selection-guidance-neo

When running models in Cosmic Frog, users can choose the size of the resource the model’s scenario(s) will be run on in terms of available memory (RAM in Gb) and number of CPU cores. Depending on the complexity of the model and the number of elements, policies and constraints in the model, the model will need a certain amount of memory to run to completion successfully. Bigger, more complex models typically need to be run using a resource that has more memory (RAM) available as compared to smaller, less complex models. The bigger the resource that is being used, the higher the billing factor which leads to using more of the available cloud compute hours available to the customer (the total amount of cloud compute time available to the customer is part of customer’s Master License Agreement with Optilogic). Ideally, users choose a resource size that is just big enough to run their scenario(s) without the resource running out of memory, while minimizing the amount of cloud compute time used. This document guides users in choosing an initial resource size and periodically re-evaluating it to ensure optimal usage of the customer’s available cloud compute time.
Once a model has been built and the user is ready to run 1 or multiple scenarios, they can click on the green Run button at the right top in Cosmic Frog which opens the Run Settings screen. The Run Settings screen is documented in the Running Models & Scenarios in Cosmic Frog Help Center article. On the right-hand side of the Run Settings screen, user can select the Resource Size that will be used for the scenario(s) that are being kicked off to run:
In this section, we will guide users on choosing an initial resource size for the different engines in Cosmic Frog, based on some model properties. Before diving in, please keep following in mind:
There are quite a few model factors that influence how much memory a scenario needs to solve a Neo run. These include the number of model elements, policies, periods, and constraints. The type(s) of constraints used may play a role too. The main factors, in order of impact on memory usage, are:
These numbers are those after expansion of any grouped records and application of scenario items, if any.
The number of lanes can depend on the Lane Creation Rule setting in the Neo (Optimization) Parameters:
Note that for lane creation, expansion of grouped records and application of scenario item(s) need to be taken into account too to get at the number of lanes considered in the scenario run.
Users can use the following list to choose an initial resource size for Neo runs. First, calculate the number of demand records multiplied with the number of lanes in your model (after expansion of grouped records and application of scenario items). Next, find the range in the list, and use the associated recommended initial resource size:
# demand records * # lanes: Recommended Initial Resource Size
A good indicator for Throg and Dendro runs to base the initial resource si
…（省略）


---
## Running a Model in Atlas/Python
**URL:** https://optilogic.com/resources/help-center/docs/running-a-model-in-atlas-python

Running a model is simple and easy. Just click the run button and watch your Python model execute. Watch the video to learn more.
To leverage the power of hyperscaling, click the “Run as Job” button.
Running a model is simple and easy. Just click the run button and watch your Python model execute. Watch the video to learn more.
To leverage the power of hyperscaling, click the “Run as Job” button.


---
## Running a Model in the Optilogic Software Development Kit (SDK)
**URL:** https://optilogic.com/resources/help-center/docs/running-a-model-in-the-optilogic-software-development-kit-sdk

Running a model from Atlas via the SDK requires the following inputs:
Model data can be stored in two common locations:
1. Cosmic Frog model (denoted by a .frog suffix) stored within Postgres SQL database in the platform
2. .CSV files stored within Atlas
For #1 simply enter the database name within single quotes. For example to run a model called Satellite_Sleep I will need to enter this data in the run_model.py file
For #2 you will need to create a folder within Atlas to store your .CSV modeling files:
Each Atlas account is loaded with a run_model.py file located within the SDK folder in your Model Library
Double click the file to open it within Atlas and enter the following data:
Running a model from Atlas via the SDK requires the following inputs:
Model data can be stored in two common locations:
1. Cosmic Frog model (denoted by a .frog suffix) stored within Postgres SQL database in the platform
2. .CSV files stored within Atlas
For #1 simply enter the database name within single quotes. For example to run a model called Satellite_Sleep I will need to enter this data in the run_model.py file
For #2 you will need to create a folder within Atlas to store your .CSV modeling files:
Each Atlas account is loaded with a run_model.py file located within the SDK folder in your Model Library
Double click the file to open it within Atlas and enter the following data:


---
## Running Models & Scenarios in Cosmic Frog
**URL:** https://optilogic.com/resources/help-center/docs/running-models-scenarios-in-cosmic-frog

When a Cosmic Frog model has been built and scenarios of interest have been created, it is usually time to run 1 or multiple scenarios. This documentation covers how scenarios can be kicked off, and which run parameters can be configured by users.
Model Run Screen
When ready to run scenarios, users can click on the green Run button at the right top of the Cosmic Frog screen:
This will bring up the Run Settings screen:
We are on the Run Settings screen.
On the left-hand side of the screen a list of all scenarios contained in the model is shown. Users can select 1 or multiple of these to be run.
To facilitate finding specific scenarios in the list, text can be typed into the search box to filter the scenario list down to scenarios that contain the typed text in their name.
Clicking on this icon with the horizontal bars allows the user to sort the scenario list. Two sort options are available:
Default: the scenarios are listed in the order they were added to the model (i.e. the same order as they are in in the Scenarios module).
A-Z Name: this sorts the scenario list in alphabetical order. Clicking on this sort option again results in sorting the list in reverse alphabetical order.
These are the 5 icons associated with each of the Cosmic Frog engines. From left to right: network optimization (Neo), simulation (Throg), inventory (Dendro), Greenfield (Triad), and transportation optimization (Hopper). These icons are shown here for reference only.
The checkbox at the top of the scenario list can be used to check / un-check all scenarios that are showing in the list simultaneously.
Each scenario has an icon in front of it to show which engine will be used to run this scenario. These match the ones discussed under bullet number 5. The 2 scenario icons outlined in green are a Greenfield and a network optimization scenario, respectively. The other scenario icon outlined in green further down the list is an inventory scenario.
At the bottom of the scenario list the number of selected scenarios is listed. Here none are selected yet.
The user can select the Resource Size that they deem most appropriate for the scenarios to be run with. Larger resource sizes have more CPUs and more RAM available; however, they also have higher billing factors. Therefore, the aim is usually to choose a resource size as small as possible to limit the time billed for running the scenarios, while still being large enough for the scenarios to not run out of memory. More guidance on Resource Size selection and assessment can be found in this help article "Resource Size Selection Guidance"; a link to this article is provided underneath the drop-down list too.
For each engine, run parameters are available for configuration by users. We will go through these for each engine in the following sections of this documentation. Note that no parameters are available here for Greenfield runs; parameters to run Greenfield scenarios are all specified in the Greenfield Settings input table, which
…（省略）


---
## Sensitivity at Scale Scenarios in Cosmic Frog
**URL:** https://optilogic.com/resources/help-center/docs/sensitivity-at-scale-scenarios-in-cosmic-frog

One of Cosmic Frog’s great competitive features is the ability to quickly run many sensitivity analysis scenarios in parallel on Optilogic’s Cloud-based platform. This built-in Sensitivity at Scale (S@S) functionality lets a user run sensitivity on demand quantity and transportation costs with 1 click of a button, on any scenario using any of Cosmic Frog’s engines. In this documentation, we will walk through how to kick-off a S@S run, where to track the status of the scenarios, and show some example outputs of S@S scenarios once they have completed running.
Kicking off a S@S analysis is simply done by clicking on the green S@S button on the right-hand side in the toolbar at the top of Cosmic Frog:
After clicking on the S@S button, the Run Sensitivity at Scale screen comes up:
Please note that the parameters that are configured on the Run Settings screen (which comes up when clicking on the Run button at the right top of Cosmic Frog) are used for the Sensitivity at Scale scenario runs.
The scenarios are then created in the model, and we can review their setup by switching to the Scenarios module within Cosmic Frog:
As an example of the sensitivity scenario items that are being created and assigned to the sensitivity scenarios as part of the S@S process, let us have a look at one of these newly created scenario items:
Once the sensitivity scenarios have been created, they are kicked off to all be run simultaneously. Users can have a look in the Run Manager application on the Optilogic platform to track their progress:
Once a S@S scenario finishes, its outputs are available for review in Cosmic Frog. As with other models and scenarios, users can review outputs through output tables, maps, and graphs/charts/dashboards in the Analytics module. Here we will just show the Optimization Network Summary output table and a cost comparison chart as example outputs. Depending on the model and technology run, users may want to look at different outputs to best understand them.
To understand how the costs are divided over the different cost types and how they compare by scenario, we can look at following Supply Chain Cost Detail graph in the Analytics module:
One of Cosmic Frog’s great competitive features is the ability to quickly run many sensitivity analysis scenarios in parallel on Optilogic’s Cloud-based platform. This built-in Sensitivity at Scale (S@S) functionality lets a user run sensitivity on demand quantity and transportation costs with 1 click of a button, on any scenario using any of Cosmic Frog’s engines. In this documentation, we will walk through how to kick-off a S@S run, where to track the status of the scenarios, and show some example outputs of S@S scenarios once they have completed running.
Kicking off a S@S analysis is simply done by clicking on the green S@S button on the right-hand side in the toolbar at the top of Cosmic Frog:
After clicking on the S@S button, the Run Sensitivity at Scale screen comes up:
Please note that the parameter
…（省略）


---
## Setting Up a Visualization Database
**URL:** https://optilogic.com/resources/help-center/docs/setting-up-a-visualization-database

The data for our visualizations comes from our Cosmic Frog model database. This is often stored in the cloud using a unique identifier.
We can decide if we want to use Optilogic servers to do our data computations, or if we want the computations to be performed locally.
Next, we must decide which table we want to use for our visualization. Generally, the results of running our model are stored in the “optimization” tables, so it can be helpful to use search for this to see output data. However, we can also use tables containing input data if desired.
We can also preview the data in a table using the magnifying glass button:
The data for our visualizations comes from our Cosmic Frog model database. This is often stored in the cloud using a unique identifier.
We can decide if we want to use Optilogic servers to do our data computations, or if we want the computations to be performed locally.
Next, we must decide which table we want to use for our visualization. Generally, the results of running our model are stored in the “optimization” tables, so it can be helpful to use search for this to see output data. However, we can also use tables containing input data if desired.
We can also preview the data in a table using the magnifying glass button:


---
## Setup: Scripting with Python for Cosmic Frog and DataStar
**URL:** https://optilogic.com/resources/help-center/docs/setup-scripting-with-python-for-cosmic-frog-and-datastar

Optilogic has developed Python libraries to facilitate scripting for 2 of its flagship applications: Cosmic Frog, the most powerful supply chain design tool on the market, and DataStar, its just released AI-powered data product where users can create flexible, accessible and repeatable workflows with zero learning curve.
Instead of going into the applications themselves to build and run supply chain models and data workflows, these libraries enable users to programmatically access their functionality and underlying data. Example use cases for such scripts are:
In this documentation we cover the basics of getting yourself set up so you can take advantage of these Python scripting libraries, both on a local computer and on the Optilogic platform leveraging the Lightning Editor application. More specific details for the cosmicfrog and datastar libraries, including examples and end-to-end scripts, are detailed in the following Help Center articles and library specifications:
Working locally with Python scripts has the advantage that you can make use of code completion features which may include text auto-completion, showing what arguments functions need, catching incorrect syntax/names, etc. An example set up to achieve this is for example one where Python, Visual Studio Code, and an IntelliSense extension package for Python for Visual Studio Code are installed locally:
Once you are set up locally and are starting to work with Python scripts in Visual Studio Code, you will need to install the Python libraries you want to use to have access to their functionality. You do this by typing following in a terminal in Visual Studio Code (if no terminal is open yet: click on the View menu at the top and select Terminal, or the keyboard shortcut Ctrl + ` can be used):
When installing these libraries, multiple external libraries (dependencies) are installed too. These are required to run the packages successfully and/or make working with them easier. These include the optilogic, pandas, and SQLAlchemy packages (among others) for both libraries. You can find out which packages are installed with the cosmicfrog / ol-datastar libraries by typing “pip show cosmicfrog” or “pip show ol-datastar" in a terminal.
To use other Python libraries in addition, you will usually need to install them using “pip install” too before you can leverage them.
If you want to access certain items on the Optilogic platform (like Cosmic Frog models, DataStar project sandboxes) while working locally, you will need to whitelist your IP address on the platform, so the connections are not blocked by a firewall. You can do this yourself on the Optilogic platform:
Please note that for working with DataStar, the whitelisting of your IP address is only necessary if you want to access the Project Sandbox of projects directly through scripts. You do not need to whitelist your IP address to leverage other functions while scripting, like creating projects, adding macros and their tasks, and running
…（省略）


---
## Shelf Life and Maturation Time (Network Optimization)
**URL:** https://optilogic.com/resources/help-center/docs/shelf-life-and-maturation-time-network-optimization

Cosmic Frog’s network optimization engine (Neo) can now account for shelf life and maturation time of products out of the box with the addition of several fields to the Products input table. The age of product that is used in production, product which flows between locations, and product sitting in inventory is now also reported in 3 new output tables, so users have 100% visibility into the age of their products across the operations.
In this documentation, we will give a brief overview of the new features first and then walk through a small demo model, which users can copy from the Resource Library, showing both shelf life and maturation time using 3 scenarios.
The new feature set consists of:
Please note that:
We will now showcase the use of both Shelf Life and Maturation Time in a small demo model. This model can be copied to your own Optilogic account from the Resource Library (see also the “How to use the Resource Library” Help Center article). This model has 3 locations which are shown on the map below:
It is a multi-period model with 6 periods, which are each 1 week long (the Model End Date is set to February 12, 2025, on the Model Settings input table, not shown):
There are 3 products included the model: 2 finished goods, Product_1 and Product_2, and 1 raw material, named Component. The component is used in a bill of materials to produce Product_1, as we will see in the screenshots after this one.
As mentioned above, a bill of materials is used to produce finished good Product_1:
This bill of materials is named BOM_1 and it specifies that 10 units of the product named Component are used as an input (product type = Component) of this bill of materials. Note that the bill of materials does not indicate the end product that is produced with it. This is specified by associating production policies with a BOM. To learn more about detailed production modelling using the Neo engine, please see this Help Center article.
In the next screenshot of the production policies table, we see that the plant can produce all 3 products, and that for the production of Product_1, the bill of materials shown in the previous screenshot, BOM_1, is used. The cost per unit is set to 1 here for each product:
For purposes of showing how Shelf Life and Maturation Time work, we will use the Production Policies Multi-Time Period input table too. In here we override the production cost per unit that we just saw in the above screenshot to become increasingly expensive in later periods for all products, adding $1 per unit for each next period. So, to produce a unit of Product_1 in Period_1 costs $1, in Period_2 it costs $2, in Period_3 $3, etc. Same for Component and Product_2:
The production cost is increased here to encourage the model to produce product as early as possible, so that it incurs the lowest possible production cost. It will also still need to respect the shelf life and maturation time requirements. Note that this is also weighed against the increased invent
…（省略）


---
## Special Characters in Cosmic Frog
**URL:** https://optilogic.com/resources/help-center/docs/special-characters-in-cosmic-frog

The use of non alpha-numeric characters can present the possibilities of data issues when running scenarios. The only special characters that will be officially supported are periods, dashes, parentheses and underscores.
Please note that while other special characters in input data or scenario names can still function as expected, we can not guarantee that they will always work. If you encounter any issues or have questions about the data being used, please feel free to contact support at support@optilogic.com.
The use of non alpha-numeric characters can present the possibilities of data issues when running scenarios. The only special characters that will be officially supported are periods, dashes, parentheses and underscores.
Please note that while other special characters in input data or scenario names can still function as expected, we can not guarantee that they will always work. If you encounter any issues or have questions about the data being used, please feel free to contact support at support@optilogic.com.


---
## SQL Editor Overview
**URL:** https://optilogic.com/resources/help-center/docs/sql-editor-overview

The SQL Editor helps users write, edit, and execute SQL (Structured Query Language) queries within Optilogic’s platform. It provides direct access to database objects such as tables and views stored within the platform. In this documentation, the Anura Supply Chain Model Database (Cosmic Frog’s database) will be used as the database example.
Anura model exploration and editing are enabled through the three windows of the SQL Editor:
The Anura database is stored in PostgreSQL and exclusively supports PostgreSQL query statements to ensure optimized performance. Visit https://www.postgresql.org/ for more detailed information.
To enable the SQL editor, select a table or view from a database. Once selected, the SQL Editor will prepopulate a Select query, and the Metadata Explorer displays the table schema to enable initial data exploration.
The Database Browser offers several tools to explore your databases and display key information.
The Query Editor enables users to create and execute custom SQL queries and view the results. Reserved words are highlighted in blue to assist in SQL editing. This window is not enabled until a model table or view has been selected from the database browser; once selected, the user is able to customize this query to run in the context of the selected database.
The Metadata Explorer provides a set of tools to efficiently create and store SQL queries.
SQL is a powerful language that allows you to manipulate and transform tabular data. The query basics overview will help guide you through creating basic SQL queries.
Example 1: Filter Criteria - Customers with status set to include without latitude
SELECT A.CustomerName, A.Status, A.Region
FROM customers A
Where A.Latitude IS NOT NULL and A.Status = ‘Include’
Example 2: Summarizing Records - Regions with 2 or more geocoded customers
SELECT A.Region, A.Status, Count(*) AS Cnt
FROM customers A
Where A.Latitude IS NOT NULL
Group By A.Region, A.Status
Having Count(*) > 1
Order by Cnt DescOften, your model analysis will require you to use data stored in more than one table. To include multiple tables in a single SQL query, you will have to use table joins to list the tables and their relationships.
If you are unsure if all joined values are present in both tables, leverage a Left or Right join to ensure you don’t unintentionally exclude records.
Example 1: Inner Join - Join Customer Demand and Customers to add Region to Demand
SELECT A.CustomerName, A.ProductName, B.Region, A.Quantity
FROM customerdemand A INNER JOIN Customers B
  on A.CustomerName = B.CustomerName
Example 2: Left Join - Find Customer Demand records missing Customer record
SELECT A.CustomerName, A.ProductName, B.Region, A.Quantity
FROM customerdemand A Left JOIN Customers B
  on A.CustomerName = B.CustomerName
Where B.CustomerName is Null
Example 3: Inner Join & Aggregation – Summarize Demand by Region
SELECT B.Region, A.ProductName, SUM(Cast (A.Quantity as Int)) Quantity
FROM customerdemand A INNER JOIN Custome
…（省略）


---
## Territory Planning (Transportation Optimization)
**URL:** https://optilogic.com/resources/help-center/docs/territory-planning-transportation-optimization

Territory Planning is a new capability in the Transportation Optimization (Hopper) engine that automatically clusters customers into geographic regions - territories - and restricts routes and drivers to operate within those territory boundaries. This reduces operational complexity, improves route consistency, and enables delivery-promise logic for end consumers.
Territory Planning is available today in Cosmic Frog for all users and is powered by an enhanced high-precision Genetic Algorithm. Please note that all Hopper models, whether using the new Territory Planning features or not, can now be run using this high-precision mode.
This "How-To Tutorial: Territory Planning" video explains the new feature:
In this documentation we will first cover the benefits of Territory Planning, next explain how it works in Cosmic Frog, and then take you through an example model showcasing the new feature.
Traditional routing optimization focuses on building the most cost-efficient set of routes. In many real-world operations, however, drivers do not cross territories. A driver consistently serving the same neighborhoods knows the roads, customer patterns, and service requirements.
Key benefits include:
With the Territory Planning feature one new Hopper input table and two new Hopper output tables are introduced.
Territory Planning requires one new input table, Territory Planning Settings, while supporting all existing Hopper tables. This table defines the characteristics and constraints of the territories to be created during the Hopper solve, and can be found in the Functional Tables section: 1. Territory Type: A descriptive name for the territory configuration (e.g., "Large Territories", "Balanced Small Territories").
The universal compatibility with all other Hopper tables ensures you can add territory planning to any existing Hopper model without needing to restructure your data.
Territory Planning generates two new output tables, the Transportation Territory Planning Summary and the Transportation Territory Assignment Summary, in addition to all standard Hopper outputs. The Transportation Territory Planning Summary table provides one record per territory with aggregate KPIs:
This table is useful for:
The Transportation Territory Assignment Summary table shows the detailed assignment of each customer to a territory:
This table enables:
Besides the 2 new output tables, the following existing transportation output tables have new fields Territory Name and Territory Type added to them: Routes Map Layer, Transportation Asset Summary, Transportation Segment Summary, and Transportation Stop Summary. This facilitates filtering on territories in these tables to for example quickly see which assets are used in which territories.
Territory Planning uses Hopper's advanced genetic algorithm to simultaneously optimize multiple objectives:
The genetic algorithm is available in Hopper's High Precision solver mode and powers all Hopper optimizations, not just territory pla
…（省略）


---
## Throg – Simulation Distribution Syntax
**URL:** https://optilogic.com/resources/help-center/docs/throg---simulation-distribution-syntax

Several input columns used by Throg (Simulation) will accept distributions as inputs. The following distributions, along with their syntax, are currently supported by Throg:
A user-defined Histogram is also supported as an acceptable input. These will be defined in the Histograms input table, and to reference a histogram in an allowed input column simply put in the Histogram Name.
Several input columns used by Throg (Simulation) will accept distributions as inputs. The following distributions, along with their syntax, are currently supported by Throg:
A user-defined Histogram is also supported as an acceptable input. These will be defined in the Histograms input table, and to reference a histogram in an allowed input column simply put in the Histogram Name.


---
## Transportation Costs in Optimization
**URL:** https://optilogic.com/resources/help-center/docs/transportation-costs-in-optimization

Here we will cover the options a Cosmic Frog user has for modeling transportation costs when using the Neo Optimization engine. The different fields that can be populated and how the calculations under the hood work will be explained in detail.
There are many ways in which transportation can be costed in real life supply chains. The Transportation Policies table contains 4 cost fields to help users model costs as close as possible to reality. These fields are: Unit Cost, Fixed Cost, Duty Rate and Inventory Carrying Cost Percentage. Not all these costs need to be used: the one(s) that are applicable should be populated and the others can be left blank. The way some of these costs work depends on additional information specified in other fields, which will be explained as well.
Note that in the screenshots throughout this documentation some fields in the Cosmic Frog tables have been moved so they could be shown together in a screenshot. You may need to scroll right to see the same fields in your Cosmic Frog model tables and they may be in a different order.
We will first discuss the input fields with the calculations and some examples; at the end of the document an overview is given of how the cost inputs translate to outputs in the optimization output tables.
This field is used for transportation costs that increase when the amount of product being transported increases and/or the transportation distance or time increases. As there are quite a few different measures based on which costs can depend on the amount of product that is transported (e.g. $2 per each, or $0.01 per each per mile, or $10 per mile for a whole shipment of 1000 units, etc.) there is a Unit Cost UOM field that specifies how the cost specified in the Unit Cost field should be applied. In a couple of cases, the Average Shipment Size and Average Shipment Size UOM fields must be specified too as we need to know the total number of shipments for the total Unit Cost calculation. The following table provides an overview of the Unit Cost UOM options and explains how the total Unit Costs are calculated for each UOM:
With the settings as in the screenshot above, total Unit Costs will be calculated as follows for beds, pillows, and alarm clocks going from DC_Reno to CUST_Phoenix:
The Unit Cost field can contain a single numeric value (as in the examples above), a step cost specified in the Step Costs table, a rate specified in the Transportation Rates table, or a custom cost function.
If stepped costs are used as the Unit Cost for Transportation Policies that use Groups in the Product Name field, then the Product Name Group Behavior field determines how these stepped costs are applied:
See following screenshots for an example of using stepped costs in the Unit Cost field and the difference in cost calculations for when Product Name Group Behavior is set to Enumerate vs Aggregate:
On the Step Costs table (screenshot above), the stepped costs we will be using in the Unit Cost field on the T
…（省略）


---
## Trouble Receiving Account Confirmation Email
**URL:** https://optilogic.com/resources/help-center/docs/trouble-receiving-account-confirmation-email

A confirmation email is sent following account creation, however this email could potentially be blocked due to an organization’s IT policies. If you are failing to receive your confirmation email, please make sure that www.optilogic.com is whitelisted, as well as the following email address: support=www.optilogic.com@mail.www.optilogic.com.
If possible, please request that a wildcard whitelist be established for all URL’s that end in *.optilogic.app.
After confirming that these have been whitelisted, try and send another confirmation email. If the problem persists, please send a note in to support@optilogic.com.
A confirmation email is sent following account creation, however this email could potentially be blocked due to an organization’s IT policies. If you are failing to receive your confirmation email, please make sure that www.optilogic.com is whitelisted, as well as the following email address: support=www.optilogic.com@mail.www.optilogic.com.
If possible, please request that a wildcard whitelist be established for all URL’s that end in *.optilogic.app.
After confirming that these have been whitelisted, try and send another confirmation email. If the problem persists, please send a note in to support@optilogic.com.


---
## Troubleshooting Model Failure Messages
**URL:** https://optilogic.com/resources/help-center/docs/troubleshooting-model-failure-messages

Please find a list of model errors that might appear in the Job Error Log and their associated resolutions.
Resolution – Please check to see if a scenario item was built where an action does not reference a column name. Scenario Actions should be of the form ColumnName = …..
Resolution – Please check to see if there is a string in the scenario condition that is missing an apostrophe to start or close the string
Resolution – This indicates an intermittent drop in connection when reading / writing to the database. Re-running the scenario should resolve this error. If the error persists, please reach out to support@optilogic.com.
Please find a list of model errors that might appear in the Job Error Log and their associated resolutions.
Resolution – Please check to see if a scenario item was built where an action does not reference a column name. Scenario Actions should be of the form ColumnName = …..
Resolution – Please check to see if there is a string in the scenario condition that is missing an apostrophe to start or close the string
Resolution – This indicates an intermittent drop in connection when reading / writing to the database. Re-running the scenario should resolve this error. If the error persists, please reach out to support@optilogic.com.


---
## Troubleshooting Resource Library Excel Apps
**URL:** https://optilogic.com/resources/help-center/docs/troubleshooting-resource-library-excel-apps

When downloading all of the related files for any of the sample Excel Apps that are posted to our Resource Library, you will likely encounter macro-enabled Excel workbooks (.xlsm) which might have their macros disabled following download.
To enable the macros, you can right-click on the Excel file in a File Explorer and select the option for Properties. In the Properties menu, check the box in the Security section to Unblock the file and then hit Apply.
You can then re-open the document and should see the macros are now enabled.
Some of the Excel templates also make use of add-ins to help expand the workbook’s capabilities. An example of this is the ArcGIS add-in which allows for map visuals to be created directly in the workbook. It is possible that these add-ins might be disabled by default in the Microsoft Office settings, if that is the case you should see an error message as follows:
This can be resolved by updating your Privacy Settings under your Microsoft Office Account page. To access this menu, click into File > Account > Account Privacy > Manage Settings. You will then want to make sure that in the Optional Connected Experiences, the option to Turn on optional connected experiences is enabled.
Updating this value will require a restart of Microsoft Office. Once the restart is completed, you should see that the add-ins are now enabled and working as expected.
If other issues come from any Resource Library templates please do not hesitate to reach out to support@optilogic.com.
When downloading all of the related files for any of the sample Excel Apps that are posted to our Resource Library, you will likely encounter macro-enabled Excel workbooks (.xlsm) which might have their macros disabled following download.
To enable the macros, you can right-click on the Excel file in a File Explorer and select the option for Properties. In the Properties menu, check the box in the Security section to Unblock the file and then hit Apply.
You can then re-open the document and should see the macros are now enabled.
Some of the Excel templates also make use of add-ins to help expand the workbook’s capabilities. An example of this is the ArcGIS add-in which allows for map visuals to be created directly in the workbook. It is possible that these add-ins might be disabled by default in the Microsoft Office settings, if that is the case you should see an error message as follows:
This can be resolved by updating your Privacy Settings under your Microsoft Office Account page. To access this menu, click into File > Account > Account Privacy > Manage Settings. You will then want to make sure that in the Optional Connected Experiences, the option to Turn on optional connected experiences is enabled.
Updating this value will require a restart of Microsoft Office. Once the restart is completed, you should see that the add-ins are now enabled and working as expected.
If other issues come from any Resource Library templates please do not hesitate to reach out to s
…（省略）


---
## Troubleshooting: Unable to Open Cosmic Frog
**URL:** https://optilogic.com/resources/help-center/docs/troubleshooting-unable-to-open-cosmic-frog

If you are seeing a "Something went wrong" error when trying to open a model in Cosmic Frog — for example, Cannot read properties of undefined (reading 'call') — this is likely caused by a cached version of the application conflicting with a recent platform update. Follow the steps below in order to resolve it.
A hard refresh forces the browser to bypass its cache and reload all files directly from the server. It clears the cache for that specific page only and ensures the latest version is loaded. This is the quickest fix for pages that have not updated properly and should be tried first.
Press the following keyboard shortcut to perform a hard refresh:
Once the page has reloaded, try opening your model again.
If the hard refresh does not resolve the issue, clearing your full browser cache will remove all stored files and force the browser to fetch the latest version of Cosmic Frog from the server.
Press the following keyboard shortcut to open the Clear Browsing Data menu:
In the menu that appears:
Once cleared, refresh the Cosmic Frog page and try opening your model again.
If neither step resolves the problem, please contact the Optilogic support team. Include your browser type and version, and a screenshot of the error if possible.
Email: support@optilogic.com
If you are seeing a "Something went wrong" error when trying to open a model in Cosmic Frog — for example, Cannot read properties of undefined (reading 'call') — this is likely caused by a cached version of the application conflicting with a recent platform update. Follow the steps below in order to resolve it.
A hard refresh forces the browser to bypass its cache and reload all files directly from the server. It clears the cache for that specific page only and ensures the latest version is loaded. This is the quickest fix for pages that have not updated properly and should be tried first.
Press the following keyboard shortcut to perform a hard refresh:
Once the page has reloaded, try opening your model again.
If the hard refresh does not resolve the issue, clearing your full browser cache will remove all stored files and force the browser to fetch the latest version of Cosmic Frog from the server.
Press the following keyboard shortcut to open the Clear Browsing Data menu:
In the menu that appears:
Once cleared, refresh the Cosmic Frog page and try opening your model again.
If neither step resolves the problem, please contact the Optilogic support team. Include your browser type and version, and a screenshot of the error if possible.
Email: support@optilogic.com


---
## Troubleshooting with Linear Programming Output Files
**URL:** https://optilogic.com/resources/help-center/docs/troubleshooting-with-linear-programming-output-files

If you are comfortable with traditional linear programming techniques, you can select the “Write Input Solver Files” and “Write LP File” parameters to get useful output files.
After running, these files are in your file explorer.
The “input_solver” folder has a list of all the tables that are entered into the optimization solver. This is useful for:
The “model.lp” file shows the model in a more traditional MIP optimization format, including the objective function and model constraints.
When using the Infeasibility Diagnostic engine, the LP file is different than a traditional Neo run. In this case, the cost coefficients in the objective function are set to 0. Instead, a positive cost coefficient is added to each slack constraint, and the goal of the model is to minimize the slack values. This allows us to find the “edge” of infeasibility.
If you are comfortable with traditional linear programming techniques, you can select the “Write Input Solver Files” and “Write LP File” parameters to get useful output files.
After running, these files are in your file explorer.
The “input_solver” folder has a list of all the tables that are entered into the optimization solver. This is useful for:
The “model.lp” file shows the model in a more traditional MIP optimization format, including the objective function and model constraints.
When using the Infeasibility Diagnostic engine, the LP file is different than a traditional Neo run. In this case, the cost coefficients in the objective function are set to 0. Instead, a positive cost coefficient is added to each slack constraint, and the goal of the model is to minimize the slack values. This allows us to find the “edge” of infeasibility.


---
## Troubleshooting with the Infeasibility Diagnostic Engine
**URL:** https://optilogic.com/resources/help-center/docs/troubleshooting-with-the-infeasibility-diagnostic-engine

When a scenario run is infeasible, it means that the solver cannot find any solutions that satisfy all the specified constraints simultaneously. In other words, the defined constraints are too restrictive or they contradict each other, making it impossible to satisfy all of them at once. Examples are:
If a Neo (network optimization) scenario run is infeasible, a user can tell from within Cosmic Frog and also by looking at the run's logs in the Run Manager application. Within Cosmic Frog, the Optimization Network Summary output table will show Solve Status = Infeasible and many other output columns, such as Solve Type and Solve Time, will be blank:
In the Run Manager application, also on the Optilogic Platform, users can select the scenario run, which will have Status = Error, and look at the run's logs on the right-hand side:
Running the check infeasibility tool is a great first step in identifying why a scenario is infeasible. It can allow the scenario to optimize even if the current constraints cause infeasibility. Generally, the tool will loosen constraints in the scenario, which allow it to solve. This means that the check infeasibility tool is solving an optimization problem focused on feasibility, not cost. The goal of this augmented model is to minimize how much the constraints are loosened, and therefore the tool can often find:
The Check Infeasibility tool is accessed via the model run options on the Run Settings screen:
When running the Check Infeasibility tool in this default manner, all constraints will be relaxed. Additional run parameters can be used to selectively choose which constraints can be relaxed during a Check Infeasibility run and which need to be enforced, see the "Infeasibility Parameters" section in the "Running Models & Scenarios" help center article. Especially in models where many different types of constraints are applied, this can help in determining which constraint(s) cause the infeasibility and how constraints interact with each other. An approach can be to run the Check Infeasibility tool a few times with different constraints enforced and then compare the results. It also lets users indicate to the solver which constraints are most important to satisfy by keeping those enforced, while others are allowed to be relaxed.
Once a Check Infeasibility run completes successfully, the results that are likely most helpful for identifying the infeasibility are found in the Optimization Constraint Summary output table. Users may need to filter for the scenario name in case this table contains results of multiple check infeasibility scenario runs. The following 2 screenshots show the 1 record in this table for the scenario called "Flow Constraint El Bajio 2M" scenario that returns infeasible as shown above. This first screenshot shows that the constraint in question is a Flow constraint that is applied on the lanes from the El Bajio Factory to a group of DCs named DCs Con:
Scrolling right in the table, we can see additiona
…（省略）


---
## Troubleshooting with Validation Errors
**URL:** https://optilogic.com/resources/help-center/docs/troubleshooting-with-validation-errors

After every Cosmic Frog run, it’s a great habit to check the OptimizationValidationErrorReport table. Even for models that run successfully, this table can have useful information on how the input data is being processed by the solver.
Key columns in the validation error report can tell you:
Validation errors that have “high” or “moderate” severity are likely to cause an infeasible model. In fact, Cosmic Frog has an “infeasibility checker” that looks for these kinds of errors and flags them before running the model to save you run time. 
In this example, there are no transportation lanes that can deliver beds to CUST_Phoenix, so demand cannot be fulfilled. The infeasibility checker finds this and stops the model run before it even tries to optimize.
A couple of examples of how we could fix this error:
The OutputValidationErrorReport table is often very useful, even if a model “successfully” runs. This table will catch potential errors that do not cause infeasibility but could change the model results. In this example, there is a typo in the CustomerDemand table for “CUST_Montgomery”. Here, the model drops that row in the demand table. This will not cause an infeasible model, as it just removes that demand constraint. However, it means that no product will be sent to this customer in our optimized result.
After every Cosmic Frog run, it’s a great habit to check the OptimizationValidationErrorReport table. Even for models that run successfully, this table can have useful information on how the input data is being processed by the solver.
Key columns in the validation error report can tell you:
Validation errors that have “high” or “moderate” severity are likely to cause an infeasible model. In fact, Cosmic Frog has an “infeasibility checker” that looks for these kinds of errors and flags them before running the model to save you run time. 
In this example, there are no transportation lanes that can deliver beds to CUST_Phoenix, so demand cannot be fulfilled. The infeasibility checker finds this and stops the model run before it even tries to optimize.
A couple of examples of how we could fix this error:
The OutputValidationErrorReport table is often very useful, even if a model “successfully” runs. This table will catch potential errors that do not cause infeasibility but could change the model results. In this example, there is a typo in the CustomerDemand table for “CUST_Montgomery”. Here, the model drops that row in the demand table. This will not cause an infeasible model, as it just removes that demand constraint. However, it means that no product will be sent to this customer in our optimized result.


---
## Understanding Anura: the Cosmic Frog Data Structure
**URL:** https://optilogic.com/resources/help-center/docs/understanding-anura-the-cosmic-frog-data-structure

The Anura data schema enables design in the Optilogic platform. It sits above the design algorithms to create a consistent modeling paradigm for our algorithms:
Anura is comprised of modeling categories required to build a model. Each modeling category contains tables to add pertinent detail and/or complexity to your model as well as identify structure, policies, costs, and constraints.
A complete list of the tables and fields within each table can be downloaded locally here.
The Anura data schema enables design in the Optilogic platform. It sits above the design algorithms to create a consistent modeling paradigm for our algorithms:
Anura is comprised of modeling categories required to build a model. Each modeling category contains tables to add pertinent detail and/or complexity to your model as well as identify structure, policies, costs, and constraints.
A complete list of the tables and fields within each table can be downloaded locally here.


---
## Understanding Lane Creation Rules
**URL:** https://optilogic.com/resources/help-center/docs/understanding-lane-creation-rules

Transportation lanes are a necessary part of any supply chain. These lanes represent how product flows throughout our supply chain. In network optimization, transportation lanes are often referred to as arcs or edges.
In general, lanes in our supply chain are generated from the transportation policies and sourcing policies provided in our data tables.
Transportation policies are stored in the TransportationPolicies table. Sourcing policies are stored in the following tables:
From the data in these tables, the software automatically generates the lanes (i.e. arcs or edges) in our network before sending it to the optimization solver. We can control how these lanes are generated as a parameter of our Neo model.
Neo models can follow 4 different lane creation policies:
If the “Transportation Policy Lanes Only” rule is selected, Cosmic Frog will only generate transportation lanes based on data in the TransportationPolicies table. If a lane between two sites is not explicitly defined here, product will not be able to directly flow between those sites. Note that any additional information specified in a Sourcing Policy table (unit cost, policy rule etc.) will still be respected for the lane so long as it exists in the Transportation Policies table.
If the “Sourcing Policy Lanes Only” rule is selected, Cosmic Frog will only generate transportation lanes based on data in the Sourcing tables. Even if an origin-destination path is defined in the TransportationPolicies table, product will not be able to flow via this lane unless there is a specific sourcing policy defining how the destination site gets product from the origin site. Note that any additional information specified in a Transportation Policies table (cost, policy rule, multiple modes etc.) will still be respected for the lane so long as it exists in a Sourcing Policy table.
If the “Intersection” rule is selected, Cosmic Frog will only generate transportation lanes if they are defined in both the transportation policy table and one of the sourcing policy tables.
For users converting models from Supply Chain Guru©, the default SCG© lane creation rule is “Intersection”.
If the “Union” rule is selected, Cosmic Frog will generate transportation lanes if they are defined in either the transportation policy table or one of the sourcing policy tables.
Transportation lanes are a necessary part of any supply chain. These lanes represent how product flows throughout our supply chain. In network optimization, transportation lanes are often referred to as arcs or edges.
In general, lanes in our supply chain are generated from the transportation policies and sourcing policies provided in our data tables.
Transportation policies are stored in the TransportationPolicies table. Sourcing policies are stored in the following tables:
From the data in these tables, the software automatically generates the lanes (i.e. arcs or edges) in our network before sending it to the optimization solver. We can control how these
…（省略）


---
## Understanding the Validation Error Report
**URL:** https://optilogic.com/resources/help-center/docs/understanding-the-validation-error-report

The validation error report table will be populated for all model solves and contains a lot of helpful information for both reviewing and troubleshooting models. A set of results will be saved for each scenario and every record will report the table and column where the issue has been identified, a description of the error, the value that was identified as the problem along with the action taken by the solver. In the instance where multiple records are generated for the same type of error, you will see an example record populated as the identified value and a count of the errors will be displayed – detailed records can be printed using debug mode. Each record will also be rated on the severity of its impact on a scale from 0 – 3 with 3 being the highest.
The validation error report can serve as a great tool to help troubleshoot an infeasible model. The best approach for utilizing this table is to first sort on the Severity column so that the highest level issues are displayed. If severity 3 issues are present, they must be addressed. If no severity 3 issues exist, the next steps would be to review any severity 2 issues to consider policy impact. It is also helpful to search for any instances where rows are being dropped as these dropped rows will likely influence other errors. To do this, filter the Action field for ‘Row Dropped’.
While the report can be helpful in trying to proactively diagnose infeasible models, it won’t always have all of the answers. To learn more about the dedicated engine for infeasibility diagnosis please check out this article: Troubleshooting With The Infeasibility Diagnostic Engine
Severity 3 records capture instances of syntax issues that are preventing the model from being built properly. This can be presented as 2 types:
Severity 3 records can also be instances where model infeasibility can be detected before the model solve begins, in the instance where a severity 3 error is detected the model solve will be cancelled immediately. There are 3 common instances of these Severity 3 errors:
Severity 2 records capture sources of potential infeasibility and while not always a definitive reason for a problem being infeasible, they will highlight potential issues with the policy structure of a model. There are 2 common instances of Severity 2 errors:
These severity 2 errors don’t necessarily indicate a problem, they can often times be caused by grouped-based policies and members overlapping from one group to another. It is still a good idea to review these gaps in policies and make sure that all of the lanes which should be considered in your solve are in fact being read into the solver.
Severity 1 records will capture issues in model data that can cause rows from input tables to be dropped when writing the solver files for a model. These can be issues on allowed numerical ranges, a negative quantity for customer demand as an example. Detailed policy linkages that do not align can also cause errors, for example a process whi
…（省略）


---
## Update connection string information for third-party tools (Alteryx, Tableau, PowerBI…)
**URL:** https://optilogic.com/resources/help-center/docs/update-connection-string-information-for-third-party-tools-alteryx-tableau-powerbi

‘Connection Info’ is required when connecting 3rd party tools such as Alteryx, Tableau, PowerBI, etc. to Cosmic Frog.
Anura version 2.7 makes use of Next-Gen database infrastructure. As a result, connection strings must be updated to maintain connectivity.
Severed connections will produce an error when connecting your 3rd party tool to Cosmic Frog.
Steps to restore connection:
Cosmic Frog ‘HOST’ value can be copied from Cloud Storage browser.
‘Connection Info’ is required when connecting 3rd party tools such as Alteryx, Tableau, PowerBI, etc. to Cosmic Frog.
Anura version 2.7 makes use of Next-Gen database infrastructure. As a result, connection strings must be updated to maintain connectivity.
Severed connections will produce an error when connecting your 3rd party tool to Cosmic Frog.
Steps to restore connection:
Cosmic Frog ‘HOST’ value can be copied from Cloud Storage browser.


---
## Uploading Data to Cosmic Frog from Alteryx
**URL:** https://optilogic.com/resources/help-center/docs/uploading-data-to-cosmic-frog-from-alteryx

The following instructions begin with the assumption that you have data that you wish to upload to your Cosmic Frog model.
The instructions below assume the user is adding information to the Suppliers table in the model database. This will use the same connection that was previously configured to download data from the Customers table.
Drag the “Output Data” action into the Workflow and click to select “Write to File or Database”
Select the relevant ODBC connection established earlier, in this example we called the connection “Alteryx Demo Model.”
You will be prompted to enter a valid table name to which the data will be written in the model database. In this example enter suppliers (all in lower case to match the table name in PostGres, which is case sensitive).
Click OK
Within the Options menu – edit “Output Options” to Append Existing in the drop-down list.
Within the Options menu – edit “Append Field Map” by clicking the three dots to see more options.
Select “Custom Mapping” option and then use the drop-down lists to map each field in the Destination column to the Source column. Fields of the same name, but case sensitive as it is PostGres.
Click OK
Now you can Run the Workflow to upload the data to your model. Once it has completed check the Suppliers table in Cosmic Frog to see the data.
The following instructions begin with the assumption that you have data that you wish to upload to your Cosmic Frog model.
The instructions below assume the user is adding information to the Suppliers table in the model database. This will use the same connection that was previously configured to download data from the Customers table.
Drag the “Output Data” action into the Workflow and click to select “Write to File or Database”
Select the relevant ODBC connection established earlier, in this example we called the connection “Alteryx Demo Model.”
You will be prompted to enter a valid table name to which the data will be written in the model database. In this example enter suppliers (all in lower case to match the table name in PostGres, which is case sensitive).
Click OK
Within the Options menu – edit “Output Options” to Append Existing in the drop-down list.
Within the Options menu – edit “Append Field Map” by clicking the three dots to see more options.
Select “Custom Mapping” option and then use the drop-down lists to map each field in the Destination column to the Source column. Fields of the same name, but case sensitive as it is PostGres.
Click OK
Now you can Run the Workflow to upload the data to your model. Once it has completed check the Suppliers table in Cosmic Frog to see the data.


---
## User-Defined Variables, Costs and Constraints (Transportation Optimization)
**URL:** https://optilogic.com/resources/help-center/docs/user-defined-variables-costs-and-constraints-transportation-optimization

User-defined variables (UDVs) are a transformative feature in Cosmic Frog’s transportation optimization algorithm (Hopper engine) that allow users to create and track custom metrics specific to their transportation needs. Once established, these variables can be seamlessly integrated into user-defined constraints and/or user-defined costs. Several example use cases are:
Before diving into Hopper’s user-defined variables, costs, and constraints, it is recommended users are familiar with the basics of building and running a Hopper model, see for example this “Getting Started with Hopper” help center article.
In this documentation, we will first describe the example model used to illustrate the UDV concepts in this help article. Next, we will cover the input and output tables available when working with user-defined variables, costs, and constraints. Finally, we will walk through the inputs and outputs of 4 UDV examples: the first two examples showcase the application of constraints to user-defined variables, while the last two examples cover how to model user-defined costs.
The characteristics of the model used to show the concepts of user-defined variables, costs, and constraints throughout this help article are as follows:
The optimized routes from the Baseline_UDV scenario are shown on this map, there are 10 routes with 10 stops each. The customers are color-coded based on the country they are in:
Filtering out the route which has stops in most countries, we find the following route which has stops on it in 4 countries Poland (1 dark blue stop), Czech Republic (7 yellow stops), Slovakia (1 orange stop), and Germany (1 red stop):
In the Input Tables part of Cosmic Frog’s Data module, there are 3 input tables in the Constraints section that can be used to configure user-defined variables, costs, and constraints:
We will take a closer look at each of these input tables now, and will also see more screenshots of these in the later sections that walk through several examples.
On this table we specify the term(s) of each variable which we wish to track or apply user-defined costs and/or constraints to. This first screenshot shows the fields which are used to define the variable, its term(s), and what the return condition is:
The next 2 screenshots show the other fields available on the Transportation User-Defined Variables input table, which are used to set the Filter Condition for the Scope. Note that several of these fields have accompanying Group Behavior fields, which are not shown in the screenshot. If a group name is used in the Asset Name, Site Name, Shipment ID, or Product Name field, the Group Behavior field specifies how the group should be interpreted: if the Group Behavior field is set to Aggregate (the default if not specified) the activity of the variable is summed over the members of the group, i.e. the variable is applied to the members of the group together. If the Group Behavior field is set to Enumerate, then an instance of the vari
…（省略）


---
## Using Alternate Geocoding Providers
**URL:** https://optilogic.com/resources/help-center/docs/using-alternate-geocoding-providers

By default, the Geocoding option in Cosmic Frog will use Mapbox as the geodata provider. Other supported providers will be Bing, Google, PTV and PC Miler. If you have an access key for an alternate provider and would like to configure this provider as the default option, follow these two steps:
1. Set up your geocoding key under your Account > Geoprovider Keys page
2. Once a new key has been created, set the key as the Default Provider to be used by clicking the Star icon next to the key. This key will now be used for Geocoding in Cosmic Frog
By default, the Geocoding option in Cosmic Frog will use Mapbox as the geodata provider. Other supported providers will be Bing, Google, PTV and PC Miler. If you have an access key for an alternate provider and would like to configure this provider as the default option, follow these two steps:
1. Set up your geocoding key under your Account > Geoprovider Keys page
2. Once a new key has been created, set the key as the Default Provider to be used by clicking the Star icon next to the key. This key will now be used for Geocoding in Cosmic Frog


---
## Using Analytics in Cosmic Frog
**URL:** https://optilogic.com/resources/help-center/docs/using-analytics-in-cosmic-frog

Fast, AI-driven supply chain decision orchestration for every individual and team —from strategic design to tactical planning.
Model, optimize, and simulate even the most complex supply chains at scale and trade off cost, service, risk, and sustainability.
Eliminate data challenges with AI-automated cleansing and workflow orchestration for decision-ready intelligence instantly.
Optilogic's breakthrough agentic AI system for supply chain design — compresses months of supply chain design work into a single day.
Purpose-built apps for every stakeholder — Deploy across your entire organization today. Act on insights from day one.
Stay updated on the latest from Optilogic.
Enhance your skills with our hands-on training sessions and courses.
Dive into expert insights, industry trends, and practical tips for success.
Discover Optilogic's partner network empowering transformation and supply chain success.
Discover on-demand interviews, demos, and customer sessions.
Find step-by-step guides, FAQs, and support.
Access our full library of guides, case studies, and tools to help you succeed.
Connect with Optilogic peers, exchange insights, and accelerate supply chain success.
Watch the video to learn how to build dashboards to analyze scenarios and tell the stories behind your Cosmic Frog models:


---
## Using Groups to Write Model Constraints
**URL:** https://optilogic.com/resources/help-center/docs/using-groups-to-write-model-constraints

Adding model constraints often requires us to take advantage of Cosmic Frog’s Groups feature. Using the Groups table, we can define groups of model elements. This allows us to reference several individual elements using just the group name.
In the example below, we have added the Harlingen, Ashland, and Memphis production sites to a group named “ProductionSites”.
Now, if we want to write a constraint that applies to all production sites, we only need to write a single constraint referencing the group.
When we reference a group in a constraint, we can choose to either aggregate or enumerate the constraint across the group.
If we aggregate the constraint, that means we want the constraint to apply to some aggregate statistic representing the entire group. For example, if we wanted the total number of pens produced across all production sites to be less than a certain value, we would aggregate this constraint across the group.
Enumerating a constraint across a group applies the constraint to each individual member of the group. This is useful if we want to avoid writing repetitive constraints. For example, if each production site had a maximum production limit of 400 pens, we could either write a constraint for each site or write a single constraint for the group. Compare the two images below to see how enumeration can help simplify our constraint tables.
Without enumeration:
With enumeration:
Adding model constraints often requires us to take advantage of Cosmic Frog’s Groups feature. Using the Groups table, we can define groups of model elements. This allows us to reference several individual elements using just the group name.
In the example below, we have added the Harlingen, Ashland, and Memphis production sites to a group named “ProductionSites”.
Now, if we want to write a constraint that applies to all production sites, we only need to write a single constraint referencing the group.
When we reference a group in a constraint, we can choose to either aggregate or enumerate the constraint across the group.
If we aggregate the constraint, that means we want the constraint to apply to some aggregate statistic representing the entire group. For example, if we wanted the total number of pens produced across all production sites to be less than a certain value, we would aggregate this constraint across the group.
Enumerating a constraint across a group applies the constraint to each individual member of the group. This is useful if we want to avoid writing repetitive constraints. For example, if each production site had a maximum production limit of 400 pens, we could either write a constraint for each site or write a single constraint for the group. Compare the two images below to see how enumeration can help simplify our constraint tables.
Without enumeration:
With enumeration:


---
## Using the Atlas File Explorer
**URL:** https://optilogic.com/resources/help-center/docs/using-the-atlas-file-explorer

The File Explorer is a fully functioning view into your workspace file system. To open the File Explorer, look for the following icon on the left-hand side of the Atlas environment:
To expand a folder to view its contents simply click anywhere on the folder, its label, or the expand icon (the small triangle next to the folder itself).
To collapse the folder you can either click on the same area again, or you can collapse all folders by clicking the button outlined below.
To open a file, navigate to it in the file explorer and double-click on it. Once done, the file will load into the editor. Please note that some files will not show properly in the editor, such as files that contain binary content or encrypted content.
There are two ways you can create a new file; through the file menu:
or via the file explorer context menu.
Keep in mind that the context you have selected in the file explorer is where the new folder will go, so if you want the folder underneath a specific other folder make sure to select that folder before you begin. That being said, if you forget you can still move the folder afterward.
To duplicate a file or folder, select the Duplicate command from the right-click context menu. This will create a copy of the file or folder in the same location with the suffix _copy.
To rename a file or folder, select the Rename command from the right-click context menu or use the hotkey F2 while the file or folder is selected. This will present a dialog where you can type in the new name that you want to use. Once specified, hit Enter or click the OK button to apply the new name.
To upload a file or files, make sure that you have a folder selected. From the right-click context menu select the Upload Files… command or select the same command from the file menu. Select the file or files from the file selection dialog and hit Enter or click the Open button. This will upload the selected files to the folder that you have selected.
To download a file or folder, select the Download command from the right-click context menu or the same command from the file menu. This will download the selected file or folder to your local machine. If you have selected a folder, the contents will be compressed into a .tar archive file. You will need to use a file archiving tool to extract the contents of the archive.
To save a file, select the Save option from the file menu or use the hotkey CTRL+S. This will save the changes in the file that has focus in the editor. Note, a file with focus will have the tab in the editor have the same background as the background of the editor itself. You can tell if a file needs to be saved by the presence of a white dot in the file header open in the editor.
You can delete a file or folder by selecting the Delete command from the right-click context menu or hitting the Delete key on your keyboard.
By default, the auto-save option is turned on. This means that your files will automatically save as you are editing them. You can turn
…（省略）


---
## Using the Cosmic Frog Python Library
**URL:** https://optilogic.com/resources/help-center/docs/using-the-cosmic-frog-python-library

Please feel free to download the Cosmic Frog Python Library PDF file. Please note that this library requires Python 3.11.
You can also reference the video shown below that covers an overview on scripting within Cosmic Frog.
Please feel free to download the Cosmic Frog Python Library PDF file. Please note that this library requires Python 3.11.
You can also reference the video shown below that covers an overview on scripting within Cosmic Frog.


---
## Using the DataStar Python Library
**URL:** https://optilogic.com/resources/help-center/docs/using-the-datastar-python-library

DataStar users can take advantage of the datastar Python library, which gives users access to DataStar projects, macros, tasks, and connections through Python scripts. This way users can build, access, and run their DataStar workflows programmatically. The library can be used in a user’s own Python environment (local or on the Optilogic platform), and it can also be used in Run Python tasks in a DataStar macro.
In this documentation we will cover how to use the library through multiple examples. At the end, we will step through an end-to-end script that creates a new project, adds a macro to the project, and creates multiple tasks that are added to the macro. The script then runs the macro while giving regular updates on its progress.
Before diving into the details of this article, it is recommended to read this “Setup: Python Scripts for Cosmic Frog and DataStar” article first; it explains what users need to do in terms of setup before they can run Python scripts using the datastar library. To learn more about the DataStar application itself, please see these articles on Optilogic’s Help Center.
Succinct documentation in PDF format of all datastar library functionality can be downloaded here (please note that the long character string at the beginning of the filename is expected). This includes a list of all available properties and methods for the Project, Macro, Task, and Connection classes at the end of the document.
All Python code that is shown in the screenshots throughout this documentation is available in the Appendix, so that you can copy-paste from there if you want to run the exact same code in your own Python environment and/or use these as jumping off points for your own scripts.
If you have reviewed the “Setup: Python Scripts for Cosmic Frog and DataStar” article and are set up with your local or online Python environment, we are ready to dive in! First, we will see how we can interrogate existing projects and macros using Python and the datastar library. We want to find out which DataStar projects are already present in the user’s Optilogic account.
Once the parentheses are typed, hover text comes up with information about this function. It tells us that the outcome of this method will be a list of strings, and the description of the method reads “Retrieve all project names visible to the authenticated user”. Most methods will have similar hover text describing the method, the arguments it takes and their default values, and the output format.
Now that we have a variable that contains the list of DataStar projects in the user account, we want to view the value of this variable:
Next, we want to dig one level deeper and for the “Import Historical Shipments” project find out what macros it contains:
Finally, we will retrieve the tasks this “Import Shipments” macro contains in a similar fashion:
In addition, we can have a quick look in the DataStar application to see that the information we are getting from the small scripts above ma
…（省略）


---
## Using the Minimum Required Tables
**URL:** https://optilogic.com/resources/help-center/docs/using-the-minimum-required-tables

Anura contains 100+ (and growing) input tables to organize modeling data.
There are six minimum required tables for every model:
This includes one table to identify the demand that must be met, two tables to lay out the structure, and a last table to link them all together with policies.
Most supply chain design models use at least one table each of the first five model categories (Modeling Elements, Sourcing, Inventory, Transportation, Demand). A Neo model converted from Supply Chain Guru© will generally contain the following tables:
By entering information in all of these tables you will have successfully added all demand, created all model elements, created sourcing and transportation policies for all arcs, and added an inventory policy to ensure inventory can be stored throughout the supply chain.
While not required, many Neo models will also contain data in the following tables:
Anura contains 100+ (and growing) input tables to organize modeling data.
There are six minimum required tables for every model:
This includes one table to identify the demand that must be met, two tables to lay out the structure, and a last table to link them all together with policies.
Most supply chain design models use at least one table each of the first five model categories (Modeling Elements, Sourcing, Inventory, Transportation, Demand). A Neo model converted from Supply Chain Guru© will generally contain the following tables:
By entering information in all of these tables you will have successfully added all demand, created all model elements, created sourcing and transportation policies for all arcs, and added an inventory policy to ensure inventory can be stored throughout the supply chain.
While not required, many Neo models will also contain data in the following tables:


---
## Using the SCG to Cosmic Frog Model Converter
**URL:** https://optilogic.com/resources/help-center/docs/using-the-scg-to-cosmic-frog-model-converter

The team at Optilogic has built a powerful tool to take existing Supply Chain Guru models from either a .scgm or .mdf format and convert them to the Optilogic Anura and .frog schema.
To try this feature click the three dots on the right side of your Home Screen to select SCG Converter icon.
This will take you to the converter page:
From here you will need to name your model and select the model you wish to convert. Then you will able to click the “Convert to Anura” button. Please do not click away from the browser tab as the model is uploading. After the upload is complete you will be redirected to another page while the model is converted to the Anura schema. At this time it is safe to click away from the page as your conversion will be in process.
Once the conversion is complete you will be redirected to the SQL Editor page where you can start executing queries on your new Anura database! You will notice that there are two schemas in the database: _original_scg and anura_2_8.
You can review the data from the original database under the _original_scg tables and can see the new transformed data under the anura_2_8 tables. You will also find a new table in the anura schema called ‘scg_conversion_log’ – this table will provide logging information from the conversion process to track where data transformations outside of the default schema took place, and will also note any warnings or issues that the converter ran into. A full list of column mappings can be found here.
The team at Optilogic has built a powerful tool to take existing Supply Chain Guru models from either a .scgm or .mdf format and convert them to the Optilogic Anura and .frog schema.
To try this feature click the three dots on the right side of your Home Screen to select SCG Converter icon.
This will take you to the converter page:
From here you will need to name your model and select the model you wish to convert. Then you will able to click the “Convert to Anura” button. Please do not click away from the browser tab as the model is uploading. After the upload is complete you will be redirected to another page while the model is converted to the Anura schema. At this time it is safe to click away from the page as your conversion will be in process.
Once the conversion is complete you will be redirected to the SQL Editor page where you can start executing queries on your new Anura database! You will notice that there are two schemas in the database: _original_scg and anura_2_8.
You can review the data from the original database under the _original_scg tables and can see the new transformed data under the anura_2_8 tables. You will also find a new table in the anura schema called ‘scg_conversion_log’ – this table will provide logging information from the conversion process to track where data transformations outside of the default schema took place, and will also note any warnings or issues that the converter ran into. A full list of column mappings can be found here.


---
## Waypoint Routes (Transportation and Network Optimization)
**URL:** https://optilogic.com/resources/help-center/docs/waypoint-routes-transportation-and-network-optimization

Cosmic Frog users can now visualize routes from Hopper (transportation optimization) and Neo (network optimization) on real road networks instead of straight lines. Valhalla, an open-source routing engine for OpenStreetMap, is used to calculate the waypoints.
This guide assumes familiarity with how to configure maps and their layers in Cosmic Frog. See the Getting Started with Maps help center article for the basics.
There are 2 tables available in the Table Name drop-down on the Condition Builder panel of a map layer for which waypoint routes can be generated:
In both cases the configuration is similar; first we will cover a Hopper example and then a Neo example.
Please note:
In our example case neither warning comes up, and the user turns on the Waypoint Routes option:
Processing time depends on the number of origin-destination pairs. As an indication, a larger Hopper model with ~3,000 routes took a little under 4 minutes to generate all waypoints.
Users can monitor the progress of the waypoint routes generation by opening the Model Activity panel:
Once the calculation completes, the map is updated to show the routes the waypoints have been calculated for on the road network:
In this Neo example, we will generate road network flows for the following DC to Customer flows. This represents 1,333 unique origin-destination pairs:
Once the waypoints have been calculated, the map updates and now looks as follows:
Cosmic Frog users can now visualize routes from Hopper (transportation optimization) and Neo (network optimization) on real road networks instead of straight lines. Valhalla, an open-source routing engine for OpenStreetMap, is used to calculate the waypoints.
This guide assumes familiarity with how to configure maps and their layers in Cosmic Frog. See the Getting Started with Maps help center article for the basics.
There are 2 tables available in the Table Name drop-down on the Condition Builder panel of a map layer for which waypoint routes can be generated:
In both cases the configuration is similar; first we will cover a Hopper example and then a Neo example.
Please note:
In our example case neither warning comes up, and the user turns on the Waypoint Routes option:
Processing time depends on the number of origin-destination pairs. As an indication, a larger Hopper model with ~3,000 routes took a little under 4 minutes to generate all waypoints.
Users can monitor the progress of the waypoint routes generation by opening the Model Activity panel:
Once the calculation completes, the map is updated to show the routes the waypoints have been calculated for on the road network:
In this Neo example, we will generate road network flows for the following DC to Customer flows. This represents 1,333 unique origin-destination pairs:
Once the waypoints have been calculated, the map updates and now looks as follows:


---
## Welcome to Optilogic!
**URL:** https://optilogic.com/resources/help-center/docs/welcome-to-optilogic

Thank you for using the most powerful Supply Chain Design software in the galaxy (I mean, as far as we know).
To see the highlights of the software please watch the following video.
Thank you for using the most powerful Supply Chain Design software in the galaxy (I mean, as far as we know).
To see the highlights of the software please watch the following video.


---
## Working with Data
**URL:** https://optilogic.com/resources/help-center/docs/working-with-data

Watch the video to learn how to import, export, geocode, and work with data within Cosmic Frog:
If you want to follow along, please download the data set available here:
Watch the video to learn how to import, export, geocode, and work with data within Cosmic Frog:
If you want to follow along, please download the data set available here:


---
## Working with Multi Time Period Tables
**URL:** https://optilogic.com/resources/help-center/docs/working-with-multi-time-period-tables

The Multi Time Period (MTP) tables allow for you to enter time-period specific data across many input tables. These MTP tables will act as overrides in the relevant periods for the records in their standard tables. If a record with the same key structure does not exist in the standard table, the MTP record won’t be recognized by the solver and will be dropped.
For example, we have a manufacturing facility with a throughput capacity of 1000 units. When this information is entered into the Facilities table, the throughput capacity will be used for each period in the model:
Let’s say that the manufacturing facility is expanding operations over the year and wants to show that the throughput capacity gradually increases over each quarter. This adjustment in throughput capacity can be defined in the Facilities Multi Time Period table:
We can see that the throughput capacity increased over time and given the constant outbound quantity, the throughput utilization goes down as the model progresses.
In all of the policy multi-time period tables, there are two fields which appear to be similar – Status and Policy Status.
For example, we have 2 manufacturing locations that can produce the same product at very different costs. We’ll see that the MFG location is used as the sole production option as it is far cheaper.
Now let’s say that we have to shut production down at the MFG location for maintenance in Q3, we can do this through the Production Policies Multi Time Period table:
This can be a quick way to to adjust policies over different times and is an alternative to using constraints. The use of Policy Status in place of constraints will stop the creation of extra solver variables as well as reducing the number of constraints being placed over the solution. This can help contribute to better model performance.
Similar to how Status and Policy Status work, you have the ability to change the operating status of a Facility and a Work Center over time. This would allow you to Open, Close, or Consider the use of a Facility or Work Center in any given period.
Using the same example as above, we can model the maintenance at MFG during Q3 by closing the entire location:
Closing the entire facility will do more than just limit production, the facility is then completely removed from the network for that given period and no other activities can take place.
The Multi Time Period (MTP) tables allow for you to enter time-period specific data across many input tables. These MTP tables will act as overrides in the relevant periods for the records in their standard tables. If a record with the same key structure does not exist in the standard table, the MTP record won’t be recognized by the solver and will be dropped.
For example, we have a manufacturing facility with a throughput capacity of 1000 units. When this information is entered into the Facilities table, the throughput capacity will be used for each period in the model:
Let’s say that the manufacturing facility 
…（省略）


---
## Writing Scenario Syntax
**URL:** https://optilogic.com/resources/help-center/docs/writing-scenario-syntax

To describe the action and conditions of our scenario, there are specific syntax rules we need to follow.
In this example, we are editing the Facilities table to define a scenario without a distribution center in Detroit.
Actions describe how we want to change a table. Actions have 2 components:
Writing actions takes the form of an equation:
Further detail on action syntax can be found here.
Conditions describe what we want to change. They are Boolean (i.e. true/false) statements describing which rows to edit. Conditions have 3 components:
Conditions take the form of a comparison, such as:
To describe the action and conditions of our scenario, there are specific syntax rules we need to follow.
In this example, we are editing the Facilities table to define a scenario without a distribution center in Detroit.
Actions describe how we want to change a table. Actions have 2 components:
Writing actions takes the form of an equation:
Further detail on action syntax can be found here.
Conditions describe what we want to change. They are Boolean (i.e. true/false) statements describing which rows to edit. Conditions have 3 components:
Conditions take the form of a comparison, such as:


---
## Writing Syntax for Actions
**URL:** https://optilogic.com/resources/help-center/docs/writing-syntax-for-actions

For a review of Actions related to Scenarios please refer to the article here. Writing actions take the form of an equation:
If you are ever doubting the name of a column that needs to be used in an action, you can type CTRL+SPACE to have the full list of columns available to you displayed. Alternatively, you can start typing and the valid column names will auto-complete.
When assigning numerical values to a column, we can use mathematical operators such as +, -, *, and /. Likewise you can use parenthesis to establish a preferred order of operations. Below are some examples of the syntax.
When assigning numerical values to a column we can use mathematical operators such as +, -, *, and /. Likewise you can use parentheses to establish a preferred order of operations as shown in the following examples.
When assigning string values to a column you must use single quotation marks to reference any string that is not a column name. Some examples of changing values with a string are included in the examples below:
For a review of Actions related to Scenarios please refer to the article here. Writing actions take the form of an equation:
If you are ever doubting the name of a column that needs to be used in an action, you can type CTRL+SPACE to have the full list of columns available to you displayed. Alternatively, you can start typing and the valid column names will auto-complete.
When assigning numerical values to a column, we can use mathematical operators such as +, -, *, and /. Likewise you can use parenthesis to establish a preferred order of operations. Below are some examples of the syntax.
When assigning numerical values to a column we can use mathematical operators such as +, -, *, and /. Likewise you can use parentheses to establish a preferred order of operations as shown in the following examples.
When assigning string values to a column you must use single quotation marks to reference any string that is not a column name. Some examples of changing values with a string are included in the examples below:


---
## Writing Syntax for Conditions
**URL:** https://optilogic.com/resources/help-center/docs/writing-syntax-for-conditions

For a review of Conditions related to Scenarios please refer to the article here. Conditions, in Scenarios, take the form of a comparison that can create a filter in your table structure.
If you are ever doubting the name of a column that needs to be used in an action, you can type CTRL+SPACE to have the full list of columns available to you displayed. Alternatively, you can start typing and the valid column names will auto-complete.
Standard comparison operators include: =, >, <, >=, <=, !=. You can also use the LIKE or NOT LIKE operators and the % or * values for wildcards for string comparisons. The % and * wildcard operators are equivalent within Cosmic Frog (though, best practice is to use the % wildcard symbol since this is valid in the database code). If you have multiple conditions, the use of AND / OR operators are supported. The IN operator is also supported for comparing strings.
Cosmic Frog will color code syntax with the following logic:
Following are some examples of valid condition syntax:
For a review of Conditions related to Scenarios please refer to the article here. Conditions, in Scenarios, take the form of a comparison that can create a filter in your table structure.
If you are ever doubting the name of a column that needs to be used in an action, you can type CTRL+SPACE to have the full list of columns available to you displayed. Alternatively, you can start typing and the valid column names will auto-complete.
Standard comparison operators include: =, >, <, >=, <=, !=. You can also use the LIKE or NOT LIKE operators and the % or * values for wildcards for string comparisons. The % and * wildcard operators are equivalent within Cosmic Frog (though, best practice is to use the % wildcard symbol since this is valid in the database code). If you have multiple conditions, the use of AND / OR operators are supported. The IN operator is also supported for comparing strings.
Cosmic Frog will color code syntax with the following logic:
Following are some examples of valid condition syntax:


---
## Getting Started with Optilogic
**URL:** https://optilogic.com/resources/help-center/getting-started-with-optilogic

Fast, AI-driven supply chain decision orchestration for every individual and team —from strategic design to tactical planning.
Model, optimize, and simulate even the most complex supply chains at scale and trade off cost, service, risk, and sustainability.
Eliminate data challenges with AI-automated cleansing and workflow orchestration for decision-ready intelligence instantly.
Optilogic's breakthrough agentic AI system for supply chain design — compresses months of supply chain design work into a single day.
Purpose-built apps for every stakeholder — Deploy across your entire organization today. Act on insights from day one.
Stay updated on the latest from Optilogic.
Enhance your skills with our hands-on training sessions and courses.
Dive into expert insights, industry trends, and practical tips for success.
Discover Optilogic's partner network empowering transformation and supply chain success.
Discover on-demand interviews, demos, and customer sessions.
Find step-by-step guides, FAQs, and support.
Access our full library of guides, case studies, and tools to help you succeed.
Connect with Optilogic peers, exchange insights, and accelerate supply chain success.


---
## Knowledge Library
**URL:** https://optilogic.com/resources/help-center/knowledge-library

The Model Output Insights Agent helps users investigate and analyze Cosmic Frog model outputs by turning analytical questions into structured, data-backed strategic reports. It breaks down complex questions into a step-by-step exploration plan, executes targeted queries, synthesizes findings, and produces a professional report - complete with visualizations and actionable recommendations.
This documentation describes how this specific agent works and can be configured. Please see the “AI Agents: Architecture and Components” Help Center article if you are interested in understanding how the Optilogic AI Agents work at a detailed level.
Extracting meaningful insights from large databases typically requires exploring and analyzing many output tables which can take a lot of time and effort. The Model Output Insights Agent streamlines the process, helping users get to the insights quicker than ever before.
Main skills the Model Output Insights Agent uses:
Supporting capabilities:
The agent can be accessed through the Run AI Agent task in DataStar. Once a Run AI Agent task is added to the macro, first the Model Output Insights Agent needs to be selected from the list of available agents and utilities in the "Select Utility" section:
Next, the inputs and settings for the task can be specified in the Configure Utility, Run Configuration, and Notes sections:
This next screenshot shows how to get a Folder Path while in the Explorer application: 1) right-click on the folder in the Explorer, 2) hover over Copy in the context menu, and 3) click on Folder Path:
After the run, a report in both markdown (.md) and pdf (.pdf) format and charts (if any) are created and can be found in the Explorer with the specified file name and folder. Once clicked, the file is opened in the Lightning Editor application for review.
Note that currently the charts are only included in the markdown file as a file name. Users can look for the charts in the Charts folder in the targeted output directory.
The Data Cleansing Agent is one of Ada’s AI-powered assistants. It helps users profile, clean, and standardize their database data without writing code. Users describe what they want in plain English -- such as "find and fix postal code issues in the customers table" or "standardize date formats in the orders table to ISO" -- and the agent autonomously discovers issues, creates safe working copies of the data, applies the appropriate fixes, and verifies the results. The agent handles common supply chain data problems including mixed date formats, inconsistent country codes, Excel-corrupted postal codes, missing values, outliers, and messy text fields. It expects a connected database with one or more tables as input. The output is a set of cleaned copies of their tables in the database which users can immediately use for Cosmic Frog model building, reporting, or further analysis, while the original data is preserved untouched for comparison or rollback.
This documentation describes how
…（省略）


---
## Navigating Ada - Agentic AI
**URL:** https://optilogic.com/resources/help-center/navigating-ada-agentic-ai

Fast, AI-driven supply chain decision orchestration for every individual and team —from strategic design to tactical planning.
Model, optimize, and simulate even the most complex supply chains at scale and trade off cost, service, risk, and sustainability.
Eliminate data challenges with AI-automated cleansing and workflow orchestration for decision-ready intelligence instantly.
Optilogic's breakthrough agentic AI system for supply chain design — compresses months of supply chain design work into a single day.
Purpose-built apps for every stakeholder — Deploy across your entire organization today. Act on insights from day one.
Stay updated on the latest from Optilogic.
Enhance your skills with our hands-on training sessions and courses.
Dive into expert insights, industry trends, and practical tips for success.
Discover Optilogic's partner network empowering transformation and supply chain success.
Discover on-demand interviews, demos, and customer sessions.
Find step-by-step guides, FAQs, and support.
Access our full library of guides, case studies, and tools to help you succeed.
Connect with Optilogic peers, exchange insights, and accelerate supply chain success.


---
## Navigating Atlas
**URL:** https://optilogic.com/resources/help-center/navigating-atlas

Fast, AI-driven supply chain decision orchestration for every individual and team —from strategic design to tactical planning.
Model, optimize, and simulate even the most complex supply chains at scale and trade off cost, service, risk, and sustainability.
Eliminate data challenges with AI-automated cleansing and workflow orchestration for decision-ready intelligence instantly.
Optilogic's breakthrough agentic AI system for supply chain design — compresses months of supply chain design work into a single day.
Purpose-built apps for every stakeholder — Deploy across your entire organization today. Act on insights from day one.
Stay updated on the latest from Optilogic.
Enhance your skills with our hands-on training sessions and courses.
Dive into expert insights, industry trends, and practical tips for success.
Discover Optilogic's partner network empowering transformation and supply chain success.
Discover on-demand interviews, demos, and customer sessions.
Find step-by-step guides, FAQs, and support.
Access our full library of guides, case studies, and tools to help you succeed.
Connect with Optilogic peers, exchange insights, and accelerate supply chain success.


---
## Navigating Cosmic Frog
**URL:** https://optilogic.com/resources/help-center/navigating-cosmic-frog

Fast, AI-driven supply chain decision orchestration for every individual and team —from strategic design to tactical planning.
Model, optimize, and simulate even the most complex supply chains at scale and trade off cost, service, risk, and sustainability.
Eliminate data challenges with AI-automated cleansing and workflow orchestration for decision-ready intelligence instantly.
Optilogic's breakthrough agentic AI system for supply chain design — compresses months of supply chain design work into a single day.
Purpose-built apps for every stakeholder — Deploy across your entire organization today. Act on insights from day one.
Stay updated on the latest from Optilogic.
Enhance your skills with our hands-on training sessions and courses.
Dive into expert insights, industry trends, and practical tips for success.
Discover Optilogic's partner network empowering transformation and supply chain success.
Discover on-demand interviews, demos, and customer sessions.
Find step-by-step guides, FAQs, and support.
Access our full library of guides, case studies, and tools to help you succeed.
Connect with Optilogic peers, exchange insights, and accelerate supply chain success.


---
## Navigating DataStar
**URL:** https://optilogic.com/resources/help-center/navigating-datastar

Fast, AI-driven supply chain decision orchestration for every individual and team —from strategic design to tactical planning.
Model, optimize, and simulate even the most complex supply chains at scale and trade off cost, service, risk, and sustainability.
Eliminate data challenges with AI-automated cleansing and workflow orchestration for decision-ready intelligence instantly.
Optilogic's breakthrough agentic AI system for supply chain design — compresses months of supply chain design work into a single day.
Purpose-built apps for every stakeholder — Deploy across your entire organization today. Act on insights from day one.
Stay updated on the latest from Optilogic.
Enhance your skills with our hands-on training sessions and courses.
Dive into expert insights, industry trends, and practical tips for success.
Discover Optilogic's partner network empowering transformation and supply chain success.
Discover on-demand interviews, demos, and customer sessions.
Find step-by-step guides, FAQs, and support.
Access our full library of guides, case studies, and tools to help you succeed.
Connect with Optilogic peers, exchange insights, and accelerate supply chain success.


---
## Navigating the Supply Chain Design Kit (SDK)
**URL:** https://optilogic.com/resources/help-center/navigating-the-supply-chain-design-kit-sdk

Fast, AI-driven supply chain decision orchestration for every individual and team —from strategic design to tactical planning.
Model, optimize, and simulate even the most complex supply chains at scale and trade off cost, service, risk, and sustainability.
Eliminate data challenges with AI-automated cleansing and workflow orchestration for decision-ready intelligence instantly.
Optilogic's breakthrough agentic AI system for supply chain design — compresses months of supply chain design work into a single day.
Purpose-built apps for every stakeholder — Deploy across your entire organization today. Act on insights from day one.
Stay updated on the latest from Optilogic.
Enhance your skills with our hands-on training sessions and courses.
Dive into expert insights, industry trends, and practical tips for success.
Discover Optilogic's partner network empowering transformation and supply chain success.
Discover on-demand interviews, demos, and customer sessions.
Find step-by-step guides, FAQs, and support.
Access our full library of guides, case studies, and tools to help you succeed.
Connect with Optilogic peers, exchange insights, and accelerate supply chain success.


---
## Troubleshooting
**URL:** https://optilogic.com/resources/help-center/troubleshooting

Fast, AI-driven supply chain decision orchestration for every individual and team —from strategic design to tactical planning.
Model, optimize, and simulate even the most complex supply chains at scale and trade off cost, service, risk, and sustainability.
Eliminate data challenges with AI-automated cleansing and workflow orchestration for decision-ready intelligence instantly.
Optilogic's breakthrough agentic AI system for supply chain design — compresses months of supply chain design work into a single day.
Purpose-built apps for every stakeholder — Deploy across your entire organization today. Act on insights from day one.
Stay updated on the latest from Optilogic.
Enhance your skills with our hands-on training sessions and courses.
Dive into expert insights, industry trends, and practical tips for success.
Discover Optilogic's partner network empowering transformation and supply chain success.
Discover on-demand interviews, demos, and customer sessions.
Find step-by-step guides, FAQs, and support.
Access our full library of guides, case studies, and tools to help you succeed.
Connect with Optilogic peers, exchange insights, and accelerate supply chain success.
