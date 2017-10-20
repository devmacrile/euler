; A Hamming number is a positive number which has no prime factor larger than 5.
; So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
; There are 1105 Hamming numbers not exceeding 10^8.
;
; We will call a positive number a generalised Hamming number of type n, if it has no prime factor larger than n.
; Hence the Hamming numbers are the generalised Hamming numbers of type 5.
;
; How many generalised Hamming numbers of type 100 are there which don't exceed 10^9?

(define (merge s1 s2)
    (cond ((stream-null? s1) s2)
          ((stream-null? s2) s1)
          (else
            (let ((s1car (stream-car s1))
                  (s2car (stream-car s2)))
                (cond ((< s1car s2car)
                        (cons-stream s1car (merge (stream-cdr s1) s2)))
                      ((> s1car s2car)
                        (cons-stream s2car (merge s1 (stream-cdr s2))))
                      (else
                        (cons-stream s1car
                                     (merge (stream-cdr s1)
                                            (stream-cdr s2)))))))))


(define (scale-stream stream factor)
    (stream-map (lambda (x) (* x factor)) stream))

(define (integers-starting-from n)
    (cons-stream n (integers-starting-from (+ n 1))))

(define (divisible? n x)
    (= (remainder n x) 0))

(define (sieve stream)
    (cons-stream
        (stream-car stream)
        (sieve (stream-filter
                 (lambda (x)
                    (not (divisible? x (stream-car stream))))
                 (stream-cdr stream)))))

(define primes (sieve (integers-starting-from 2)))


(define (make-merge stream-exp-a stream-exp-b)
    (list `merge stream-exp-a stream-exp-b))

(define (make-scale-stream stream-var factor)
    (list `scale-stream stream-var factor))

(display (make-scale-stream `S 5))
(display (make-merge (make-scale-stream `S 2) (make-scale-stream `S 3)))

(define (prime-merge-expression stream-var n)
    (define (iter k exp)
        (let ((p (stream-ref primes k)))
            (if (> p n)
                exp
                (iter (+ k 1) (make-merge exp (make-scale-stream stream-var p))))))
    (iter 1 (make-scale-stream stream-var 2)))

(eval (list `define `s 
        (list `cons-stream 1 (prime-merge-expression `s 100)))
        user-initial-environment)


(define (stream-values-under stream upper-bound)
    (define (iter stream count)
        (let ((next (stream-car stream)))
            (if (> next upper-bound)
                count
                (iter (stream-cdr stream) (+ count 1)))))
    (iter stream 0))

(stream-values-under s 1000000000)
;Value: 2944730
