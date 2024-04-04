# Open Source OHIS Radio Adapter(s?)
An open-source OHIS Radio Adapter.

As of 2024-04-04, this is a Work In Progress.

# Goals

1. Design a set of circuits that can be used to build OHIS compliant radio adapters.
2. Designs should be as simple as possible, but no simpler.
3. When laying out boards, keep as many parts through-hole as possible for ease of assembly.
4. There are two types of designs here:
    1. **General:** Has all the circuits required to work with any radio, that needs to be configured.
    2. **Radio Specific:** Trades Configurability for Simplicity.  Make a simpler device for a specific radio.

# Directory Structure

All KiCAD projects are in their own subdirectories off the git root.  Where it makes sense to do so, an additional layer of subdirectory may be used to group several projects together more obviously.

`/Documentation/` and `/docs/` are reserved for documentation source, and documentation output, respectively.

Everything in `/docs/` will be published on github Pages.
