/* TFT Legal Service — interactions */
(function () {
  "use strict";

  var header = document.querySelector(".site-header");
  var navToggle = document.querySelector(".nav-toggle");
  var mainNav = document.querySelector(".main-nav");

  /* Sticky header state */
  function onScroll() {
    if (header) header.classList.toggle("is-scrolled", window.scrollY > 24);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* Mobile navigation */
  if (navToggle && mainNav) {
    navToggle.addEventListener("click", function () {
      var open = mainNav.classList.toggle("is-open");
      navToggle.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.style.overflow = open ? "hidden" : "";
    });
    mainNav.addEventListener("click", function (e) {
      if (e.target.closest("a")) {
        mainNav.classList.remove("is-open");
        navToggle.setAttribute("aria-expanded", "false");
        document.body.style.overflow = "";
      }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && mainNav.classList.contains("is-open")) {
        mainNav.classList.remove("is-open");
        navToggle.setAttribute("aria-expanded", "false");
        document.body.style.overflow = "";
        navToggle.focus();
      }
    });
  }

  /* Reveal on scroll */
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -6% 0px" }
    );
    revealEls.forEach(function (el, i) {
      var group = el.closest("[data-stagger]");
      if (group) {
        var siblings = Array.prototype.slice.call(group.querySelectorAll(".reveal"));
        var idx = siblings.indexOf(el);
        el.style.setProperty("--reveal-delay", Math.min(idx * 0.08, 0.5) + "s");
      }
      io.observe(el);
    });
  } else {
    revealEls.forEach(function (el) { el.classList.add("is-visible"); });
  }

  /* Animated counters */
  var counters = document.querySelectorAll("[data-count]");
  if ("IntersectionObserver" in window && counters.length) {
    var cio = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          var el = entry.target;
          cio.unobserve(el);
          var target = parseFloat(el.getAttribute("data-count"));
          var suffix = el.getAttribute("data-suffix") || "";
          var dur = 1600;
          var start = null;
          function tick(ts) {
            if (!start) start = ts;
            var p = Math.min((ts - start) / dur, 1);
            var eased = 1 - Math.pow(1 - p, 3);
            el.textContent = Math.round(target * eased).toLocaleString("en-US") + suffix;
            if (p < 1) requestAnimationFrame(tick);
          }
          requestAnimationFrame(tick);
        });
      },
      { threshold: 0.4 }
    );
    counters.forEach(function (el) { cio.observe(el); });
  }

  /* FAQ accordion */
  document.querySelectorAll(".faq-item").forEach(function (item) {
    var btn = item.querySelector(".faq-q");
    var panel = item.querySelector(".faq-a");
    if (!btn || !panel) return;
    btn.addEventListener("click", function () {
      var isOpen = item.classList.contains("is-open");
      document.querySelectorAll(".faq-item.is-open").forEach(function (other) {
        other.classList.remove("is-open");
        other.querySelector(".faq-q").setAttribute("aria-expanded", "false");
        other.querySelector(".faq-a").style.maxHeight = "0px";
      });
      if (!isOpen) {
        item.classList.add("is-open");
        btn.setAttribute("aria-expanded", "true");
        panel.style.maxHeight = panel.scrollHeight + "px";
      }
    });
  });

  /* Cookie banner */
  var banner = document.querySelector(".cookie-banner");
  var COOKIE_KEY = "tft-cookie-consent";
  try {
    if (banner && !localStorage.getItem(COOKIE_KEY)) {
      setTimeout(function () { banner.classList.add("is-visible"); }, 1200);
    }
    if (banner) {
      banner.querySelector("[data-cookie-accept]").addEventListener("click", function () {
        localStorage.setItem(COOKIE_KEY, "accepted");
        banner.classList.remove("is-visible");
      });
    }
  } catch (e) { /* storage unavailable */ }

  /* Contact / intake forms: validation + mailto fallback */
  document.querySelectorAll("form[data-intake-form]").forEach(function (form) {
    form.setAttribute("novalidate", "novalidate");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var valid = true;

      form.querySelectorAll("[required]").forEach(function (field) {
        var wrap = field.closest(".form-field");
        var err = wrap ? wrap.querySelector(".field-error") : null;
        var ok = field.type === "checkbox" ? field.checked : field.value.trim().length > 0;
        if (ok && field.type === "email") {
          ok = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(field.value.trim());
        }
        field.setAttribute("aria-invalid", ok ? "false" : "true");
        if (err) err.classList.toggle("is-visible", !ok);
        if (!ok) valid = false;
      });

      var status = form.querySelector(".form-status");
      if (!valid) {
        if (status) {
          status.textContent = "Please complete the highlighted fields and try again.";
          status.className = "form-status is-error";
        }
        return;
      }

      /* If a form endpoint is configured (e.g. Formspree), submit via fetch. */
      var endpoint = form.getAttribute("data-endpoint");
      if (endpoint) {
        var data = new FormData(form);
        fetch(endpoint, { method: "POST", body: data, headers: { Accept: "application/json" } })
          .then(function (res) {
            if (res.ok) {
              form.reset();
              if (status) {
                status.textContent = "Thank you. Your message has been sent — our team will reach out shortly.";
                status.className = "form-status is-success";
              }
            } else {
              throw new Error("Request failed");
            }
          })
          .catch(function () {
            if (status) {
              status.textContent = "Something went wrong. Please email us directly at info@tftlegalservice.com.";
              status.className = "form-status is-error";
            }
          });
        return;
      }

      /* Fallback: open the visitor's mail client with the form contents. */
      var name = (form.querySelector("[name=name]") || {}).value || "";
      var email = (form.querySelector("[name=email]") || {}).value || "";
      var phone = (form.querySelector("[name=phone]") || {}).value || "";
      var topic = (form.querySelector("[name=topic]") || {}).value || "General inquiry";
      var message = (form.querySelector("[name=message]") || {}).value || "";
      var body =
        "Name: " + name + "\n" +
        "Email: " + email + "\n" +
        (phone ? "Phone: " + phone + "\n" : "") +
        "Topic: " + topic + "\n\n" +
        message;
      window.location.href =
        "mailto:info@tftlegalservice.com?subject=" +
        encodeURIComponent("Website inquiry — " + topic) +
        "&body=" + encodeURIComponent(body);
      if (status) {
        status.textContent = "Opening your email client… You can also reach us directly at info@tftlegalservice.com.";
        status.className = "form-status is-success";
      }
    });
  });

  /* Footer year */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
