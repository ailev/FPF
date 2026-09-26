# Using FPF and its DPF Suites

Use the publications in this folder to help with the project's work. Paths below are relative to the folder containing this file.

When a referenced publication is present in this folder, resolve its pattern references in that copy, including references written as GitHub links. Use another edition when the task calls for an update or a comparison.

## Choose what to read

Start with the actual situation, the object being worked on, and the result the answer needs to support. If a pattern is already named, find its body directly. Otherwise search the available publications together, using terms for the difficulty and needed result. Include English technical terms when the user's language differs from the sources. You can find an individual method or a connected application without first choosing a Suite, Reference or pattern file.

Establish which publications are available for this search. The full distribution includes FPF, both DPF Suites and their References, and the independent Narrativization DPF; a downloaded subset or one attached document offers less. The public `Readme.md` and Suite `README.md` files identify the publications. A missing search result means that this search has not found an answer in its available sources. Broaden the terms or obtain the relevant publication when the present question remains unanswered.

Inspect a promising passage with its enclosing heading. A pattern body supplies its method; a Reference answer can explain how several contributions work together; a README or contents row helps locate that explanation. Open the substantive source and the conditions needed for the present use. When exploring the repertoire without a useful search phrase, browse the existing contents and FPF Part headings, then read selected full entries. The full ToC retains technical terms and dependencies for more precise searches.

To perform a selected method, read its description, applicability conditions, and the related patterns needed for that use. To use a particular technique, read its section together with the conditions it depends on. Apply it to the facts and constraints of the task.

Explain results and give feedback in the language of the project's work. Preserve the source distinctions that affect the answer. Cite the patterns and locations used. State assumptions, missing evidence, use limits, and the need for human judgement where they affect the decision. Let the current question determine the next step.

When a question needs several methods, use a relevant connected example or Practical-Use Card. Follow the intermediate results: what each method returns, which operation uses it, and what changed condition sends the work back. A mantra helps retain that connection. Read the supplying patterns and start at the contribution whose inputs are available. If one method's result leaves the larger work unresolved, search the same publications for that larger result together with the method's ID or useful terms. Continue through the connected account only where it supplies a contribution the work still needs. An adequate earlier result or a sufficient individual method can end the lookup.

Also recover the relevant Method vertical: what larger work is being performed through this action now, what constituent performances it needs, and which conditions must hold together. Use B.1.5.EW when this is unclear and B.1.5.RS for a proposed constituent replacement. A DPF can describe only part of the needed vertical. Retain already available capabilities, expose missing intermediate coordination or support, and check joint demands on shared resources. Use CGUS conditions when these facts change which continuation is available. Explain the connection in the language of the work; a formal stack diagram is optional.

## Learn the contribution the work needs

Using a method to obtain a result and learning to perform it are different purposes. Decide which contribution you need to make yourself and which can be supplied by a source, tool, specialist or AI assistant. For example, interpreting a model's limits may be necessary even when another contributor constructs and computes it. An available answer can be enough for the current work; it does not establish that you can produce or adapt it in a different situation.

When learning is the purpose, use the [Human Capability Development DPF](Engineering%20DPF%20Suite/HUMAN-CAPABILITY-DEVELOPMENT-PRINCIPLES-FRAMEWORK.md). HCD.1–.3 connect later work, current preparation and the choice of development or support. HCD.9 guides practice with feedback and correction; HCD.10 helps vary it for the missing operation. HCD.12 distinguishes evidence of applying an already learned method under a changed condition from evidence of learning a new method with a source. HCD.15 reopens development when the work or its support changes. Read only the contributions needed for your question; the order of publications is not a requirement to learn every method first.

## File structure

A publication contains several patterns, located by their IDs. For example:

| Markdown | Meaning |
| --- | --- |
| `## SYSE.24 - Choose How the Project Will Obtain a Needed Engineering Result` | Start of pattern `SYSE.24` |
| `### SYSE.24:4 - Solution` | Section of that pattern |
| `#### SYSE.24:4.1 - Name one result and one decision` | Subsection |
| `### SYSE.24:End` | End of the pattern |

IDs also occur in contents tables and cross-references. Match a heading at the start of a line to locate the pattern itself. Line numbers help retrieve portions of a file; IDs locate a pattern after its line numbers change. A reference such as `SYSE.24:4.1` points to a subsection; read it through to the next heading of the same or a higher level.

## Search and read

Use `rg` (ripgrep), or the environment's equivalent search tool with regular expressions. Run these commands with the public distribution folder as the working directory, or prepend its actual path to the file arguments. In a source repository, limit the search to the selected public publications; campaign notes and historical drafts are not the public corpus.

Inspect the available Markdown files once to establish the search scope:

```sh
rg --files --no-ignore -g '*.md' .
```

For the illustrative question “obtain a needed engineering result: build or buy”, search across that scope:

```sh
rg -n -i -C 2 --no-ignore -g '*.md' -- 'build or buy|obtain a needed engineering result|obtain climate control' .
```

This query can return a pattern, a contents row and a connected Reference case. Compare the question each passage answers, open its enclosing section and retain the useful result or return condition. If the output is too large, use the same query with `-l` instead of `-n -C 2` to list matching files, then inspect promising passages. Reformulate an unsuccessful query; a lexical match alone does not establish fit, and no match does not establish that the method is absent.

A browser or retrieval system can serve the same search when it covers the declared publications, including Reference answers. If it exposes only one file or titles, state that limit and extend access when the question requires it.

Locate the file and the start and end lines of the selected pattern:

```sh
rg -n --no-ignore -g '*.md' '^## SYSE\.24 |^### SYSE\.24:End[ \t]*\r?$' -- .
```

Read that pattern in full:

```sh
rg -U --no-heading --no-line-number --no-filename --color never '(?ms)^## SYSE\.24 [^\r\n]*\r?\n.*?^### SYSE\.24:End[ \t]*\r?$' -- "Engineering DPF Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md"
```

Here `-U` enables multiline search; `(?m)` makes `^` and `$` match line starts and ends, and `(?s)` lets a dot match a newline. `(?ms)` combines them. `.*?` matches through to the nearest specified `:End` heading; `\r?\n` accepts Windows and Unix line endings. Substitute another ID and file as needed; escape literal dots in IDs as `\.`.

For other searches, `-F` treats the query as literal text, `-i` ignores case, and `-C 2` includes neighbouring lines. `--no-ignore` searches files even in a Git-ignored folder; `-g '*.md'` selects Markdown files.

If the tool truncates a long result, read the selected text in successive line ranges with the available file reader. Folder search already covers separate publications; no combined file is needed.
