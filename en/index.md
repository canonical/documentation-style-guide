# Canonical Documentation Style Guide

![Product logo](../media/logo.svg)

This is an as yet incomplete guide to the language and style conventions used
for Canonical documentation projects. Topics are listed in the navigation
to the left, and presented here as a single page to aid searching.


## Diátaxis

Use Diátaxis to structure product documentation.
Diátaxis provides rules that help you identify the type of document that you are writing.
Document types include:

- Tutorial
- How-to guide
- Reference
- Explanation

Each type serves a different user need — it is useful to understand the needs being
addressed as these will influence the documentation approach.

Refer to the [official Diátaxis website](https://diataxis.fr/) for more information.

## Spelling

Canonical previously used UK English, but has changed to US English. There are
many small differences between UK and US English, but for the most part it comes
down to spelling.

<!-- RULE
#01 Spelling suggestions for English words
-->
Some common differences are:

|            UK English               |    US English                     |
|-------------------------------------|-----------------------------------|
|  license (verb) licence (noun)      | license (verb) license (noun)     |
|  defence (noun)                     | defense (noun)                    |
|  sausages, beans and mash           | sausages, beans, and mash         |
| programme (TV, agenda) program (IT) | program (TV, agenda) program (IT) |
|              per cent               | percent                           |
|   sceptical                         | skeptical                         |
|   catalogue                         | catalog                           |
|   travelling                        |    traveling                      |
|   labelled                          |    labeled                        |
|  -eable                             |    -able                          |
|  -ise                               |    -ize                           |
|  -our                               |    -or                            |

In the most part this can be mitigated by simply enabling spell checking
on your editing software and choosing an **en-us** dictionary. The minor
differences in grammar will (hopefully) be picked up in review by the
documentation team.

### Other common terms

<!-- RULE
#02 Spelling suggestions for common terms
-->

We would like to standardise on the following spellings for common
technology terms:

 - email
 - online
 - setup (noun), set up (verb)
 - backup (noun), back up (verb)
 - login (noun), log in (verb)
 - web
 - website
 - internet
 - systems management
 - virtualization
 - space-separated, comma-delimited
 - load balancer (only upper case as part of proper name e.g. Elastic Load Balancer)

## Branding

Consistency in branding is important for a number of reasons, including the protection of trademarks where they apply.
For our own products, and those of others we mention frequently, the following guidance applies.

### Ubuntu

When we refer to Ubuntu |oǒ'boǒntoō|, we are usually referring to the distribution, rather than the Ubuntu project itself.

Our convention is to use the name, followed by the release number and, if applicable, 'LTS' to denote that the version
is in Long Term Support. Optionally, you may also further identify the release by its codename (the first or both parts
of the release name) if this is likely to be useful (e.g. some of our products also use the release names to identify
versions).

<!-- RULE
#03 Correct use of Ubuntu versions
-->
Some examples of correct usage:

- **Ubuntu 22.04 LTS**
- **Ubuntu 22.10**
- **Ubuntu 23.04 (Lunar Lobster)** _(note case!)_
- **Ubuntu 23.10 (Mantic)**
- **Ubuntu 24.04 LTS (Noble Numbat)**

This also follows on to more specific products, e.g.

**Ubuntu Server 22.04 LTS**

In cases where the release may be mentioned many times in a single document, it is up to the author's judgement whether this
could be reworded or replaced by simply 'Ubuntu' on subsequent mentions.

Note also that when referring to releases in the general sense, it is "_**an**_ Ubuntu release".

<!-- RULE
#04 Correct use of Canonical product names
-->

### Other Canonical products

| Product           |  Notes                        |
|-------------------|-------------------------------|
| Anbox Cloud       |                               |
| Charmed Kubeflow  |                               |
| COS               | Canonical Observability Stack |
| Juju              |                               |
| Landscape         |                               |
| Launchpad         |                               |
| LXD               |                               |
| MAAS              | Metal As A Service            |
| MicroCeph         |                               |
| MicroCloud        |                               |
| MicroK8s          |                               |
| MicroOVN          |                               |
| MicroStack        |                               |
| Mir               |                               |
| Multipass         |                               |
| Snapcraft         |                               |
| snapd             |                               |
| Ubuntu Core       |                               |
| Ubuntu Pro        |                               |
| Ubuntu Server     |                               |

<!-- RULE
#05 Correct use of external product names
-->

### Other commonly referenced products/projects

| Product           | Notes                         |
|-------------------|-------------------------------|
| NVIDIA            |                               |
| OpenStack         |                               |
| PostgreSQL        |                               |
| Kubernetes        |                               |

## Contractions

Contractions are very common in spoken English and in many types of writing.
Avoiding the use of them entirely makes it difficult to achieve a friendly,
conversational tone. However, we should keep to contractions that are commonly
understood and not part of some regional dialect, and only use them in
"conversational" parts of the documentation (i.e. explanatory text).

### Contractions you can use

| contraction | meaning           | notes                         |
|-------------|-------------------|-------------------------------|
|aren't       |are not            |                               |
|can't        |cannot             |                               |
|could've     |could have         |                               |
|couldn't     |could not          |                               |
|didn't       |did not            |                               |
|doesn't      |does not           |                               |
|don't        |do not             |                               |
|hadn't       |had not            |                               |
|hasn't       |has not            |                               |
|haven't      |have not           |                               |
|it's         |it has / it is     |                               |
|isn't        |is not             |                               |
|mustn't      |must not           |                               |
|o'clock      |of the clock       |                               |
|wasn't       | was not           |                               |
|we'll 	      |we will            |                               |
|we're 	      |we are             |                               |
|we've 	      |we have            |                               |
|won't 	      |will not           |                               |
|would've     |would have         |                               |
|wouldn't     |would not          |                               |
|you'd        |you had /you would |                               |
|you'll       |you shall /you will|                               |
|you're       |you are            |                               |
|you've       |you have           |                               |

<!-- RULE
#06 Forbidden contractions
-->
### Don't use these!

| contraction | meaning       | notes
|-------------|---------------|-----------------------------------|
| ain't       | is not        | colloquial - use isn't            |
|how'd 	      |how did / how would|                               |
|how'll       |	how will      |                                   |
| I'd         | I would       | We don't use first person!        |
|'twas 	      | it was        | only relevant in Christmas fables |
|something's  | something is  | avoid - confusion with possessive |
|mayn't       |may not        |                                   |
|may've       |may have       |                                   |
|mightn't     |might not      |                                   |
|might've     |might have     |                                   |
|gonna 	      |going to       |                                   |
|gotta 	      |got to         |                                   |

## Headings

Headings are important for navigation, for setting tone and for search indexing. Please bear
in mind the following:

<!-- RULE
#07 Use sentence case in headings
-->
### Sentence case

All headings and headlines should be sentence case. This means that you
should only capitalise the first word unless it falls into one of the categories
outlined below:

 - product names
 - personal names
 - company names
 - brands
 - places
 - Ubuntu Server, not Ubuntu server

**Use:** Do more with Ubuntu
**Don't use:** Do More With Ubuntu

If it is not the actual product name, it should not be capitalised. Never capitalise keywords, technical terms and jargon.

<!-- RULE
#08 Headings must not end in '.'
-->
<!-- RULE
#09 Headings should not contain links
-->
<!-- RULE
#10 Headings should not contain code
-->
<!-- RULE
#11 Headings should not be followed by a subheading
-->
### Other considerations

 - Avoid overusing punctuation in headings. Headings should not end with a period/full point/full stop
 - Avoid links in headings
 - Don't overuse `code` styling in headings - it can be useful to document command references, for example, but you should always consider if it is really needed
 - Imperatives should be used for 'How to...' style docs instead of gerunds (i.e. "Create an instance" rather than "Creating an instance")
 - Do not skip levels of heading hierarchy (e.g. following an h1/# with an h3/###)
 - Headings require content and should not be followed directly by a subheading


<!-- RULE
#12 Dates should follow '1 January 1970' format
-->
## Dates

For consistency, we will use the following date format:

 - Single day: 1 January 2013
 - Date range within same month: 1-2 January 2013
 - Date range across two or more months: 1 January - 2 February 2013

<!-- RULE
#13 Numbers below 10 should be spelled out
-->
<!-- RULE
#14 Numbers above 9 should be written in the '1,970' format
-->
## Numbers

Numbers in single figures should be spelled out in most cases. From
10 onwards, numbers should be written in digits.

Exceptions to this rule include numbered lists and units of measurement.

When writing out numbers over the 100s, remember to include commas.

**Use:** 7,000

**Don't use:** 7000

<!-- RULE
#15 Do not use $/# prompts in code blocks
-->
<!-- RULE
#16 Avoid inlining comments in code blocks
-->
<!-- RULE
#17 Avoid cade blocks more than 40 lines long
-->
<!-- RULE
#18 Separate input and output code blocks
-->
## Code examples in documentation

**DO NOT** use prompt marks (e.g. `$` or `#`) in code samples. These cause problems
for users who sometimes mistakenly type them in, or who want to copy and paste
sections of code. They also encourage poor explanation of the code.

**DO NOT** use comments in normal bash code. E.g.:

```bash
juju deploy wordpress
juju deploy ntp-master --to 2   #colocates with wordpress
juju add-relation mysql wordpress
```

This may be a useful comment if you just have a bash script to communicate
information, but we have words! It is clearer, more obvious and more helpful
to simply explain, before after or during the code.

**DO NOT** use long blocks of code. Anything which doesn't comfortably fit
on a screen is too long. Consider *why* you are showing it. Can it be broken
up into parts? Long sections of code are rarely read in documentation. If the
code is an example intended to be used rather than read, offer it as a
download instead.


**DO** separate commands and output where appropriate. For example, instead of:

```bash
juju status
environment: gce3
machines:
  "0":
    agent-state: started
    agent-version: 1.24.2
    dns-name: 104.197.44.114
...
...
```

It is more informative to break between the command and the output
with explanation. This doesn't even have to be long. It breaks up the
code blocks somewhat and makes the whole document more legible and less
likely to cause unintended naps. For example

``` bash
To check what is going on, run:


      juju status

... which should return some formatted information giving the current
state of each unit and service:

       environment: gce3
       machines:
        "0":
          agent-state: started
          agent-version: 1.24.2
...
...
```

### Placeholders in code blocks

There are many situations where it's necessary for users to provide their own
information in a code block, such as IP addresses or names. It's common to
substitute these values with a placeholder, consisting of terms within
delimiters, representing the value to be replaced. For example:

```
lxc delete <instance_name>/<snapshot_name>
```

Here, the reader is expected to substitute their values for the placeholders.
To minimise the risk of errors, instruct the reader that such values need to be
substituted, especially when the first placeholder is referenced. There is no
set style for the delimiter: the author should choose something unlikely to be
confusing in the context, and use it consistently.

In longer code blocks the placeholders become more difficult to manage
and easier to overlook. Instead, consider defining the placeholders as
environmental variables. For example:

````
Define the channel for the charms required. For example, to select the stable 
release of 1.30:

```
CHANNEL=1.30/stable
```

Then proceed to fetch the required charms:

```
juju download easyrsa --channel=$CHANNEL
juju download kubernetes-worker --channel=$CHANNEL
...
```

````

This approach has the following advantages:

 - Separates user-supplied data from commands, making it easier to reference
   and explain
 - Enables blocks of code to be copied without modification
 - Reduces the chance of users making mistakes when editing the commands

## Images

An image should not be overly cropped - allow for context.

<!-- RULE
#19 No images linked to Google drive
-->
**DO NOT LINK IMAGES FROM A GOOGLE DRIVE**
This will work, until such a time as whoever owns the image closes their account (or leaves Canonical).

## Video

Video is rarely an effective replacement for text in product documentation.
The use of videos in documentation is generally not recommended, as they are:

- Challenging to do well
- Difficult to maintain
- Prone to accessibility issues

When there is a legitimate need for video content within documentation, a tool like [asciinema](https://asciinema.org/) is preferred.
This generates text-based videos that are easier to maintain, while the text itself can be copied/pasted by the person reading the documentation.

Any videos which are included should meet the same standards of accuracy, clarity and quality expected of written documentation.

<!-- RULE
#20 Cliché words and phrases to avoid
-->
## Words and phrases to avoid

Try to avoid jargon, long-winded phrases and words with negative
connotations:

| Avoid                | Reason                  | Substitution examples               |
|----------------------|-------------------------|-------------------------------------|
|Allow                 | This suggests that we are in a position of power, permitting users or customers to conduct certain activities.|                          |
|The ability to        |                         | Use `We can` instead of `We have the ability to`                        |
|Is able to            |                         | Use `Ubuntu can` instead of `Ubuntu is able to` |
|Not only...but also...|                         |                               |
|Eliminate             |                         | `Remove`, `destroy`           |
|Execute               |                         |                               |
|Terminate             |                         | `Stop`, `destroy`             |
|Kill                  |                         | `Stop`, `destroy`             |
|Disruptive            |                         |                               |
|Explosive             |                         | `Major`, `significant`, `high impact`|
|Leverage              |                         |                               |
|Ecosystem             |                         |                               |
|Going forward         |                         |                               |
|In order to           |                         | `To`                          |
|Form factor           |                         |                               |
|Use case              |                         |                               |
|End user              |                         | `User`                        |
|Linux for human beings|                         |                               |
|Thing                 |                         |                               |
|Next level            |                         |                               |
|Harness               |                         |                               |

It can be tempting to use flowery, official-sounding words
rather than plain English. Try to keep it simple.

<!-- RULE
#25 Latinisms to avoid
-->

## Latin words and phrases

Latinisms make documents less approachable to an international audience, and we can't assume our reader is familiar with them. They disregard the principle of plain English, and, worse, are often misunderstood or misused by both readers and writers.

Instead of reaching for a Latin phrase, choose among several English equivalents:

Instead of... | Use...
--------------|-------
a priori | self-evident<br>presupposed<br>presumed<br>assumed
ad hoc | unscheduled<br>unexpected<br>improvised<br>temporary<br>bespoke
ad infinitum | and so on<br>to the fullest extent<br>recursively
cf. | refer to
caveat | warning<br>provision
circa | around<br>near
de facto | current<br>actual<br>established
ergo | therefore<br>hence
et cetera<br>etc.<br>&c | and so on
exempli gratia<br>e.g. | for example<br>as an example<br>such as
gratis | free
id est<br>i.e. | that is<br>in other words
nota bene<br>n.b. | note<br>notice<br>observe<br>pay attention to<br>keep your eye on
in situ | in-place
per diem | every day
per capita | every/each person
per se | necessarily<br>intrinsically
pro bono | freely given<br>volunteered
proviso | condition<br>provided that
stanza | division<br>block<br>paragraph<br>
status quo | state<br>state of things
verbatim | exact words<br>exactly
versus<br>vs. | compared to/with<br>opposed to
via | through<br>with<br>using
vice versa | the reverse<br>the other way around
viz. | specifically<br>namely

The following Latin words and phrases are firmly embedded in everyday English, but you can still improve a document's readability by avoiding them:

Instead of... | Consider...
--------------|------------
AM, PM<br>a.m., p.m. | Use 24-hour time.
per | each<br> every

Lastly, these Latin words and phrases are widespread in academia and research. Their meanings don't belong in documentation:

- a postiori
- ad nauseum
- et al
- ibidum, ibid.
- sic
- stet


<!-- RULE
#26 Avoid orphan demonstrative pronouns
-->

## Lone "this", "these", "those", "that"

The familiar words "this", "these", "those" and "that" serve to refer back to something previously discussed and are called _demonstrative pronouns_. They can work both on their own ("That's great!") and paired with the thing they refer to ("This apple is sweet.").

When there's no chance for ambiguity, an isolated demonstrative pronoun can flow nicely:

- Create two new instances. These will operate as your client and server.

There's no doubt here that "these" refers to the instances.

However, if there's a significant distance between a pronoun and the thing it refers to, or the previous sentence contains multiple ideas, the reader may confuse the meaning. If there's a risk of ambiguity, put the target noun immediately after the demonstrative pronoun:

- **Use**: The `yaml` object is sourced from the `yamllib` library. This object is only available if...
- **Don't use**: The `yaml` object is sourced from the `yamllib` library. This is only available if...

In the improved sentence, inserting "object" after "this" makes it clear we're referring to the object and not the library.


<!-- RULE
#27 Active voice and passive voice
-->

## Active and passive voice

Documentation contains a mix of active and passive voice. When to use each depends on the focus of the sentence.

Active voice makes the agent – the thing taking action – the subject of the sentence. In "The server hosts all the files", _the server_ is the agent. 

Passive voice occurs when we demote the agent. It either recasts the agent into an adjunct role, such as in "The files are hosted by the server", or omits the agent entirely, as in "The files are hosted".

Use each voice with care and attention. When writing about software, we often describe user actions (_You can do X_) and causes and effects (_A makes B happen_). Sometimes, only the effects matter (_A happens, B happens_). A common mistake in documentation is to _only_ describe effects, which risks disengaging the reader or obscuring the interactions between the software's components.

Consider the sentence "In Ubuntu, apps **are installed** with the App Center". This would be poor phrasing in a user guide, as the user isn't the focus. We ought to communicate that _they_ should take this action, not some unspecified entity. We can improve this sentence by adding the user as the agent – "In Ubuntu, **you can install** apps with the App Center".

When describing a user action, or a cause and its effect, it's best to include the agent in the sentence:

- **Use**: The `validate` library checks the form for errors.
- **Use**: The script deletes the files.

When describing an effect, or when the agent isn't the focus or is unknown, you can call on passive voice:

- **Use**: Before an upload, the form is checked for errors.
- **Use**: Every time the script is called, the files are deleted.

If you're uncertain about how to recognise passive voice, look for these patterns:

- is <em>verb</em>ed
- are <em>verb</em>ed
- were <em>verb</em>ed
- was <em>verb</em>ed
- been <em>verb</em>ed
- being <em>verb</em>ed
- by _agent_
- with _agent_


<!-- RULE
#21 No double space after a period/full stop
-->

## Admonitions

Admonitions (also referred to as "admonishments", "callouts" or
"notifications") are a device used in documentation to draw attention to a
particular statement or paragraph of text. Typically their use is to highlight:

 - A consequence of performing a particular action
 - An additional source of information which is useful but not required
 - A helpful tip that will save effort/time
 - A reminder of some pre-requisite or restriction

The [Vanilla framework][], which is used to publish most of our documentation,
only allows for a particular set of pre-defined admonitions (or "Notifications"
as they are referred to in that framework): **Information** and **Warning**.

Although other systems may allow for more scope it is advised to **only use these 
two types**, in the circumstances indicated below.

### Warning

The **Warning** style of admonition is appropriate where certain actions or
lack of action could have negative consequences - for example the loss of data
or a service interruption.

![An example warning notice](https://assets.ubuntu.com/v1/3a5556d1-Screenshot%20from%202024-07-10%2015-13-18.png)


### Information

The **Information** admonition should be used for general notices which don't
form part of the main narrative of the document, such as a useful shortcut, an
additional source of information or a link to a related tutorial.

![An example information notice](https://assets.ubuntu.com/v1/c952851c-Screenshot%20from%202024-07-10%2015-11-03.png)

Note that the implementation of these admonitions relates solely to the colours and
icons used with the notes. It is entirely possible to create an Information
admonition and use the label 'Useful tip' or to call a Warning 'Danger of
imminent death' to clarify the nature of the message.

Overuse of admonitions diminishes their impact and disrupts the reader's
journey, so use them sparingly and try to avoid having several in quick
succession.

## Interacting with UI elements

### Screenshots

Screenshots should be used sparingly.

A screenshot is not a replacement for clear descriptions in documentation. If an image is well described,
a screenshot shouldn’t be necessary in many situations, and including many screenshots can clutter the
documentation.

<!-- Rule#22
Images must have Alt text
-->
Screenshots also can’t be translated, so they aren’t as accessible to non-native English users or those using translated documentation. Additionally, those using screen-readers won’t be able to access the screenshots without alt-text.

### Using UI elements as the English words

<!-- Rule
#23 Don’t use UI elements as though they are English words
-->

Don’t use UI elements as though they are English words.

For example:

- **Use**: When you’re finished, click **Save** to save your settings.
- **Don’t use**: When you’re finished, **Save** your settings.

Using the UI text as English words is less clear and may not transfer well to certain translated versions.

### Click vs. Tap vs. Select

 - Use “Click” for buttons that you click on (or “Tap” if the product is primarily for mobile devices)
- Use “Select” for selecting from multiple options (e.g., a dropdown menu, multiple menu items, etc.)
- Use “Select” when there are multiple instructions separated by > (e.g., Select Preferences > Languages)

For example:

- **Use**: Click **Settings** to open your user settings.
- **Use**: Select the machines you want to register, then click **Save**.
- **Use**: Tap the application to open it.
- **Don’t use**: Select **Add bookmark** to save your bookmark.

“Click”/”Tap” is preferred over “Select” for UI elements that are definitive. This is because “Select” has an
open-ended connotation, while “Click”/”Tap” is direct and definitive. Although “Click”/”Tap” may
technically be wrong in certain situations (e.g., if a user is using the mobile version of a web page on
their desktop computer), it’s important to consider accessibility and the primary audience of the documentation
over these edge cases. Differentiating when users may have to *select* from
options or *select* more than one option can be useful for them, especially when following a longer
how-to guide (e.g., Click **X**, Click **Y**, Click **Z**, Select the settings you want to apply,
Click **Save**). This extra level of precision can also be helpful for non-native English users and
those using translated documentation.

### Bold vs. Italics

Use bold for UI elements the user clicks/selects. Use quotes or quotes with italics to draw attention to a specific word or phrase, or when referring to a word rather than using it normally.

For example:

- **Use**: Click **Save**
- **Use**: In the Computers column, click **Register a new computer**.
- **Use**: Click the link in the text *“You can register new computers by following these instructions”*.
- **Use**: Use the word “and” instead of “or”*.*
- **Use**: Use the word *“and”* instead of *“or”*.
- **Don’t use**: Once you’ve made your selections, click *Save*.

Bolding UI elements can help make the documentation easier to scan for critical information. This is especially good for users who aren’t reading the documentation for the first time and just want key information without having to sift through extraneous documentation.

### Angled brackets

You can use a right angled bracket > for navigating menu items with multiple steps.

For example:

- **Use**: Select **Preferences > Languages > English**
- **Use**: You can navigate to **File** > **Documents** and select one of your saved documents.
- **Use**: Select **Blank Document** from the **File >** **New** menu.
- **Don’t use**: Navigate to the home page > Click **Packages** > Select each package you want to export > Click **Export**

Using the right angled bracket (**>**) is at the author’s discretion; however, you’re encouraged to use this format where possible to keep things concise.

### Checkboxes

Use “Select” and ”Clear” or “Check” and ”Uncheck” together at the author’s discretion, depending on what is most natural in context.

For example:

- **Use**: Select the **Enable firewall** checkbox.
- **Use**: Clear the **Add bookmark** checkbox.
- **Use**: “Check the computer(s) you want to register” with “Uncheck any computer(s) you don’t want registered”
- **Don’t use**: Check the computer(s) you want to register, or clear any computer(s) you don’t want registered

This helps establish consistency in how we refer to checkboxes in the UI.

### Keyboard shortcuts and keyboard keys

Use “Press” when instructing the user to use a specific keyboard shortcut or keyboard key, and “Use” when instructing them to use collective or ambiguous keys.

<!-- Rule
#24 Don’t use "Click the 'Enter' Key" or derivations
-->


For example:

- **Use**: Press `Ctrl + C`
- **Use**: “To save, press `Enter`.” or “To save, press the `Enter` key”.
- **Use**: Use the arrow keys to navigate the menu.
- **Don’t use**: Click the `Enter` key.

This ensures they don’t get confused with our use of “Click”/”Tap”/”Select”.

### “Icon” vs. “Button”

“Icon” is for a symbol/image that represents an object or function, and “button” is for UI elements that initiate action when clicked. Icons typically don’t include explanatory text, and are sometimes buttons or included on a button.

If using the image of an icon or button, write the name of the icon/button directly after it or add alt-text. Avoid using the terms “icon” or “button” unless they’re needed for clarity.

For example:

- A search icon (also may be a button): ![search icon](https://assets.ubuntu.com/v1/46244ff9-magnifying_glass.png)

- A save button: ![save button](https://assets.ubuntu.com/v1/46eccbaa-Screenshot%20from%202024-02-14%2012-25-36.png)

- A reply button with an icon: ![reply button](https://assets.ubuntu.com/v1/1370f4e1-reply_button.png)

- **Use**: Click ![menu](https://assets.ubuntu.com/v1/9526cf28-menu_icon.svg) for more options. (Alt-text: “the menu”)

- **Use**: Click the ![star](https://assets.ubuntu.com/v1/821178e7-icon-orange-resources.png) star to add the page to your favorites.

- **Don’t use:** Click the ![pencil](https://assets.ubuntu.com/v1/633aab2b-pencil.png) pencil icon to edit the post.

## Hyperlinks

Here are some pointers about the general use of hyperlinks and how to format
them correctly.

### General use

Avoid excessive links in the same paragraph or instruction. If you find
yourself introducing several links in your content, consider listing them in a
separate section called "Related topics", "Additional resources", or similar.

When linking to versioned files or specific lines of code, copy the
**permalink** instead of the URL if available. This will ensure the link is
bound to the current revision of the file, so it will direct to the same
content even if the file changes.

### Formatting

Try to make the link text match the title or heading that you are referencing.
Make sure either the link text itself or the surrounding sentence provides
enough context about the contents of the linked section. 

Avoid phrases like "this document", "this article", or "click here" as the link
text.

For example, when referring to a section called "Formatting":

- Use: `See the [formatting guidelines](#formatting) for hyperlinks.`
- Use: `See the [Formatting section](#formatting) for guidelines about hyperlink formatting.` 
- Avoid: `See [Formatting](#formatting).`
- Avoid: `See [this section](#formatting).`

Avoid using a URL as the linked text.

- Use: `[Page title](https://page-url.com)`
- Avoid: `[https://page-url.com](https://page-url.com)`

Avoid superfluous links to external pages that could become outdated or
deprecated. External links such as the documentation's upstream project or
repository are fine.

Inform the user the link is external to the current doc set by specifying the source. 

- Use: `To submit an issue related to the code, see the [Contributing guide](www.github.com/org/repo/contributing.md) on GitHub.`
- Avoid: `For more information, see [How to format hyperlinks](www.external-style-guide.com/hyperlinks)`

If clicking the link performs an action, like downloading a file, link the
entire action in the sentence.

- Use: `First, [download file.zip](file.zip)`
- Avoid: `First, download the [file](file.zip)`

## FAQs

There are some grammatical issues that can cause confusion. Here are some of the main offenders.

### What is the difference between fewer and less?

Fewer means “not as many,” less means “not as much.”

A commonly-quoted example used to highlight the distinction is: “There are fewer cars on the road, which means there is less traffic.”

Also compare: “The fewer people know about this the better” and “The less people know about this the better”.

Note: The rule does not work if the number is counted as a quantity or as a unit. For example: “She paid less than ten pounds for it” or “His last jump was less than fifteen feet”.

### What is the difference between that and which?

This can, and has, caused many arguments, so it's probably best not to get too worried about it. A useful guide is: that defines, which informs.

This is not a cast-iron rule but it can help: “This is the house that Jack built, but I think the one next door, which Jack also built, is more attractive.”

“Which” is often clausal, so is predominantly preceded by a comma - compare “The police stopped the second car that was driven by a woman.” and “The police stopped the second car, which was driven by a woman.”

### Is it OK to split an infinitive?

There is no grammatical rule that says you can't split an infinitive. Sometimes, it is definitely better to split:

_"Can dot.com companies ever hope to fully recover their share values?"_

This sounds much better than moving “fully” in front of “to recover” or behind it. The key is not to write anything that is ambiguous or inelegant.


<!-- LINKS -->
[Vanilla framework]: https://vanillaframework.io/docs/patterns/notification
