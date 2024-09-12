**Magic Methods**

It appears that the type <method-wrapper ..> is used by CPython for methods implemented in C code. Basically the type doesn't wrap another method. Instead it wraps a C-implemented function as a bound method. In this way <method-wrapper> is exactly like a <bound-method> except that it is implemented in C.