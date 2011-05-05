// -*- C++ -*-
// -*- coding: utf-8 -*-
//
// michael a.g. aïvázis
// california institute of technology
// (c) 1998-2011 all rights reserved
//


#if !defined(pyre_jourmal_Selector_h)
#define pyre_journal_Selector_h


// forward declarations
namespace pyre {
    namespace journal {
        class Selector;
    }
}


// the injection operator; should be at global scope
template <typename Channel>
inline
pyre::journal::Diagnostic<Channel> &
operator << (pyre::journal::Diagnostic<Channel> &, const pyre::journal::Selector &);


// definitions
// attributes
class pyre::journal::Selector {
    // types
public:
    typedef std::string string_t;
    // interface
public:
    template <typename Channel>
    inline
    Diagnostic<Channel> & 
    inject(Diagnostic<Channel> & channel) const;

    // meta methods
public:
    inline ~Selector();
    inline Selector(string_t, string_t);
    // disallow
private:
    inline Selector(const Selector &);
    inline Selector & operator= (const Selector &);

    // data
private:
    string_t _key;
    string_t _value;
};


// get the inline definitions
#define pyre_journal_Selector_icc
#include "Selector.icc"
#undef pyre_journal_Selector_icc

#endif // pyre_journal_manipulators_0_h

// end of file
