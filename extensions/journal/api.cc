// -*- c++ -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2021 all rights reserved


// externals
#include "external.h"
// namespace setup
#include "forward.h"


// add bindings to the inventory
void
pyre::journal::py::api(py::module & m)
{
    // easy access to the manager of the global state
    m.attr("chronicler") = m.attr("Chronicler");

    // registration of the application name
    m.def(
        "application",
        // the implementation
        &pyre::journal::application,
        // the signature
        "name"_a,
        // the docstring
        "register the application {name}");

    // suppress all output
    m.def(
        "quiet",
        // the implementation
        &pyre::journal::quiet,
        // the docstring
        "suppress all channel output");

    // send output to a log file
    m.def(
        "logfile",
        // the implementation
        [](const debug_t::string_type & path) -> void {
            // set up the output device
            pyre::journal::logfile(path);
            // all done
            return;
        },
        // the signature
        "name"_a,
        // the docstring
        "send all output to a file");

    // set the maximum message decoration level
    m.def(
        "decor",
        // the implementation
        [](chronicler_t::detail_type level) -> void {
            // set the maximum detail level
            chronicler_t::decor(level);
            // all done
            return;
        },
        // the signature
        "level"_a,
        // the docstring
        "set the maximum message decoration level");

    // set the maximum message detail level
    m.def(
        "detail",
        // the implementation
        [](chronicler_t::detail_type level) -> void { chronicler_t::detail(level); },
        // the sigmature
        "level"_a,
        // the docstring
        "set the maximum message detail level");

    // all done
    return;
}


// end of file
