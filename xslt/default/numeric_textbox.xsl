<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">

<xsl:variable name="identifier" select="numeric-textbox/identifier" />

<div class="container">
    <div class="form-group">
        
        <label for="{$identifier}">
            <xsl:value-of select="numeric-textbox/label"/> 
        </label>
        
        <input type="text" class="form-control form-control-sm" id="{$identifier}">
                <xsl:attribute name="min"> 
                    <xsl:value-of select="numeric-textbox/min-value"/>
                </xsl:attribute>
                <xsl:attribute name="max"> 
                    <xsl:value-of select="numeric-textbox/max-value"/>
                </xsl:attribute>
        </input>

        <small class="form-text form-text-sm text-muted">
            <xsl:value-of select="numeric-textbox/tooltip"/>
        </small>
        
  </div>
</div>

</xsl:template>
</xsl:stylesheet>
