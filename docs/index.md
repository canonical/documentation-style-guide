# Documentation Style Guide

This is a minimal guide to the language and style conventions used
for Canonical documentation projects.

```{eval-rst}
.. toctree::
   :maxdepth: 2
   :hidden:

   self

```

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

## Branding

Consistency in branding is important for a number of reasons, including the protection of trademarks where they apply.
For our own products, and those of others we mention frequently, the following guidance applies.

### Ubuntu

When we refer to Ubuntu |oǒ'boǒntoō|, we are usually referring to the distribution, rather than the Ubuntu project itself.

Our convention is to use the name, followed by the release number and, if applicable, 'LTS' to denote that the version
is in Long Term Support. Optionally, you may also further identify the release by its codename (the first or both parts
of the release name) if this is likely to be useful For example, some of our products also use the release names to identify
versions.

<!-- RULE
#03 Correct use of Ubuntu versions
-->
Some examples of correct usage:

- **Ubuntu 22.04 LTS**
- **Ubuntu 22.10**
- **Ubuntu 23.04 (Lunar Lobster)** _(note case!)_
- **Ubuntu 23.10 (Mantic)**
- **Ubuntu 24.04 LTS (Noble Numbat)**

This also applies to more specific products, such as **Ubuntu Server 22.04 LTS**.

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
Note: Removed from written guide, still retained in automation.
-->

## Contractions

Contractions are very common in spoken English and in many types of writing.
Avoiding the use of them entirely makes it difficult to achieve a friendly,
conversational tone. However, we should keep to contractions that are commonly
understood and not part of some regional dialect, and only use them in
"conversational" parts of the documentation such as explanatory text.

<!-- RULE
#06 Forbidden contractions
-->

### Forbidden contractions

<!-- vale Canonical.000-US-spellcheck = NO -->

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

<!-- vale Canonical.000-US-spellcheck = YES -->

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

 - Avoid overusing punctuation in headings. Headings should not end with a period/full point/full stop.
 - Avoid links in headings.
 - Don't overuse `code` styling in headings - it can be useful to document command references, for example, but you should always consider if it is really needed.
 - Do not skip levels of heading hierarchy. For example, do not follow an `h1` with an `h3`.
 - Headings require content and should not be followed directly by a subheading.

<!-- RULE
#12 Dates should follow 'January 1, 1970' format
-->

## Dates

For consistency, we use the following date format:

* Single day: January 1, 2013  
* Date range within same month: January 1-2, 2013  
* Date range across two or more months: January 1 \- February 2,  2013

<!-- RULE
#13 Numbers below 10 should be spelled out
-->
<!-- RULE
#14 Numbers above 9 should be written in the '1,970' format
-->

## Numbers

Numbers in single figures should be spelled out in most cases. From
10 onward, numbers should be written in digits.

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

Use of prompt marks such as `$` and `#` in code samples **must** allow users to copy
the code. Otherwise prompt marks cause problems for users.

**DO NOT** use comments in normal bash code. For example:

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
likely to cause unintended gaps. For example:

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

```{note}
For Canonical documentation, you may want to use the [sphinx-terminal](https://github.com/canonical/sphinx-terminal) extension, which natively separates code input and output.
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
This is not accessible for external contributors. Also, this will only work temporarily. Google Drive can rotate URLs and when a user
leaves or closes their account the asset will be unavailable.

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
Note: Removed from written guide
-->

<!-- RULE
#25 Latin words to avoid
-->

## Latin words and phrases

Latin words and phrases make documents less approachable to an international audience, and we can't assume our reader is familiar with them. They disregard the principle of plain English, and, worse, are often misunderstood or misused by both readers and writers.

Instead of reaching for a Latin phrase, choose among several English equivalents:

<!-- vale Canonical.000-US-spellcheck = NO -->

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

<!-- vale Canonical.000-US-spellcheck = NO -->

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

## Admonitions

Admonitions (also referred to as "admonishments", "callouts" or
"notifications") are a device used in documentation to draw attention to a
particular statement or paragraph of text. Typically their use is to highlight:

 - A consequence of performing a particular action
 - An additional source of information which is useful but not required
 - A helpful tip that will save effort/time
 - A reminder of some pre-requisite or restriction

**Try to avoid hint and tip admonitions**, as admonitions should be of higher levels or importance.

## Interacting with UI elements

### Screenshots

Do not use screenshots unless there is no better way to better indicate the interaction or interface you are documenting.

A screenshot is not a replacement for clear descriptions in documentation. If an image is well described,
a screenshot shouldn’t be necessary in many situations, and including many screenshots can clutter the
documentation.

<!-- Rule#22
Images must have Alt text
-->
Screenshots also can’t be translated, so they aren’t as accessible to non-native English users or those using translated documentation. Additionally, those using screen-readers won’t be able to access the screenshots without alt-text.

### Using UI elements as the English words

Use UI elements as though they are English words.

For example:

- **Use**: When you’re finished, **Save** your settings.
- **Don't use**: When you’re finished, click **Save** to save your settings.

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

## Lists

Use numbered lists sparingly, and ensure that bulleted lists are definitive lists, not examples or subsets of a category.

Numbered lists should be used only when:

- The order of items matters, such as in step-by-step instructions
- You need to reference specific items by number
- You're describing a process or sequence

Bulleted lists are preferred for most other situations because they're easier to scan
and don't imply a hierarchy or sequence that may not exist. Overusing numbered lists
can make documentation feel unnecessarily rigid and make it harder to maintain,
especially when items need to be added or removed.

<!-- LINKS -->
[Vanilla framework]: https://vanillaframework.io/docs/patterns/notification
