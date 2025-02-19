"""
This document contains the regular expressions for our programming language.
® 2023 Layer Programming Language design,

Layer language overview,

    Layer is a new programming language designed to be fast and the most powerful programming language.
    What makes layer different from other programming languages is that it is completly new, different
    and different execution architecture.

Layer working and execution architecture,

    Layer does not use the traditional interpreter or compiler architecture, it uses a new architecture
    called the 'layer engine'.
    The layer code can be written in a text editor and saved with the '.layer' or '.ly' extension.
    The layer engine is a program that reads the layer code and executes it.
    But How does the layer engine work?
        The layer engine is a program which reads the layer code and performs the following steps,
            1. Lexical analysis
            2. Syntax analysis
            3. Semantic analysis
            4. Code generation (new)
            5. Code execution (new)
            but it is done in a different way than other programming languages.
        When layer code passes the first 3 steps and reaches the 4th step,
        the layer engine generates something we call it as 'super prompt' based on layer code.
        The super prompt is a new type of LLM prompt which can only be understood by the layer LLM.
            The layer LLM what we call it 'Assembly fusion' is a new type of LLM which is trained only on,
                Assembly language, X86, X86_64, ARM architectures. It is trained to understand the super prompts
                generated by the layer engine. And based on the super prompt, the layer LLM generates the ASM code.
            Then, the ASM code is what the layer engine executes. Making it the fastest programming language.

    In short,
        Layer code -> Layer engine -> Super prompt -> Layer LLM -> ASM code -> Layer engine -> Code execution

Layer Language design,

0. Basics
    0.1. Comments
        comments are ignored by the interpreter
        to comment a line, use the '#' character
        regex: ^\s*#.*$

    0.2. Indentation
        inden tation is used to define blocks
        indentation is 4 spaces
        regex: ^\s{4}.*$

    0.3. Newline
        newline is used to separate statements
        regex: ^\n$

    0.4. Whitespace
        whitespace is ignored by the interpreter
        regex: ^\s+$

    0.5. Identifiers
        identifiers are used to name variables
        identifiers can only contain letters, numbers and underscores
        identifiers cannot start with a number
        regex: ^[a-zA-Z_][a-zA-Z0-9_]*$

    0.6. Numbers
        numbers are used to represent can be integers or floats
        regex: ^[0-9]+(\.[0-9]+)?$

    0.7. Strings
        strings are used to represent text
        strings are surrounded by double quotes
        regex: ^".*"$

    0.8. Operators
        operators are used to perform operations
        operators are: +, -, *, /, %, ^, =, ==, !=, <, >, <=, >=, and, or, not
        regex: ^(\+|-|\*|/|%|\^|=|==|!=|<|>|<=|>=|and|or|not)$

    0.9. Keywords
        keywords are used to define statements
        keywords are: cvar, ivar,if, else, while, for, break, continue, def, return, class, import, from, as
        regex: ^(cvar|ivar|if|else|while|for|break|continue|def|return|class|import|from|as)$

    0.10. Punctuation
        punctuation is used to separate statements
        punctuation is: ., ,, :, (, ), [, ], {, }
        regex: ^(\.|,|:|\(|\)|\[|\]|\{|\})$

    0.11. Boolean
        boolean is used to represent true or false
        boolean is: true, false
        regex: ^(true|false)$


1.0 Statements

    1.1. Variable declaration and initialization

        variable declaration is used to declare variables
        there are two types of variables, cvar and ivar
            cvar is a 'create variable' for which the value assignment is optional
            ivar is a 'initialize variable' for which the value assignment is mandatory

        1.1.1 cvar
            cvar example : cvar age
            or
            cvar age = 5
            :cvar <keyword> <identifier>
            or
            :cvar <keyword> <identifier> = <expression>

        1.1.2 ivar
            ivar example : ivar age = 5
            :ivar <identifier> = <expression>
            regex: ^:cvar <identifier>( = <expression>)?$

    1.2. Print statement

        print statement is used to print values to the console
        print statement in layers is as powerful as the print function in python but with some limitations

        1.2.1. Print statements
            there are two types of print statements, print and fprint
            print statement
                print statement is used to print values to the console
                print statement in layers is as powerful as the print function in python
                print statement example : print("Hello World! from layers programming language")
                print statement example : print(5)
                print statement example : print(5 + 5)
                print statement example : print(5 + 5, 5 - 5, 5 * 5, 5 / 5, 5 % 5, 5 ^ 5)

                regex: ^print\((.*)\)$


            fprint statement
                fprint statement is formatter print statement just like print(f"Hello {name}!") in python
                fprint statement example : fprint("Hello {name}!")
                fprint statement example : fprint("Hello {name}!", name = "World")

                regex: ^fprint\((.*)\)$

    1.3 Loops

        loops are used to repeat a block of code
        there are two type of loops, while and for
        loops in layer is very different from loops in python or other programming languages

        1.3.1 for loop

                for loop example : loop for 5 times -> print("Hello World!")
                for loop example : loop i for 5 times -> print(i)
                for loop example : loop x for 10 times -> { print(x) } or can be multiline also.
                for loop example : loop x for 10 times -> {
                print(x)
                print(x + 1)
                print(x + 2)
                }
                syntax: loop <identifier> for <expression> times -> <block>
                or
                syntax: loop <identifier> for <expression> times -> { <block> }

                regex: ^loop ([a-zA-Z_][a-zA-Z0-9_]*) for ([0-9]+) times -> (.*)$
                or
                regex: ^loop ([a-zA-Z_][a-zA-Z0-9_]*) for ([0-9]+) times -> \{(.*)\}$

        1.3.2 while loop

                while loop example : loop while i < 5 -> print(i)
                while loop example : loop while i < 5 -> { print(i) }
                while loop example : loop while i < 5 -> {
                print(i)
                print(i + 1)
                print(i + 2)
                }
                syntax: loop while <expression> -> <block>
                or
                syntax: loop while <expression> -> { <block> }

                regex: ^loop while (.*) -> (.*)$
                or
                regex: ^loop while (.*) -> \{(.*)\}$

    1.4 Conditional statements

        conditional statements are used to execute a block of code if a condition is true
        there are three types of conditional statements, if, if-else, else

        1.4.1 if statement

            if statement example : if i < 5 -> print(i)
            if statement example : if i < 5 -> { print(i) }
            if statement example : if i < 5 -> {
                print(i)
                print(i + 1)
                print(i + 2)
            }
            syntax: if <expression> -> <block>
            or
            syntax: if <expression> -> { <block> }

            regex: ^if (.*) -> (.*)$
            or
            regex: ^if (.*) -> \{(.*)\}$

            1.4.1.1 break statement

                break statement is used to break out of a loop
                break statement example : if i < 5 -> break
                break statement example : if i < 5 -> { break }
                break statement example : if i < 5 -> {
                break
                }
                syntax: if <expression> -> break
                or
                syntax: if <expression> -> { break }

                regex: ^if (.*) -> break$
                or
                regex: ^if (.*) -> \{ break \}$

"""